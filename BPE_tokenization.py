from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.trainers import BpeTrainer

from traitement_corpus import dataset

french_tokenizer_2k = Tokenizer(BPE(unk_token="[UNK]"))
trainer = BpeTrainer(
    vocab_size=2000, special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"]
)
french_tokenizer_2k.pre_tokenizer = Whitespace()


def french_verse_iterator(dataset):
    yield from dataset["french"]


french_tokenizer_2k.train_from_iterator(french_verse_iterator(dataset), trainer)
print(french_tokenizer_2k.get_vocab_size())
