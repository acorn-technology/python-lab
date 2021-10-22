import sys
import os

NEWLINE = b"\n"[0]

def last_lines_simple(file, num_of_lines = 10):
    with open(file, "r", newline='') as stream:
        lines = stream.readlines()
        return "".join(lines[-min(num_of_lines, len(lines)):])

def last_lines(file, num_of_lines = 10):
    with open(file, 'br') as stream:
        block_size = 512
        stream.seek(0, os.SEEK_END)

        lines_remaining = num_of_lines
        file_length = stream.tell()
        offset = 0

        while file_length > offset and lines_remaining > 0:
            offset = min(file_length, offset + block_size)
            stream.seek(-offset, os.SEEK_END)
            block = stream.read(block_size)
            lines_remaining -= block.count(NEWLINE)

        i = 0
        while lines_remaining < 0 or (lines_remaining == 0 and block[i] != NEWLINE):
            if block[i] == NEWLINE:
                lines_remaining += 1

            i += 1

        if block[i] == NEWLINE:
            i += 1

        offset -= i
        stream.seek(-offset, os.SEEK_END)
        return bytes.decode(stream.read(offset))

if __name__ == "__main__":
    print_header = len(sys.argv) > 2
    files = sys.argv[1:]
    line_count = 10

    if "-n" in sys.argv:
        arg_index = sys.argv.index("-n")
        line_count = int(sys.argv[arg_index + 1])
        files = [f for i,f in enumerate(sys.argv) if i not in [0, arg_index, arg_index + 1]]

    for file in files:
        if print_header:
            print("\n==> {} <==".format(file))
        print(last_lines(file, line_count))