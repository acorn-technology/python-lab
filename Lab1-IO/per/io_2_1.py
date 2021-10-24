import sys

if __name__ == '__main__':
    n_lines = 10
    file_name = sys.argv[1]

    buffer = []
    with open(file_name) as fp:
        while True:
            line = fp.readline()
            buffer.append(line)

            if len(buffer) > n_lines:
                buffer.pop(0)

            if not line:
                break

    for line in buffer:
        print(line, end='')
    print()
