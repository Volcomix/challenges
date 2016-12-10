import fileinput
import os
import sys

BUILD_DIR = './.build'

if len(sys.argv) != 2:
    print('''
Usage: python builder/build.py <filename>

Recursively merge all python files in current directory and subdirectories.
Directories and files starting with '.' or '__' are excluded from the search. \
The 'builder' directory is ignored as well.
A '.build' directory will be created in the current directory. \
This directory will contain all challenge files merged in \
a single output file named <filename>.

Arguments:
 <filename>     Must be a python file name (not a path) located in the current
                directory. If <filename> does not end with the '.py' extension,
                it will be added automatically.
''')
    sys.exit()

challenge_file = sys.argv[1]
if not challenge_file.endswith('.py'):
    challenge_file += '.py'

def walk_dir(path):
    files = []
    for entry in os.scandir(path):
        if (
            entry.name == 'builder' or
            entry.name.startswith('.') or
            entry.name.startswith('__')
        ):
            continue
        if entry.is_file():
            files.append(entry.path)
        else:
            files.extend(walk_dir(entry.path))
    return files

def walk_root():
    files = []
    for directory in os.scandir('.'):
        if (
            directory.is_dir() and
            directory.name != 'builder' and
            not directory.name.startswith('.') and
            not directory.name.startswith('__')
        ):
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
         open(BUILD_DIR + '/' + challenge_file, 'w') as out_file, \
         open('./' + challenge_file, 'r') as main_file:
        
        main_lines = main_file.readlines()
        main_line_idx = write_imports(main_lines, out_file)

        for line in in_file:
            if not line.startswith('import') and not line.startswith('from'):
                out_file.write(line)
        
        write_main(main_lines, main_line_idx, out_file)

write_output(walk_root())
