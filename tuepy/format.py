# Generate a Progress Bar
def progress(percent, width=10, start='[', end=']', fill='*'):
    filled = round((int(percent) / 100) * width)
    empty = width - filled
    return f"{start}{fill * filled}{' ' * empty}{end}"

# Fill Right
def fr(data, width, fill=' ', first='', last=''):
    
    # Calculate how many padding characters we need on the right
    padding = width - len(data)

    return f"{first}{data}{fill * padding}{last}"

# Fill Left
def fl(data, width, fill=' ', first='', last=''):
    padding = width - len(data)
    return f"{first}{fill * padding} {data}{last}"

def print_task(todo, index=0):
    prog = int(todo[3])
    title = todo[2]
    ttype = todo[4]
    
    index_fmt = f"{fl(str(index),2)}"
    print(f"|{index_fmt} {progress(prog, fill='█', start='|', end='|')}{fr(title, 34)}")


def print_class_header(todo):
    name = f"[ {todo[0]} ]"
    print(f"+----+----------+{fl(name, 45, '-')}")

def print_week_header(week):
    print("+-------------------------------------------------------------+")
    print(f"|                           Week {week}                             ")

# todo: add print progress footer