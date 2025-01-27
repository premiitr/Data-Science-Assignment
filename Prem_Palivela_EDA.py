# IMPORTING LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# LOADING DATASETS
Customers = pd.read_csv('Customers.csv')
Products = pd.read_csv('Products.csv')
Transactions = pd.read_csv('Transactions.csv')

# # Basic info about the datasets
# print(Customers.info())
# print(Products.info())
# print(Transactions.info())

# # Summary statistics
# print(Customers.describe())
# print(Products.describe())
# print(Transactions.describe())

# VISUALIZE DATA
def plotting():

    plt.rcParams["figure.figsize"] = [10, 5]
    plt.rcParams["figure.autolayout"] = True

    # Customer Distribution
    counter = Counter(Customers['Region'])
    cus_labels = list(counter.keys())
    cus_counts = list(counter.values())
    colors = plt.cm.Pastel1(range(len(cus_labels)))
    x_positions = range(len(cus_labels))
    plt.xticks(x_positions, cus_labels)
    plt.bar(cus_labels, cus_counts, color=colors, edgecolor='black', width=0.5)
    plt.xlabel('Region')
    plt.ylabel('Number of Customers')
    plt.title('Customer Distribution by Region')
    plt.show()

    # Product Distribution
    counter = Counter(Products['Category'])
    pro_labels = list(counter.keys())
    pro_counts = list(counter.values())
    colors = plt.cm.Pastel1(range(len(pro_labels)))
    plt.bar(pro_labels, pro_counts, color=colors, edgecolor='black', width=0.5)
    plt.xlabel('Category')
    plt.ylabel('Number of Products')
    plt.title('Product Distribution by Category')
    plt.show()

    # Transactions Plot
    Transactions['TransactionDate'] = pd.to_datetime(Transactions['TransactionDate'])
    Transactions['Month'] = Transactions['TransactionDate'].dt.to_period('M')
    monthly_totals = Transactions.groupby('Month')['TotalValue'].sum()
    plt.plot(monthly_totals.index.astype(str), monthly_totals, marker='o', linestyle='-', color='lightcoral', linewidth=2)
    plt.title('Monthly Total Transaction Value', fontsize=14)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Total Value', fontsize=12)
    plt.xticks(rotation=30) 
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plotting()