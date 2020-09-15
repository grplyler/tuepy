
import csv
from os import path
from .format import fr, fl, progress, print_task


class TodoManager(object):

    def __init__(self):             # Constructor (takes no arguments)
        super().__init__()          # Call constructor on parent class
        self.todos = []             
        self._data = []

        # Load data and set data path
        self.data_path = self._boot()
        
    def _boot(self):

        # Get tue.csv file in users home dir

        # Check it data file exists, create if not


        # Return path to data file
        pass

    def test(self):
        # Test function for doing testy stuff
        pass
            
    def add(self, todo):

        # Add Todo to data

        # Save Data

        pass


    def set_progress(self, id, progress):
        # Set the progress for a given task id
        # (todo[3] == progress)

        # Save
        self.save()
        print(f"Progress on task {id} set to {progress}%.")


    def load(self):

        # Load CSV data to self._data
 

            # Skip Headers

            
            # Read Rows


        # Sort Data by week then class
        self._data = sorted(self._data, key=lambda element: (element[1], element[0]))

    # Return Number of most recent (latest) week
    def latest_week(self):
        pass

    # Remove
    def remove_by_id(self, id):
        index = 0
        newdata = []

        # loop over data

            # if index != int: append row to newdata

            # update index counter

        # Save data

        pass

    def weekly_summary(self, week):

        total = 0
        done = 0
        index = 0
        last_class = ""

        # Print Weekly Summary Header
        print_week_header(week)

        # Loop over todos
        for todo in self._data:

            # If the todo belongs to the week we want
                
                # If we've encountered a new class, print the class header
                
                # Print Task

                # Update counters

            # Update index
            index += 1


        
        # Display % done
        if total != 0:

            # Calculation Total Percentage Done


            # Print Total Progress Footer

            pass



    def save(self):

        # Sort Data by week then class
        self._data = sorted(self._data, key=lambda element: (element[1], element[0]))

        # Write Data lines to CSV files
        pass
