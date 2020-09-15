def progress(percent, width=10, start='[', end=']', fill='*'):
    filled = round((int(percent) / 100) * width)
    empty = width - filled
    return f"{start}{fill * filled}{' ' * empty}{end}"

def fr(data, width, fill=' ', first='', last=''):
    padding = width - len(data)
    return f"{first}{data}{fill * padding}{last}"

def fl(data, width, fill=' ', first='', last=''):
    padding = width - len(data)
    return f"{first}{fill * padding} {data}{last}"

def print_task(task, index=0):
    prog = task[3]
    title = task[2]
    index_fmt = f"{fl(str(index),2)}"
    print(f"|{index_fmt} {progress(prog, fill='█', start='|', end='|')} {title}")
