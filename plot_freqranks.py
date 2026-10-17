from pathlib import Path

import matplotlib.pyplot as plt

FREQ_DIR = Path("freqranks")


def plot_freqranks(freqranks, label, output_path):
    ranks = range(1, len(freqranks) + 1)
    frequencies = [frequency for _, frequency in freqranks]

    plt.figure(figsize=(10, 6))
    plt.loglog(ranks, frequencies, label)
    plt.xlabel("Frequency rank")
    plt.ylabel("Token Frequency")
    plt.title(f"Zipf distribution - {label}")
    plt.legend()
    plt.grid(True, which="both")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
