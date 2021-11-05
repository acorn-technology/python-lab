from io import open

from builtins import print, len

with open('../acorn-system-development.txt') as file:
    content = file.read()
    print(f"Number of characters: {len(content)}")
    print(f"Number of words: {len(content.split())}")
