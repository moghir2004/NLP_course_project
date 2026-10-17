from collections import Counter
from pathlib import Path

from transformers import AutoTokenizer

xlmr = AutoTokenizer.from_pretrained("FacebookAI/xlm-roberta-base")
languages = ["English", "French", "German", "Finnish", "Arabic"]
TOKENIZER_DIR = Path("tokenizers")
CORPUS_DIR = Path("treated_corpus")
FREQ_DIR = Path("freqranks")


def read_corpus(language):
    with (CORPUS_DIR / f"{language}.txt").open(encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


for language in languages:
    verses = read_corpus(language)

    frequencies = Counter()

    for verse in verses:
        frequencies.update(xlmr.tokenize(verse))

    ranked_frequencies = sorted(
        frequencies.items(), key=lambda pair: pair[1], reverse=True
    )
    output_path = FREQ_DIR / f"{language}_xlmr.txt"

    with output_path.open("w", encoding="utf-8") as f:
        for token, count in ranked_frequencies:
            f.write(f"{token} {count}\n")
