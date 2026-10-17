from collections import Counter
import os

languages = ["Arabic","English","French","Finnish","German"]
corpus = dict()
for language in languages:
    with open(os.path.join(os.curdir,"treated_corpus",f"{language}.txt"),"r",encoding="utf-8") as f:
        corpus[language] = f.read().splitlines()


for language in languages:
    raw_freqs = Counter(" ".join(corpus[language]).split(" "))
    raw_whitespace_tokenized_freqranks = sorted( [(w,c) for w,c in raw_freqs.items()], key = lambda pair:pair[1], reverse=True )
    with open(os.path.join(os.curdir,"freqranks",f"{language}_whitespace_raw"),"w",encoding="utf-8") as f:
        for (w,c) in raw_whitespace_tokenized_freqranks:
            f.write(w+" "+str(c)+"\n")
        
    lowercase_freqs = Counter(" ".join(corpus[language]).lower().split(" "))
    lowercased_whitespace_tokenized_freqranks = sorted( [(w,c) for w,c in lowercase_freqs.items()], key = lambda pair:pair[1], reverse=True )
    with open(os.path.join(os.curdir,"freqranks",f"{language}_whitespace_lowercased"),"w",encoding="utf-8") as f:
        for (w,c) in lowercased_whitespace_tokenized_freqranks:
            f.write(w+" "+str(c)+"\n")

