Task Tracker is a project that is used to track and manage your tasks. It is a simple command line interface (CLI) written in python to track what you need to do, what you have done, and what you are currently working on.

Run `pip install -e .` to use the task-cli prefix in cli, else use `python main.py`

```bash
#Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
```

This project helped me practice my programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.
