import matplotlib.pyplot as plt
import seaborn as sns

def plot_support_vs_lift(rules):
    """
    Scatter plot: Support vs Lift colored by Itemset Size
    """
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(
        rules['support'],
        rules['lift'],
        c=rules['itemset_size'],
        cmap='viridis',
        alpha=0.5,
        s=60
    )
    cbar = plt.colorbar(scatter, label='Itemset Size')
    cbar.set_ticks(range(2, rules['itemset_size'].max() + 1))

    plt.title("Support vs Lift by Itemset Size")
    plt.xlabel("Support")
    plt.ylabel("Lift")
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_avg_confidence_by_itemset_size(rules):
    """
    Line plot: Average confidence by itemset size
    """
    avg_conf = rules.groupby('itemset_size')['confidence'].mean().reset_index()

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=avg_conf, x='itemset_size', y='confidence', marker='o', linewidth=2, color='teal')
    plt.title("Average Confidence by Itemset Size")
    plt.xlabel("Itemset Size")
    plt.ylabel("Average Confidence")
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.tight_layout()
    plt.show()
