import os
import sys

INPUT_FILE = os.path.join(os.path.dirname(__file__), '../triangle-input.txt')

def is_valid(triangle):
    sides = [int(s) for s in triangle]
    return ((sides[0] + sides[1]) > sides[2] and
            (sides[1] + sides[2]) > sides[0] and
            (sides[2] + sides[0]) > sides[1])

def reformat_lines(lines):
    for i in range(0, len(lines), 3):
        group = [l.split() for l in lines[i:i+3]]
        for j in range(0, 3):
            yield [x[j] for x in group]


with open(INPUT_FILE, 'r', encoding='utf8') as file:
    if '-1' in sys.argv:
        num_of_invalid = len([l for l in file.readlines() if is_valid(l.split())])
    else:
        num_of_invalid = len([t for t in reformat_lines(file.readlines()) if is_valid(t)])

    print(f'Number of valid rectangles: {num_of_invalid}')