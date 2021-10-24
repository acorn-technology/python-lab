import sys


def tail(file, lines):
    buffer = []
    with open(file) as fp:
        while True:
            line = fp.readline()
            buffer.append(line)

            if len(buffer) > lines:
                buffer.pop(0)

            if not line:
                break

    print("{}:".format(file))
    for line in buffer:
        print(line, end='')
    print("\n")


if __name__ == '__main__':
    n_lines = 10
    file_names = [sys.argv[i] for i in range(1, len(sys.argv))]

    for file_name in file_names:
        tail(file_name, n_lines)
