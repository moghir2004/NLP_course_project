import random
from collections import Counter, defaultdict
from itertools import pairwise


def train_bigrams(text):
    bigrams = defaultdict(Counter)
    initial_words = []

    for verse in text:
        words = verse.lower().split()
        if words:
            initial_words.append(words[0])
            for current_word, next_word in pairwise(words):
                bigrams[current_word][next_word] += 1
    return bigrams, initial_words


def sample_bigrams(text, bigrams, initial_words):
    generated_verses = []

    for verse in text:
        original_words = verse.lower().split()

        if not original_words:
            generated_verses.append("")
            continue

        current_word = random.choice(initial_words)
        generated_words = [current_word]

        for _ in range(len(original_words) - 1):
            possible_next_words = bigrams.get(current_word)

            if not possible_next_words:
                current_word = random.choice(initial_words)
            else:
                words = list(possible_next_words.keys())
                frequencies = list(possible_next_words.values())
                current_word = random.choices(words, weights=frequencies, k=1)[0]

            generated_words.append(current_word)

        generated_verses.append(" ".join(generated_words))

    return generated_verses


# French
with open("./treated_corpus/French.txt", encoding="utf-8") as f:
    verses = f.readlines()

random.seed(42)

bigrams, initial_words = train_bigrams(verses)

generated_verses = sample_bigrams(verses, bigrams, initial_words)

with open("./treated_corpus/French_word_bigrams.txt", "w", encoding="utf-8") as f:
    f.writelines(verse + "\n" for verse in generated_verses)

# Arabic
with open("./treated_corpus/Arabic.txt", encoding="utf-8") as a:
    verses = a.readlines()

random.seed(42)

bigrams, initial_words = train_bigrams(verses)

generated_verses = sample_bigrams(verses, bigrams, initial_words)

with open("./treated_corpus/Arabic_word_bigrams.txt", "w", encoding="utf-8") as f:
    f.writelines(verse + "\n" for verse in generated_verses)

# English
with open("./treated_corpus/English.txt", encoding="utf-8") as f:
    verses = f.readlines()

random.seed(42)

bigrams, initial_words = train_bigrams(verses)

generated_verses = sample_bigrams(verses, bigrams, initial_words)

with open("./treated_corpus/English_word_bigrams.txt", "w", encoding="utf-8") as f:
    f.writelines(verse + "\n" for verse in generated_verses)

# German
with open("./treated_corpus/German.txt", encoding="utf-8") as f:
    verses = f.readlines()

random.seed(42)

bigrams, initial_words = train_bigrams(verses)

generated_verses = sample_bigrams(verses, bigrams, initial_words)

with open("./treated_corpus/German_word_bigrams.txt", "w", encoding="utf-8") as f:
    f.writelines(verse + "\n" for verse in generated_verses)

# Finnish
with open("./treated_corpus/Finnish.txt", encoding="utf-8") as f:
    verses = f.readlines()

random.seed(42)

bigrams, initial_words = train_bigrams(verses)

generated_verses = sample_bigrams(verses, bigrams, initial_words)

with open("./treated_corpus/Finnish_word_bigrams.txt", "w", encoding="utf-8") as f:
    f.writelines(verse + "\n" for verse in generated_verses)


print("\n".join(generated_verses[:5]))
