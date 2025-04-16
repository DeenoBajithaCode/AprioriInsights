# 🛍️ Apriori Insights

Welcome to **Apriori Insights**, a data-driven project showcasing how **Association Rule Mining** and **Market Basket Analysis (MBA)** can be used to uncover hidden patterns in transactional data.

This project uses the **Apriori algorithm** to generate strong association rules and provide actionable retail and marketing insights from customer purchase behavior.

🔗 GitHub Repo: [DeenoBajithaCode/AprioriInsights](https://github.com/DeenoBajithaCode/AprioriInsights)

---

## 🚀 Project Highlights

- ✅ Discover product combinations frequently bought together
- 📊 Visualize itemset patterns with support, confidence, and lift
- 🧠 Gain business recommendations from rule clusters
- 🔍 Analyze itemsets of varying sizes and their significance
- 🐍 Powered by Python and the `mlxtend` library

---

## 📁 Project Structure

```
AprioriInsights/
│
├── data/                       # Transactional dataset (e.g., basket_analysis.csv)
├── notebooks/                  # Jupyter notebook (for exploratory work)
├── src/                        # Modular Python source files
│   ├── preprocessing.py        # Data loading and inspection
│   ├── apriori_utils.py        # Apriori logic and rule generation
│   └── visualizations.py       # Custom visual plots
├── reports/                    # (Optional) Exported PDF reports
├── images/                     # Generated visualizations
├── run_analysis.py             # Main script to run the analysis
├── requirements.txt            # Project dependencies
└── README.md                   # This file
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/DeenoBajithaCode/AprioriInsights.git
cd AprioriInsights
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 How to Run

### ▶️ Run from script

```bash
python run_analysis.py
```

### 📓 Or use the notebook

Open `notebooks/01_market_basket_analysis.ipynb` in **JupyterLab** or **VS Code** and follow the step-by-step cells.

---

## 📈 Sample Visuals

- **Support vs Lift by Itemset Size**
- **Average Confidence by Itemset Size**
- **Top Rules by Lift and Support**

_All generated during runtime and can be customized._

---

## 💡 Business Insights

Based on rule strength:
- 🎯 Use frequent pairs for general promotions
- 🧃 Target larger itemsets in loyalty programs
- 🧩 Identify cross-selling and bundling opportunities

---

## 🧰 Tech Stack

- **Python 3.10+**
- **Pandas**, **mlxtend**, **matplotlib**, **seaborn**
- (Optional) JupyterLab for interactive exploration

---

## 📬 Contact

Made with ❤️ by **Deeno Bajitha**  
Connect on [GitHub](https://github.com/DeenoBajithaCode)

---
