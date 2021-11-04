
import sys
from collections import deque

def single_tail(file, lines):
    q = deque([], maxlen = lines + 1)

    with open(file) as f:
        line = f.readline()
        while line:
            line = f.readline()
            q.append(line)
    while q:
        print(q.popleft(), end="")


def main(argv):
    single_tail(argv[0])
    
if __name__ == "__main__":
    main(sys.argv[1:])
