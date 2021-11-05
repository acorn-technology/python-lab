#!/usr/bin/env python

import sys

def basic_stats(text):
    """
    ## 1.1 Basic stats

    Read the input file and write the number if characters and number of words.

    Example output:
    ```
    Number of characters: 1868
    Number of words: 290
    ```
    """
    print("Number of characters: {}".format(len(text)))

    word_count = 0
    new_word = False
    for c in text:
        # Ignore some characters
        if c in ['.', ',', '-', "'", '’', '"', '‘']:
            pass
        # Increase number of words when we see a new word
        elif c.isalnum() and not new_word:
            new_word = True
            word_count = word_count + 1
        # Otherwise note that we no longer is in a new word
        elif not c.isalnum():
            new_word = False
    print("Number of words: {}".format(word_count))


def word_counter(text):
    """
    ## 1.2 Word count

    Count the number of occurences for each word in the file and print them sorted by the number of occurences.

    Example output:
    ```
    and: 17
    of: 15
    to: 11
    the: 9
    we: 8
    ...
    ```
    """
    new_word = False
    current_word = ''
    word_dict = dict()
    for c in text:
        # Ignore some characters
        if c in ['.', ',', '-', "'", '’', '"', '‘']:
            pass
        else:
            if c.isalnum():
                current_word = current_word + c
            # Increase number of words when we see a new word
            if c.isalnum() and not new_word:
                new_word = True
            # Otherwise note that we no longer is in a new word
            elif not c.isalnum():
                if len(current_word) > 0:
                    if current_word in word_dict:
                        word_dict[current_word] = word_dict[current_word] + 1
                    else:
                        word_dict[current_word] = 1

                new_word = False
                current_word = ''

    word_list_sorted = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

    for word, num in word_list_sorted:
        print('{}: {}'.format(word, num))

def word_search(text, word):
    """
    ## 1.3 Search

    Take a string as input and print all the words that are containing that string.

    _Note:_ Try solving it with [list comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) (e.g `[x.lower() for x in data]`)

    Example output for "res":
    ```
    architectures
    irrespective
    present
    representing
    ```
    """
    new_word = False
    current_word = ''
    word_list = []
    for c in text:
        # Ignore some characters
        if c in ['.', ',', '-', "'", '’', '"', '‘']:
            pass
        else:
            if c.isalnum():
                current_word = current_word + c
            # Increase number of words when we see a new word
            if c.isalnum() and not new_word:
                new_word = True
            # Otherwise note that we no longer is in a new word
            elif not c.isalnum():
                if len(current_word) > 0:
                    if not current_word in word_list:
                        word_list.append(current_word)

                new_word = False
                current_word = ''

    word_list.sort()

    matches = [w for w in word_list if word in w ]

    for w in matches:
        print('{}'.format(w))


"""## 1.4 Regular Expressions

Expand the word search to support regular expressions as input
"""
# TODO: RegExp-search

if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename) as file:
        text = file.read()
        basic_stats(text)
        word_counter(text)
        word_search(text, 'res')
