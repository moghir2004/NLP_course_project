from collections import Counter
from pathlib import Path

from tokenizers import Tokenizer

CORPUS_DIR = Path("treated_corpus")
TOKENIZER_DIR = Path("tokenizers")
FREQ_DIR = Path("freqranks")
FREQ_DIR.mkdir(parents=True, exist_ok=True)


def read_corpus(language):
    with (CORPUS_DIR / f"{language}.txt").open(encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


languages = ["Arabic", "English", "French", "Finnish", "German"]
vocab_sizes = [2000, 8000, 32000]


def get_bpe_freqs(tokenizer, verses):
    frequencies = Counter()

    for verse in verses:
        frequencies.update(tokenizer.encode(verse).tokens)
    return frequencies


for language in languages:
    corpus = read_corpus(language)

    for vocab_size in vocab_sizes:
        tokenizer_path = (
            TOKENIZER_DIR / f"{language.lower()}_{vocab_size // 1000}k.json"
        )

        tokenizer = Tokenizer.from_file(str(tokenizer_path))
        frequencies = get_bpe_freqs(tokenizer, corpus)

        ranked_frequencies = sorted(
            frequencies.items(),
            key=lambda pair: pair[1],
            reverse=True,
        )

        output_path = FREQ_DIR / f"{language}_bpe_{vocab_size // 1000}k.txt"

        with output_path.open("w", encoding="utf-8") as f:
            for token, count in ranked_frequencies:
                f.write(f"{token} {count}\n")
