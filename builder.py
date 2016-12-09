import os
import fileinput

BUILD_DIR = './.build'
OUTPUT_FILE = 'output.py'

def walk_dir(path):
    files = []
    for entry in os.scandir(path):
        if entry.name.startswith('.'):
            continue
        if entry.is_file():
            files.append(entry.path)
        else:
            files.extend(walk_dir(entry.path))
    return files

def walk_root():
    files = []
    for directory in os.scandir('.'):
        if not directory.name.startswith('.') and directory.is_dir():
            files.extend(walk_dir(directory.path))
    return files

def write_output(files):
    if not os.path.exists(BUILD_DIR):
        os.mkdir(BUILD_DIR)
    with open(BUILD_DIR + '/' + OUTPUT_FILE, 'w') as out_file, \
        fileinput.input(files) as in_file:
        for line in in_file:
            if not line.startswith('import') and not line.startswith('from'):
                out_file.write(line)

write_output(walk_root())