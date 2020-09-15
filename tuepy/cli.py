from sys import argv
from subprocess import Popen
from .todo import TodoManager

def main():

    # Initialize TodoManager and Load Data
    tm = TodoManager()
    tm.load()

    # Default Command: If no argument supplied,
    # show weekly summary of latest week
    if len(argv) == 1:
        tm.weekly_summary(str(tm.latest_week()))

    # Add a Todo: if arg 1 == 'a'
    elif argv[1] == 'a':
        todo = " ".join(argv[2:]).split(':')
        tm.add(todo)
        print("Added", split)

    # Show Weekly Summary: is arg 1 == 'w'
    elif argv[1] == 'w':
        week = argv[2]
        tm.weekly_summary(week)

    # Update Task Progress: if arg 1 is digit AND arg 2 is digit
    elif argv[1].isdigit() and argv[2].isdigit():
        tm.set_progress(argv[1], argv[2])

    # Remove task by id: if arg 1 is digit AND arg 2 is 'rm'
    elif argv[1].isdigit() and argv[2] == 'rm':
        tm.remove_by_id(argv[1])

    # Mark task as done: if arg 1 is digit and arg 2 == 'done'
    elif argv[1].isdigit() and argv[2] == 'done':
        tm.set_progress(argv[1], 100)

    # Open csv datafile with default system application (Excel)
    elif argv[1] == "edit":
        print(f"Opening {tm.data_path} with Excel")
        excel = Popen(tm.data_path, shell=True)
    
    # Run Test function: is arg 1 == 'test'
    elif argv[1] == "test":
        tm.test()
