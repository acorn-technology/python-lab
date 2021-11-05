import os
import sys
import re


def print_basic_stats(text):
    print(f'Number of characters: {len(text)}')
    print(f'Number of words: {len(text.split())}')

def print_occurence_count(text):
    count = dict()
    for word in [w.lower().strip(',.!"') for w in text.split()]:
        count[word] = count.setdefault(word, 0) + 1

    for c in sorted(count.keys(), key = lambda key: -count[key]):
        print(f'{c}: {count[c]}')

def print_matching(text, input, regex = False):
    if regex:
        matches = set([x.strip(',.!"') for x in text.split() if re.match(input, x.lower())])
    else:
        matches = set([x.strip(',.!"') for x in text.split() if input in x])

    for match in sorted(matches):
        print(match)

INPUT_FILE = os.path.join(os.path.dirname(__file__), '../acorn-system-development.txt')

print(INPUT_FILE)

if __name__ == '__main__':
    with open(INPUT_FILE, 'r', encoding='utf8') as file:
        text = file.read()

        if ('-b' in sys.argv):
            print_basic_stats(text)
        if ('-u' in sys.argv):
            print_occurence_count(text)
        if ('-s' in sys.argv):
            print_matching(text, sys.argv[sys.argv.index('-s') + 1])
        if ('-r' in sys.argv):
            print_matching(text, sys.argv[sys.argv.index('-r') + 1], regex=True)