import matplotlib.pyplot as plt
from baird import TD_target 

def main():
    # List of checkpoint values to test
    checkpoint_values = [1, 2, 3, 5, 10, 100]

    # Grid configuration for subplots
    fig, axs = plt.subplots(2, 3, figsize=(15, 8))
    axs = axs.flatten()
    
    # Experiment execution and plotting for each checkpoint value
    for i, cp in enumerate(checkpoint_values):
        print("Ejecutando TD_target con checkpoint =", cp)
        parameters, values = TD_target(eta=0.999, checkpoint=cp)
        axs[i].plot(range(len(values)), values, label=f"cp = {cp}")
        axs[i].set_title(f"Checkpoint = {cp}")
        axs[i].set_xlabel("Training Steps")
        axs[i].set_ylabel("MAX-VE")
        axs[i].set_xscale("log")
        axs[i].set_yscale("symlog")
        axs[i].set_ylim(-0.4,10000)
        axs[i].legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
