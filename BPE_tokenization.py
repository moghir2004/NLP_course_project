from datasets import Dataset
from tokenizers import Tokenizer
from tokenizers.models import BPE

from traitement_corpus import filtered_corpus, shared_ids

shared_ids = sorted(shared_ids)
dataset_dict = {
    "verse_id": shared_ids,
    "english": [filtered_corpus["english"][id] for id in shared_ids],
    "french": [filtered_corpus["french"][id] for id in shared_ids],
    "german": [filtered_corpus["german"][id] for id in shared_ids],
    "finnish": [filtered_corpus["german"][id] for id in shared_ids],
    "arabic": [filtered_corpus["arabic"][id] for id in shared_ids],
}

dataset = Dataset.from_dict(dataset_dict)
french_tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
print(dataset[2])
