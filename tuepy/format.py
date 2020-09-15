
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

def print_task(task, index=0):
    prog = task[3]
    title = task[2]
    index_fmt = f"{fl(str(index),2)}"
    print(f"|{index_fmt} {progress(prog, fill='█', start='|', end='|')} {title}")
