if __name__ == '__main__':
    file_name = "../acorn-system-development.txt"

    n_characters = 0
    n_words = 0
    with open(file_name) as fp:
        while True:
            line = fp.readline()
            n_characters += sum(c.isascii() for c in line)
            n_words += len(line.split())

            if not line:
                break

    print("Number of characters: ", n_characters)
    print("Number of words: ", n_words)
