import xml.etree.ElementTree as ET

from datasets import Dataset

# les IDs pour le nouveau testament
NOUVEAU_TESTAMENT = {
    "b.MAT",
    "b.MAR",
    "b.LUK",
    "b.JOH",
    "b.ACT",
    "b.ROM",
    "b.1CO",
    "b.2CO",
    "b.GAL",
    "b.EPH",
    "b.PHI",
    "b.COL",
    "b.1TH",
    "b.2TH",
    "b.1TI",
    "b.2TI",
    "b.TIT",
    "b.PHM",
    "b.HEB",
    "b.JAM",
    "b.1PE",
    "b.2PE",
    "b.1JO",
    "b.2JO",
    "b.3JO",
    "b.JUD",
    "b.REV",
}


def extract_new_testament(path):
    root = ET.parse(path).getroot()
    verses = {}

    for book in root.iter("div"):
        if book.get("type") != "book":
            continue

        if book.get("id") not in NOUVEAU_TESTAMENT:
            continue
        for verse in book.iter("seg"):
            if verse.get("type") != "verse":
                continue
            verse_id = verse.get("id")
            text = "".join(verse.itertext()).strip()
            if verse_id and text:
                verses[verse_id] = text
    return verses


files = {
    "french": "./bibles/French.xml",
    "english": "./bibles/English.xml",
    "arabic": "./bibles/Arabic.xml",
    "finnish": "./bibles/Finnish.xml",
    "german": "./bibles/German.xml",
}

corpuses = {language: extract_new_testament(path) for language, path in files.items()}
shared_ids = set.intersection(*(set(corpus) for corpus in corpuses.values()))
filtered_corpus = {
    language: {verse_id: corpus[verse_id] for verse_id in sorted(shared_ids)}
    for language, corpus in corpuses.items()
}

shared_ids = sorted(shared_ids)
dataset_dict = {
    "verse_id": shared_ids,
    "english": [filtered_corpus["english"][id] for id in shared_ids],
    "french": [filtered_corpus["french"][id] for id in shared_ids],
    "german": [filtered_corpus["german"][id] for id in shared_ids],
    "finnish": [filtered_corpus["german"][id] for id in shared_ids],
    "arabic": [filtered_corpus["arabic"][id] for id in shared_ids],
}
# on peut finalement n'importer que cela (voir le fichier BPE_tokenizer.py)
dataset = Dataset.from_dict(dataset_dict)
