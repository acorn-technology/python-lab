from pathlib import Path
from collections import Counter
from itertools import chain
import re
import os


PATH1 = os.path.join(os.path.dirname(__file__), "../acorn-system-development.txt")
PATH2 = os.path.join(os.path.dirname(__file__), "../triangle-input.txt")

def p11(text):
    print(len(text))
    print(len(text.split()))

def p12(text):
    words = text.lower().split()
    print(Counter(words).most_common(10))

def p13(needle, haystack):
    words = haystack.lower().split()
    print("\n".join((word for word in words if needle in word)))

def p14(needle, haystack, regex=False):
    words = haystack.lower().split()
    if regex:
        condition = lambda word: re.findall(needle, word)
    else:
        condition = lambda word: needle in word
    print("\n".join((word for word in words if condition(word))))

def check_triangle(t):
    return t[0] + t[1] > t[2] and t[1] + t[2] > t[0] and t[0] + t[2] > t[1]

def p21(text):
    lines = text.splitlines()
    print(sum(check_triangle(tuple(map(int, line.split()))) for line in lines))

def p22(text):
    lines = text.splitlines()
    rows = [(map(int, line.split())) for line in lines]
    one_column = list(chain.from_iterable(map(list, zip(*rows))))
    print(sum(check_triangle(three) for three in [one_column[i*3:i*3+3] for i in range(len(lines))]))

def main():
    text_1 = Path(PATH1).read_text()
    p11(text_1)
    p12(text_1)
    p13("res", text_1)
    p14("res$", text_1, regex=True)

    text2 = Path(PATH2).read_text()
    p21(text2)
    p22(text2)


if __name__ == "__main__":
    main()
