# run_analysis.py

import os
from src.preprocessing import load_dataset, inspect_data
from src.apriori_utils import (
    get_frequent_itemsets,
    get_association_rules,
    get_top_rules_by_lift_and_support
)
from src.visualizations import (
    plot_support_vs_lift,
    plot_avg_confidence_by_itemset_size
)

def main():
    # 1. Load the dataset
    data_path = os.path.join("data", "basket_analysis.csv")
    df = load_dataset(data_path)

    if df is None:
        print("❌ Dataset loading failed.")
        return

    print("✅ Dataset loaded successfully.\n")
    print(inspect_data(df))

    # 2. Generate frequent itemsets
    print("\n🔍 Generating frequent itemsets...")
    frequent_itemsets = get_frequent_itemsets(df, min_support=0.02)
    print(f"✅ Found {len(frequent_itemsets)} frequent itemsets.\n")

    # 3. Generate association rules
    print("🔗 Generating association rules...")
    rules = get_association_rules(frequent_itemsets, metric="lift", min_threshold=1.01)
    print(f"✅ Generated {len(rules)} rules.\n")

    # 4. Plot Support vs Lift
    print("📊 Visualizing Support vs Lift...")
    plot_support_vs_lift(rules)

    # 5. Plot Average Confidence by Itemset Size
    print("📈 Visualizing Average Confidence by Itemset Size...")
    plot_avg_confidence_by_itemset_size(rules)

    # 6. Show top rules
    print("🏆 Top rules per itemset size (highest lift and support):")
    top_rules = get_top_rules_by_lift_and_support(rules)
    print(top_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

if __name__ == "__main__":
    main()
