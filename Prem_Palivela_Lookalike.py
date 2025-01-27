# IMPORTING LIBRARIES
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# LOADING DATASETS
Transactions = pd.read_csv('Transactions.csv')


def get_similar_customers(customer_id, similarity_df, n=3):
    if customer_id not in similarity_df.index:
        return f"CustomerID {customer_id} not found in the data."
    similar_customers = similarity_df[customer_id].sort_values(ascending=False)[1:n+1]
    return [(idx, round(score, 2)) for idx, score in similar_customers.items()]

def compute_similarity():
    # Creating customer-product matrix
    cust_prod_matrix = Transactions.pivot_table(index='CustomerID', columns='ProductID', values='Quantity', aggfunc='sum', fill_value=0)

    # Computing Cosine similarity and storing in Pandas dataframe
    similarity_matrix = cosine_similarity(cust_prod_matrix)
    similarity_df = pd.DataFrame(similarity_matrix, index=cust_prod_matrix.index, columns=cust_prod_matrix.index)

    lookalikes = {}
    for customer_id in similarity_df.index[:20]:
        lookalikes[customer_id] = get_similar_customers(customer_id,similarity_df)

    # Saving lookalikes to CSV
    lookalikes_df = pd.DataFrame.from_dict(lookalikes, orient='index', columns=['Similar_Customer_1', 'Similar_Customer_2', 'Similar_Customer_3'])
    lookalikes_df.to_csv('Prem_Palivela_Lookalike.csv', index_label='CustomerID')

if __name__  == "__main__":
    compute_similarity()