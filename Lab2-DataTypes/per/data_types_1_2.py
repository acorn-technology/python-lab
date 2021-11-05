import re

if __name__ == '__main__':
    file_name = "../acorn-system-development.txt"

    words_count = {}
    with open(file_name) as fp:
        while True:
            line = fp.readline()

            if not line:
                break

            words = re.split('[^a-zA-Z]', line)
            for word in words:
                word_lowercase = word.lower()
                if word_lowercase not in words_count:
                    words_count[word_lowercase] = 0
                words_count[word_lowercase] = words_count[word_lowercase] + 1

    for key, value in words_count.items():
        if len(key) > 0:
            print("{}: {}".format(key, value))
