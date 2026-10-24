from pathlib import Path

import matplotlib.pyplot as plt

FREQ_DIR = Path("freqranks")
Path("./figures").mkdir(parents=True, exist_ok=True)

languages = ["Arabic","English","Finnish","French","German"]
tokenizers = ["_bpe_2k","_bpe_8k","_bpe_32k","_spacy","_whitespace_lowercased","_whitespace_raw","_xmlr"]

def load_freqranks(path):
    freqranks = []

    with open(path, encoding="utf-8") as file:
        for line in file:
            token, frequency = line.rsplit(maxsplit=1)
            freqranks.append((token, int(frequency)))

    return freqranks


def plot_freqranks(freqranks_dict, title, output_path):
    plt.figure(figsize=(10, 6))
<<<<<<< HEAD
    plt.loglog(ranks, frequencies, label=label, marker=".", linestyle = "None", markersize=2)
=======
    for label, freqranks in freqranks_dict.items():
        ranks = range(1, len(freqranks) + 1)
        frequencies = [frequency for _, frequency in freqranks]
        plt.loglog(ranks, frequencies, label=label)

>>>>>>> 1985180d5ca5c7139d8196fd00e1f236c599cff1
    plt.xlabel("Frequency rank")
    plt.ylabel("Token Frequency")
    plt.title(title)
    plt.legend()
    plt.savefig(output_path, dpi=300)
    plt.close()


<<<<<<< HEAD
for file in FREQ_DIR.iterdir():
    freqranks = load_freqranks(file)
    plot_freqranks(freqranks, label=file.stem, output_path=f"./figures/{file.stem}.png")

def plot_freqranks_perlang(language):
    
=======
languages = ["English", "French", "German", "Finnish", "Arabic"]
for language in languages:

    files = [
        f"{language}_whitespace_raw.txt",
        f"{language}_whitespace_lowercased.txt",
        f"{language}_xlmr.txt",
        f"{language}_bpe_2k.txt",
        f"{language}_bpe_8k.txt",
        f"{language}_bpe_32k.txt",
    ]

    freqranks_dict = {
        file.removesuffix(".txt").replace(f"{language}_", ""): load_freqranks(
            FREQ_DIR / file
        )
        for file in files
    }
    plot_freqranks(
        freqranks_dict,
        title=f"{language}: tokenizer comparison",
        output_path=f"./figures/{language}_comparison.png",
    )
>>>>>>> 1985180d5ca5c7139d8196fd00e1f236c599cff1
