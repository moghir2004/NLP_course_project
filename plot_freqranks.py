from pathlib import Path
import powerlaw
import matplotlib.pyplot as plt
import numpy as np
import time
import scipy

FREQ_DIR = Path("freqranks")
Path("./figures").mkdir(parents=True, exist_ok=True)


def load_freqranks(path):
    freqranks = []

    with open(path, encoding="utf-8") as file:
        for line in file:
            token, frequency = line.rsplit(maxsplit=1)
            freqranks.append(int(frequency))

    return freqranks

def plot_freqranks(freqranks_dict, title, output_path):
    plt.figure(figsize=(10, 6))
    for label, freqranks in freqranks_dict.items():
        ranks = np.arange(1, len(freqranks) + 1)
        plt.loglog(ranks, freqranks, linestyle="none", marker="+", markersize=5, label=label)

    plt.xlabel("Frequency rank")
    plt.ylabel("Token Frequency")
    plt.title(title)
    plt.legend()
    plt.grid(which="both")
    plt.minorticks_on()
    plt.savefig(output_path, dpi=300)
    plt.close()


def compute_alpha_least_square(freqranks):
    ranks = np.arange(1, len(freqranks) + 1)
    return -np.polyfit(np.log(ranks), np.log(freqranks),1)[0]

def compute_alpha_powerlaw(freqranks):
    gamma =  powerlaw.Fit(freqranks, discrete=True).alpha
    return 1/(gamma-1)

def fit_plot_alpha_nobootstrap(freqranks_dict, title, output_path, color_code, alpha_compute_method):
    alphas = dict()
    plt.figure(figsize=(10, 6))
    for label, freqranks in freqranks_dict.items():
        ranks = np.arange(1, len(freqranks) + 1)
        plt.loglog(ranks, freqranks, linestyle="none", marker="+", markersize=5, label=label+" raw data", color=color_code[label])
    
        alpha = alpha_compute_method(freqranks)
        alphas[label] = alpha
        fitted_freqs = freqranks[0]/(ranks**alpha)
        plt.loglog(ranks,fitted_freqs, label=label+" fitted", color=color_code[label])
    
    plt.xlabel("Frequency rank")
    plt.ylabel("Token Frequency")
    plt.title(title)
    plt.legend()
    plt.grid(which="both")
    plt.minorticks_on()
    plt.savefig(output_path, dpi=300)
    plt.close()
    
    return alphas
        
def fit_plot_alpha_with_bootstrap(freqranks_dict, title, output_path, color_code, alpha_compute_method):
    alphas = dict()
    eps_alphas = dict()
    plt.figure(figsize=(10, 6))
    for label, freqranks in freqranks_dict.items():
        ranks = np.arange(1, len(freqranks) + 1)
        plt.loglog(ranks, freqranks, linestyle="none", marker="+", markersize=5, label=label+" raw data", color=color_code[label])
        
        low,high = scipy.stats.bootstrap((freqranks,), alpha_compute_method, n_resamples=100).confidence_interval
        alpha = 0.5*(high + low)
        print(f"Finished bootstrapping for {language}, {label}")
        eps_alpha = 0.5*(high - low) #incertitude
        alphas[label] = alpha
        eps_alphas[label] = eps_alpha
        fitted_freqs = freqranks[0]/(ranks**alpha)
        plt.loglog(ranks,fitted_freqs, label=label+" fitted", color=color_code[label])
    
    plt.xlabel("Frequency rank")
    plt.ylabel("Token Frequency")
    plt.title(title)
    plt.legend()
    plt.grid(which="both")
    plt.minorticks_on()
    plt.savefig(output_path, dpi=300)
    plt.close()
    return alphas,eps_alphas

    


languages = ["English", "French", "German", "Finnish", "Arabic"]
color_code = {"whitespace_raw":"blue","whitespace_lowercased":"orange","xlmr":"green","bpe_2k":"red","bpe_8k":"purple","bpe_32k":"brown"}
#NB : si on rajoute des nouveaux "tokenizers" (genre random ou bigram), il faut absolument update color_code, sinon le programme va planter!!!
alphas_ls_noBS = dict() #least‐square
alphas_pl_noBS = dict() #powerlaw

alphas_ls_wBS = dict()
eps_alphas_ls = dict() #incertitude, i.e. taille de l'intervalle de confiance à 95% divisée par deux
alphas_pl_wBS = dict()
eps_alphas_pl = dict()

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
    
    alphas_ls_noBS[language] =  fit_plot_alpha_nobootstrap(freqranks_dict, 
                             title=fr"{language} : Zipf law with $\alpha$ fitted via least‐square log_linear regression (no bootstrapping)", 
                             output_path=f"./figures/{language}_alpha_least_square_no_bootstrap.png",
                             color_code=color_code, alpha_compute_method=compute_alpha_least_square)

    alphas_pl_noBS[language] = fit_plot_alpha_nobootstrap(freqranks_dict, 
                             title=fr"{language} : Zipf law with $\alpha$ fitted via powerlaw (no bootstrapping)", 
                             output_path=f"./figures/{language}_alpha_powerlaw_no_bootstrap.png",
                             color_code=color_code, alpha_compute_method=compute_alpha_powerlaw)
    
    alphas_ls_wBS[language], eps_alphas_ls[language] = fit_plot_alpha_with_bootstrap(freqranks_dict, 
                             title=fr"{language} : Zipf law with $\alpha$ fitted via least‐square log_linear regression (with bootsrapping)", 
                             output_path=f"./figures/{language}_alpha_least_square_with_bootstrapping.png",
                             color_code=color_code, alpha_compute_method=compute_alpha_least_square)
    

print(f"{alphas_ls_noBS = }")
print(f"{alphas_pl_noBS = }")



