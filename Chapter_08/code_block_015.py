# Method 2: KS test on first principal component
from sklearn.decomposition import PCA
pca = PCA(n_components=1)
baseline_pc1 = pca.fit_transform(baseline_embeddings).flatten()
current_pc1 = pca.transform(current_embeddings).flatten()