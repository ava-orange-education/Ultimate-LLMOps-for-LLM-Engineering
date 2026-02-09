# Method 1: Compare mean embeddings
baseline_mean = np.mean(baseline_embeddings, axis=0)
current_mean = np.mean(current_embeddings, axis=0)
drift_score = cosine(baseline_mean, current_mean)