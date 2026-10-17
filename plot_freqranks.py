from pathlib import Path

import matplotlib.pyplot as plt

FREQ_DIR = Path("freqranks")
Path("./figures").mkdir(parents=True, exist_ok=True)


def load_freqranks(path):
    freqranks = []

    with open(path, encoding="utf-8") as file:
        for line in file:
            token, frequency = line.rsplit(maxsplit=1)
            freqranks.append((token, int(frequency)))

    return freqranks


def plot_freqranks(freqranks, label, output_path):
    ranks = range(1, len(freqranks) + 1)
    frequencies = [frequency for _, frequency in freqranks]

    plt.figure(figsize=(10, 6))
    plt.loglog(ranks, frequencies, label=label)
    plt.xlabel("Frequency rank")
    plt.ylabel("Token Frequency")
    plt.title(f"Zipf distribution - {label}")
    plt.legend()
    plt.grid(True, which="both")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


for file in FREQ_DIR.iterdir():
    freqranks = load_freqranks(file)
    plot_freqranks(freqranks, label=file.stem, output_path=f"./figures/{file.stem}.png")
