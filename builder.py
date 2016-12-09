import os
import fileinput

BUILD_DIR = './.build'
OUTPUT_FILE = 'output.py'
MAIN_FILE = 'main.py'

def walk_dir(path):
    files = []
    for entry in os.scandir(path):
        if entry.name.startswith('.') or entry.name == '__pycache__':
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

def write_imports(lines, out_file):
    n = len(lines)
    i = 0
    while i < n:
        line = lines[i]
        if line.startswith('import') or line.startswith('from'):
            out_file.write(line)
            i += 1
        else:
            break
    return i

def write_main(lines, start_idx, out_file):
    n = len(lines)
    i = start_idx
    while i < n:
        line = lines[i]
        if not line.startswith('import') and not line.startswith('from'):
            out_file.write(line)
        i += 1

def write_output(files):
    if not os.path.exists(BUILD_DIR):
        os.mkdir(BUILD_DIR)
    with fileinput.input(files) as in_file, \
         open(BUILD_DIR + '/' + OUTPUT_FILE, 'w') as out_file, \
         open('./' + MAIN_FILE, 'r') as main_file:
        
        main_lines = main_file.readlines()
        main_line_idx = write_imports(main_lines, out_file)

        for line in in_file:
            if not line.startswith('import') and not line.startswith('from'):
                out_file.write(line)
        
        write_main(main_lines, main_line_idx, out_file)

write_output(walk_root())