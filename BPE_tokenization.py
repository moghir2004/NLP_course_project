from tokenizers.implementations.sentencepiece_bpe import SentencePieceBPETokenizer

from traitement_corpus import dataset

# Constante pour changer une fois pour tout les tokenizers
VOCAB_SIZE = 32000

# initialiser différents tokenizers pour différentes langues
arabic_tokenizer = SentencePieceBPETokenizer()
english_tokenizer = SentencePieceBPETokenizer()
finnish_tokenizer = SentencePieceBPETokenizer()
french_tokenizer = SentencePieceBPETokenizer()
german_tokenizer = SentencePieceBPETokenizer()


# pour avoir chaque verset dans chaque langue
def verse_iterator(dataset, language):
    yield from dataset[language]


# entraînement des différents tokenizers de chaque langue
arabic_tokenizer.train_from_iterator(
    verse_iterator(dataset, "Arabic"),
    vocab_size=VOCAB_SIZE,
    special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"],
)
english_tokenizer.train_from_iterator(
    verse_iterator(dataset, "English"),
    vocab_size=VOCAB_SIZE,
    special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"],
)
finnish_tokenizer.train_from_iterator(
    verse_iterator(dataset, "Finnish"),
    vocab_size=VOCAB_SIZE,
    special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"],
)
french_tokenizer.train_from_iterator(
    verse_iterator(dataset, "French"),
    vocab_size=VOCAB_SIZE,
    special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"],
)
german_tokenizer.train_from_iterator(
    verse_iterator(dataset, "German"),
    vocab_size=VOCAB_SIZE,
    special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"],
)
# enregistrement des résultats pour ne pas le relancer à chaque fois
arabic_tokenizer.save_model("tokenizers", "arabic_32k")
english_tokenizer.save_model("tokenizers", "english_32k")
finnish_tokenizer.save_model("tokenizers", "finnish_32k")
french_tokenizer.save_model("tokenizers", "french_32k")
german_tokenizer.save_model("tokenizers", "german_32k")

french_tokenizer.save("tokenizers/french_32k.json")
german_tokenizer.save("tokenizers/german_32k.json")
english_tokenizer.save("tokenizers/english_32k.json")
finnish_tokenizer.save("tokenizers/finnish_32k.json")
arabic_tokenizer.save("tokenizers/arabic_32k.json")
