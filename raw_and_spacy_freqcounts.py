from collections import Counter
import os
import spacy

verbose = False

if verbose : print("Executing raw_and_spacy_freqcounts.py")

if verbose : print("Loading corpus…")
languages = ["Arabic","English","French","Finnish","German"]
corpus = dict()
for language in languages:
    with open(os.path.join(os.curdir,"treated_corpus",f"{language}.txt"),"r",encoding="utf-8") as f:
        corpus[language] = f.read().splitlines()
if verbose : print("Finished loading corpus")

for language,langcode in {"Arabic":"","English":"en","Finnish":"fi","French":"fr","German":"de"}.items():
    if verbose : print(f"Whitespace‐tokenizing raw text and computing frequency ranks for {language}")
    raw_text = " ".join(corpus[language])
    raw_freqs = Counter(raw_text.split(" "))
    raw_whitespace_tokenized_freqranks = sorted( [(w,c) for w,c in raw_freqs.items()], key = lambda pair:pair[1], reverse=True )
    with open(os.path.join(os.curdir,"freqranks",f"{language}_whitespace_raw"),"w",encoding="utf-8") as f:
        for (w,c) in raw_whitespace_tokenized_freqranks:
            f.write(w+" "+str(c)+"\n")
    
    if True: 
        if verbose : print(f"Tokenizing with Spacy and computing frequency ranks for {language}")
        if language == "Arabic":
            nlp = spacy.blank("ar")
        else:
            nlp = spacy.load(f"{langcode}_core_{"web" if langcode=="en" else "news"}_sm", disable=["parser", "ner"])
        spacy_freqs = Counter([t.lower_ for t in nlp(raw_text) if not (t.is_punct or t.is_space)])
        spacy_freqranks = sorted( [(w,c) for w,c in spacy_freqs.items()], key = lambda pair:pair[1], reverse=True )
        with open(os.path.join(os.curdir,"freqranks",f"{language}_spacy"), "w", encoding="utf-8") as f:
            for (w,c) in raw_whitespace_tokenized_freqranks:
                f.write(w+" "+str(c)+"\n")
    
    if verbose : print(f"Whitespace‐tokenizing lowercased text and computing frequency ranks for {language}\n")
    lowercase_freqs = Counter(" ".join(corpus[language]).lower().split(" "))
    lowercased_whitespace_tokenized_freqranks = sorted( [(w,c) for w,c in lowercase_freqs.items()], key = lambda pair:pair[1], reverse=True )
    with open(os.path.join(os.curdir,"freqranks",f"{language}_whitespace_lowercased"),"w",encoding="utf-8") as f:
        for (w,c) in lowercased_whitespace_tokenized_freqranks:
            f.write(w+" "+str(c)+"\n")




#TODO: add prints (and comments if needed)