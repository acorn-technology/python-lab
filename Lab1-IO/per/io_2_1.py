import sys

if __name__ == '__main__':
    file_name = sys.argv[1]

    buffer = []
    n_lines = 10
    with open(file_name) as fp:
        while True:
            line = fp.readline()
            buffer.append(line)

            if len(buffer) > 10:
                buffer.pop(0)

            if not line:
                break

    for line in buffer:
        print(line, end='')
    print()
