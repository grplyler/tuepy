from sys import argv
from subprocess import Popen
from .todo import TodoManager, Todo

def main():
    tm = TodoManager()
    tm.load()

    # If no argument supplied,
    # show weekly summary of latest week
    if len(argv) == 1:
        tm.weekly_summary(str(tm.latest_week()))

    # Add a Todo
    elif argv[1] == 'a':
        split = " ".join(argv[2:]).split(':')
        todo = Todo(split[0], split[1], split[2], split[3], split[4])

        tm.add(todo)
        print("Added", split)

    # Show Weekly Summary
    elif argv[1] == 'w':
        week = argv[2]
        tm.weekly_summary(week)

    # Update Task Progress
    elif argv[1].isdigit() and argv[2].isdigit():
        tm.set_progress(argv[1], argv[2])

    # Remove task by id
    elif argv[1].isdigit() and argv[2] == 'rm':
        tm.remove_by_id(argv[1])

    # Mark task as done
    elif argv[1].isdigit() and argv[2] == 'done':
        tm.set_progress(argv[1], 100)

    # Open csv datafile with Excel
    elif argv[1] == "edit":
        print(f"Opening {tm.data_path} with Excel")
        excel = Popen(tm.data_path, shell=True)



    