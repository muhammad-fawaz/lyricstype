import string
import random

with open("lyrics.txt", "r") as f:
    lyrics = f.read()

# print(lyrics)
words = lyrics.split()
chain = {}

for i in range(len(words) - 1):

    current_word = words[i].strip(string.punctuation).lower()
    next_word = words[i+1].strip(string.punctuation).lower()

    if current_word not in chain:
        chain[current_word] = []

    chain[current_word].append(next_word)


# for key, val in chain.items():
    # print(key, val)


word = random.choice(list(chain.keys()))
# out_str = 
# print(word)
for i in range(20):
    pass