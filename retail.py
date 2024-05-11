import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Generate synthetic customer data
np.random.seed(0)  # For reproducibility

num_customers = 1000
total_purchases = np.random.randint(1, 1000, size=num_customers)
average_purchase = np.random.randint(1, 100, size=num_customers)

# Create a DataFrame
customer_data = pd.DataFrame({
    'TotalPurchases': total_purchases,
    'AveragePurchase': average_purchase
})

# Display the first few rows of the DataFrame
print(customer_data.head())

# Select relevant features for clustering
selected_features = ['TotalPurchases', 'AveragePurchase']

# Preprocess the data
X = customer_data[selected_features].values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine optimal number of clusters using the Elbow method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot the Elbow method graph
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
plt.show()

# Based on the Elbow method, select the optimal number of clusters
optimal_num_clusters = 3  # Adjust based on the graph

# Perform K-means clustering with the optimal number of clusters
kmeans = KMeans(n_clusters=optimal_num_clusters, init='k-means++', random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Add cluster labels to the original DataFrame
customer_data['Cluster'] = clusters

# Display cluster centers
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
cluster_centers_df = pd.DataFrame(cluster_centers, columns=selected_features)
print("Cluster Centers:")
print(cluster_centers_df)

# Visualize the clusters
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='X', s=100, color='red')
plt.title('Customer Segmentation based on Purchase History')
plt.xlabel('Total Purchases')
plt.ylabel('Average Purchase')
plt.show()

# Analyze the characteristics of each cluster and interpret the results
# For example, you could calculate the mean or median of each feature within each cluster
cluster_analysis = customer_data.groupby('Cluster')[selected_features].mean()
print("Cluster Analysis:")
print(cluster_analysis)