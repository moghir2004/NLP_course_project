import xml.etree.ElementTree as ET
import os


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

languages = ["French", "English", "Arabic", "Finnish", "German"]


original_files = {language : os.path.join(os.curdir,"bibles",f"{language}.xml") for language in languages}

corpuses = {language: extract_new_testament(path) for language, path in original_files.items()}
shared_ids = set.intersection(*(set(corpus) for corpus in corpuses.values())) #explication?
filtered_corpus = {
    language: {verse_id: corpus[verse_id] for verse_id in sorted(shared_ids)}
    for language, corpus in corpuses.items()
}

for language in languages:
    with open( os.path.join(os.curdir,"treated_corpus",f"{language}.txt") ) as f:
    










