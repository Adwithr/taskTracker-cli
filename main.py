import sys
import json
import os

file_name = "tasks.json"

#Helper functions
def load_file():
    if os.path.exists(file_name):
        with open(file_name,'r') as file:
            return json.load(file)
    else:
        return []

def save_file(database):
    with open(file_name,'w') as file:
        json.dump(database,file,indent=4)


def add(obj):
    database = load_file()
    database.append(obj)
    save_file(database)

    
