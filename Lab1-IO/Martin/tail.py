import sys
import os
import json

def parse_args(args):
    files = []
    lines = 10
    skipnext = False
    for i, arg in enumerate(args):
        if skipnext:
            skipnext = False
            continue
        if arg == "-l":
            lines = int(args[i+1])
            skipnext = True # Skip next line of iteration
        else:
            files.append(arg)
    return files, lines


if __name__ == "__main__":

    files, linecount = parse_args(sys.argv[1:])

    for file in files:

        parsed_bytes = 0
        parsed_lines = 0
        with open(file, 'rb') as f:
            f.seek(0, os.SEEK_END)
            position = f.tell()
            while position != 0 and parsed_lines <= linecount:
                ch = f.read(1)
                if ch == b'\n':
                    parsed_lines += 1
                parsed_bytes += 1
                f.seek(f.tell() - 2, os.SEEK_SET)
                position = f.tell()

            lines = f.read(parsed_bytes).split(b'\n')

        print(f">>> {file}")
        for line in lines:
            print(line.decode("utf-8"))
        print("\n")
