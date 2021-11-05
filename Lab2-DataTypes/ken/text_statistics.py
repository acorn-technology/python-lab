import re

with open("../acorn-system-development.txt", "r") as file:
    content = file.read()
    file.close()
    print(f"Number of characters: {len(content)}")

    words = content.split()
    print(f"Number of words: {len(words)}")

    sorted_words = sorted(words)
    sorted_words_lower_case = list((map(lambda x: x.lower(), sorted_words)))
    pattern = r'[^\w]'
    sorted_words_lower_case_only_letters = list((map(lambda x: re.sub(pattern, "", x), sorted_words_lower_case)))

    word_frequency = []
    for word in sorted_words_lower_case_only_letters:
        word_frequency.append(sorted_words_lower_case_only_letters.count(word))

    word_count = dict(list(zip(sorted_words_lower_case_only_letters, word_frequency)))
    print("Word occurrence count:")
    for key, value in sorted(word_count.items()):
        print(f"* {key}: {value}")
