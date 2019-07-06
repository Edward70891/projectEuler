#!/bin/env python3
from collections import Counter

# Problem at:
# https://projecteuler.net/problem=42


def word_value(word):
    return sum([ord(char) - 64 for char in word])


with open("42_words.txt", "rt") as words_file:
    words = {
        word: False
        for word in words_file.read().replace('"', "").split(',')
    }

max_val = max([len(word) for word in words.keys()]) * 26
triangle_nums = {int(0.5 * i * (i + 1)) for i in range(1, max_val + 1)}

for word in words.keys():
    if word_value(word) in triangle_nums:
        words[word] = True

print(Counter(words.values())[True])
