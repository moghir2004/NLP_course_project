import random
from collections import Counter


def train(text, alphabet):
    # take only valid letters in alphabet and ignore unicode artifacts
    counts = Counter(char for char in text.lower() if char in alphabet)
    return counts


def sample(counts, max_len):
    characters = list(counts.keys())
    frequencies = list(counts.values())
    # weighted random string from alphabet
    return "".join(random.choices(characters, weights=frequencies, k=max_len))


# French part
with open("./treated_corpus/French.txt", encoding="utf-8") as f:
    french_text = f.read()

french_alphabet = list("abcdefghijklmnopqrstuvwxyzàâæçéèêëîïôœùûüÿ ")
model = train(french_text, french_alphabet)
generated_text = sample(model, len(french_text))

with open("./treated_corpus/French_random.txt", "w", encoding="utf-8") as gen_f:
    gen_f.write(generated_text)

# Arabic part
with open("./treated_corpus/Arabic.txt", encoding="utf-8") as a:  # a as in arabic
    arabic_text = a.read()

arabic_alphabet = list(" ابتثجحخدذرزسشصضطظعغفقكلمنهويءآأإؤئىة")
model = train(arabic_text, arabic_alphabet)
generated_text = sample(model, len(arabic_text))

with open("./treated_corpus/Arabic_random.txt", "w", encoding="utf-8") as gen_a:
    gen_a.write(generated_text)

# English part
with open("./treated_corpus/English.txt", encoding="utf-8") as e:
    english_text = e.read()

english_alphabet = list("abcdefghijklmnopqrstuvwxyz ")
model = train(english_text, english_alphabet)
generated_text = sample(model, len(english_text))

with open("./treated_corpus/English_random.txt", "w", encoding="utf-8") as gen_e:
    gen_e.write(generated_text)

# German part
with open("./treated_corpus/German.txt", encoding="utf-8") as g:
    german_text = g.read()

german_alphabet = list("abcdefghijklmnopqrstuvwxyzäöüß ")
model = train(german_text, german_alphabet)
generated_text = sample(model, len(german_text))

with open("./treated_corpus/German_random.txt", "w", encoding="utf-8") as gen_g:
    gen_g.write(generated_text)

# Finnish part
with open("./treated_corpus/Finnish.txt", encoding="utf-8") as fi:
    finnish_text = fi.read()

finnish_alphabet = list("abcdefghijklmnopqrstuvwxyzåäöü ")
model = train(finnish_text, finnish_alphabet)
generated_text = sample(model, len(finnish_text))

with open("./treated_corpus/Finnish_random.txt", "w", encoding="utf-8") as gen_fi:
    gen_fi.write(generated_text)
