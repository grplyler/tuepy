
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
        datafile = path.expanduser("~/tue.csv")
        if not path.exists(datafile):
            print("Intializing datafile:", datafile)
            with open(datafile, "w") as output:
                output.write("class,week,title,progress,type\n")

        return datafile
            
    # Add a Todo
    def add(self, todo):
        self._data.append([
            todo.cls,
            todo.week,
            todo.title,
            todo.progress,
            todo.type
        ])

        self.save()

    def set_progress(self, id, progress):
        index = 0
        for row in self._data:
            if index == int(id):
                self._data[index][3] = progress
            index += 1

        self.save()
        print(f"Progress on task {id} set to {progress}%.")


    def load(self):

        with open(self.data_path) as datafile:
            csvreader = csv.reader(datafile)

            # Skip Headers
            next(csvreader)
            
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
                
                current_class = todo[0]
                if current_class != last_class:
                    # Print Class Header if Changed
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
            percent = (done / total) * 100
            complete = f"[ {percent:.2f}% done ]"
            # print(fl(complete, width=62, fill='='))

            print("+==============================================================")
            print(f"{progress(percent, fill='█', start='|', end='', width=48)}{complete}")
            print("+==============================================================")


    def save(self):

        # Sort Data by week then class
        self._data = sorted(self._data, key=lambda element: (element[1], element[0]))

        with open(self.data_path, 'w', newline='') as datafile:
            csvwriter = csv.writer(datafile)
            csvwriter.writerow(['class', 'week', 'title', 'progress', 'type'])
            csvwriter.writerows(self._data)


class Todo(object):
    
    def __init__(self, cls="", week=3, title="", progress=0, type="study"):
        self.cls = cls #class
        self.week = week
        self.title = title
        self.progress = progress
        self.type = type

    def print(self):
        print(f"{self.cls} {self.week} {self.title} {self.progress} {self.type}")
   