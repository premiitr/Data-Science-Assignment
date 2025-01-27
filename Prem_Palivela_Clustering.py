# IMPORTING LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import davies_bouldin_score

# LOADING DATASETS
Customers = pd.read_csv('Customers.csv')
Transactions = pd.read_csv('Transactions.csv')

# Combining Customer profile and transaction data
customer_data = Customers.merge(Transactions.groupby('CustomerID').agg({'TotalValue': 'sum', 'Quantity': 'sum'}).reset_index(),on='CustomerID',how='left').fillna(0)


def cluster_model(n,scaled_data):
    # Applying KMeans clustering
    kmeans = KMeans(n_clusters=n, random_state=36)
    customer_data['Cluster'] = kmeans.fit_predict(scaled_data)

    # Evaluate clustering
    db_index = davies_bouldin_score(scaled_data, customer_data['Cluster'])
    print(f'Davies-Bouldin Index: {db_index}')

    # Visualize clusters
    colors = plt.cm.tab10(range(n))
    for cluster in range(n):  # Assuming n clusters
        cluster_data = customer_data[customer_data['Cluster'] == cluster]
        plt.scatter(cluster_data['TotalValue'], cluster_data['Quantity'], label=f'Cluster {cluster}', color=colors[cluster], alpha=0.7)
    plt.xlabel("TotalValue")
    plt.ylabel("Quantity")
    plt.legend(title='Clusters', loc="upper right")
    plt.show()

    # Save clustering results
    customer_data.to_csv('Prem_Palivela_Clustering.csv', index=False)

if __name__ == "__main__":
    # Preprocess data for clustering
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(customer_data[['TotalValue', 'Quantity']])
    n = 5
    cluster_model(n,scaled_data)