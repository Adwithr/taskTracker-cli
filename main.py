import sys
import json
import os
from datetime import datetime

file_name = "tasks.json"


def load_file():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    else:
        return []


def save_file(database):
    with open(file_name, "w") as file:
        json.dump(database, file, indent=4)


def add(desc):
    database = load_file()
    date = datetime.now()
    formatted_time = date.strftime("%Y-%m-%d %H:%M:%S")
    next_id = max([task["id"] for task in database], default=0) + 1
    task = {
        "id": next_id,
        "description": desc,
        "status": "todo",
        "createdAt": formatted_time,
        "updatedAt": formatted_time,
    }
    database.append(task)
    save_file(database)
    print(f"Task added successfully! (ID: {next_id})")


def update(id, desc):
    database = load_file()
    id = int(id)
    date = datetime.now()
    formatted_time = date.strftime("%Y-%m-%d %H:%M:%S")

    for data in database:
        if data["id"] == id:
            data["description"] = desc
            data["updatedAt"] = formatted_time
            save_file(database)
            break
    else:
        print("Invalid ID")
        return


def delete(id):
    database = load_file()
    id = int(id)

    for data in database:
        if data["id"] == id:
            task = data
            break
    else:
        print("Invalid ID")
        return

    database.remove(task)
    save_file(database)
    print("Task deleted succesfully!")


def markInProgress(id):
    database = load_file()
    id = int(id)

    for data in database:
        if data["id"] == id:
            data["status"] = "in-progress"
            break
    else:
        print("Invalid ID")
        return
    save_file(database)


def markDone(id):
    database = load_file()
    id = int(id)

    for data in database:
        if data["id"] == id:
            data["status"] = "done"
            break
    else:
        print("Invalid ID")
        return
    save_file(database)


def main():
    command = sys.argv[1].lower()
    if command == "add":
        add(sys.argv[2])
    elif command == "update":
        update(sys.argv[2], sys.argv[3])
    elif command == "delete":
        delete(sys.argv[2])
    elif command == "mark-in-progress":
        markInProgress(sys.argv[2])
    elif command == "mark-done":
        markDone(sys.argv[2])


main()
