Task Tracker is a project that is used to track and manage your tasks. It is a simple command line interface (CLI) written in python to track what you need to do, what you have done, and what you are currently working on.

```bash
#Adding a new task
python main.py add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
python main.py update 1 "Buy groceries and cook dinner"
python main.py delete 1

# Marking a task as in progress or done
python main.py mark-in-progress 1
python main.py mark-done 1

# Listing all tasks
python main.py list

# Listing tasks by status
python main.py list done
python main.py list todo
python main.py list in-progress
```

This project helped me practice my programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.
