
import csv
from os import path
from .format import fr, fl, progress, print_task


class TodoManager(object):

    def __init__(self):
        super().__init__()
        self.todos = []
        self._data = []
        self.data_path = self._boot()
        
    # ensure ~/.tue.csv exists, create if not
    def _boot(self):

        # Get tue.csv file in users home dir
        datafile = path.expanduser("~/tue.csv")

        # Check it data file exists, create if not
        if not path.exists(datafile):
            print("Intializing datafile:", datafile)
            with open(datafile, "w") as output:
                output.write("class,week,title,progress,type\n")

        # Return path to data file
        return datafile

    def test(self):
        # Test function for doing testy stuff
        pass
            
    def add(self, todo):

        # Add Todo to data
        self._data.append([
            todo[0],
            todo[1],
            todo[2],
            todo[3],
            todo[4],
        ])

        # Save Data
        self.save()

    def set_progress(self, id, progress):
        # Set the progress for a given task id
        # (todo[3] == progress)

        index = 0
        for row in self._data:
            if index == int(id):
                self._data[index][3] = progress
            index += 1

        # Save
        self.save()
        print(f"Progress on task {id} set to {progress}%.")


    def load(self):

        # Load CSV data to self._data
        with open(self.data_path) as datafile:
            csvreader = csv.reader(datafile)

            # Skip Headers
            next(csvreader)
            
            # Read Rows
            for row in csvreader:
                if len(row) > 0:
                    self._data.append(row)

        # Sort Data by week then class
        self._data = sorted(self._data, key=lambda element: (element[1], element[0]))

    # Return Number of most recent (latest) week
    def latest_week(self):
        latest = 0
        for row in self._data:
            current = int(row[1])
            if current > latest:
                latest = current

        return latest

    # Remove
    def remove_by_id(self, id):
        index = 0
        newdata = []

        for row in self._data:
            if index != int(id):
                newdata.append(row)

            index += 1

        self._data = newdata
        self.save()

        print(f"Task {id} removed.")

    def weekly_summary(self, week):

        total = 0
        done = 0
        index = 0
        last_class = ""

        # Print Weekly Summary Header
        print("+-------------------------------------------------------------+")
        print(f"|                           Week {week}                             ")


        for todo in self._data:

            if todo[1] == week:
                
                # If we've encountered a new class, print the class header
                current_class = todo[0]
                if current_class != last_class:
                    name = f"[ {todo[0]} ]"
                    print(f"+----+----------+{fl(name, 45, '-')}")
                
                # Print Task
                prog = int(todo[3])
                title = todo[2]
                ttype = todo[4]
                
                index_fmt = f"{fl(str(index),2)}"
                print(f"|{index_fmt} {progress(prog, fill='█', start='|', end='|')}{fr(title, 34)}")

                total += 100
                done += int(todo[3])
                last_class = todo[0]

            index += 1

        
        # Display % done
        if total != 0:

            # Calculation Total Percentage Done
            percent = (done / total) * 100
            complete = f"[ {percent:.2f}% done ]"

            # Print Total Progress Footer
            print("+==============================================================")
            print(f"{progress(percent, fill='█', start='|', end='', width=48)}{complete}")
            print("+==============================================================")


    def save(self):

        # Sort Data by week then class
        self._data = sorted(self._data, key=lambda element: (element[1], element[0]))

        # Write Data lines to CSV files
        with open(self.data_path, 'w', newline='') as datafile:
            csvwriter = csv.writer(datafile)
            csvwriter.writerow(['class', 'week', 'title', 'progress', 'type'])
            csvwriter.writerows(self._data)
