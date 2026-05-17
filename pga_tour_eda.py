import pandas as pd

df = pd.read_csv("pga_tour_2025.csv")

# How many rows and columns?
print(df.shape)

# See just the first 5 rows
print(df.head())

# See all the column names
print(df.columns.tolist())

# Basic stats on every number column
print(df.describe())
top5 = df.sort_values("SG_Total", ascending=False).head(5)
print(top5[["Player", "SG_Total", "Wins_2025", "Earnings_M"]])

import matplotlib.pyplot as plt

# Top 10 players by Strokes Gained — bar chart
top10 = df.sort_values("SG_Total", ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.barh(top10["Player"], top10["SG_Total"], color="steelblue")
plt.xlabel("Strokes Gained Total")
plt.title("PGA Tour 2025 — Top 10 Players by Strokes Gained")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
# Chart 2: Earnings vs Wins scatter plot
plt.figure(figsize=(10, 6))
# Only label the notable players to avoid overlap
label_these = ["Scheffler", "McIlroy", "Fleetwood", "Spaun", "Henley"]

for i, row in df.iterrows():
    last_name = row["Player"].split()[-1]
    if last_name in label_these:
        plt.annotate(last_name,
                     (row["Wins_2025"], row["Earnings_M"]),
                     textcoords="offset points", xytext=(5, 5), fontsize=9)

plt.xlabel("Wins in 2025")
plt.ylabel("Earnings ($ Millions)")
plt.title("PGA Tour 2025 — Wins vs Earnings")
plt.tight_layout()
plt.show()
import seaborn as sns

# Chart 3: Correlation heatmap
plt.figure(figsize=(10, 8))

cols = ["Scoring_Avg", "SG_Total", "SG_OffTee", "SG_Approach", 
        "SG_Putting", "GIR_pct", "Earnings_M", "Wins_2025"]

corr = df[cols].corr()

sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", 
            center=0, linewidths=0.5)

plt.title("PGA Tour 2025 — Correlation Heatmap")
plt.tight_layout()
plt.show()
