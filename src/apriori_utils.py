from mlxtend.frequent_patterns import apriori, association_rules

def get_frequent_itemsets(df, min_support=0.02):
    """
    Applies the Apriori algorithm to find frequent itemsets.
    """
    frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
    return frequent_itemsets

def get_association_rules(frequent_itemsets, metric="lift", min_threshold=1.01):
    """
    Generates association rules from frequent itemsets.
    """
    rules = association_rules(frequent_itemsets, metric=metric, min_threshold=min_threshold)
    rules['itemset_size'] = rules['antecedents'].apply(len) + rules['consequents'].apply(len)
    return rules

def get_top_rules_by_lift_and_support(rules):
    """
    For each itemset size, get the top rule based on lift and support.
    """
    sorted_rules = rules.sort_values(by=['itemset_size', 'lift', 'support'], ascending=[True, False, False])
    top_rules = sorted_rules.groupby('itemset_size').head(1).reset_index(drop=True)
    return top_rules
