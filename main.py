import sys
import json
import os
from datetime import datetime

file_name = "tasks.json"

def load_file():
    if os.path.exists(file_name):
        with open(file_name,'r') as file:
            return json.load(file)
    else:
        return []

def save_file(database):
    with open(file_name,'w') as file:
        json.dump(database,file,indent=4)


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
        "updatedAt": formatted_time
    }
    database.append(task)
    save_file(database)

def main():
    command = sys.argv[1].lower()
    if command == 'add':
        add(sys.argv[2])

main()