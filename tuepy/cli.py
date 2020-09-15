from sys import argv
from subprocess import Popen
from .todo import TodoManager

def main():

    # Initialize TodoManager and Load Data


    # Default Command: If no argument supplied,
    # show weekly summary of latest week


    # Add a Todo: if arg 1 == 'a'


    # Show Weekly Summary: is arg 1 == 'w'


    # Update Task Progress: if arg 1 is digit AND arg 2 is digit


    # Remove task by id: if arg 1 is digit AND arg 2 is 'rm'


    # Mark task as done: if arg 1 is digit and arg 2 == 'done'


    # Open csv datafile with default system application (Excel)

    
    # Run Test function: is arg 1 == 'test'
    elif argv[1] == "test":
        tm.test()
