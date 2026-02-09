print(f"Cosine distance between means: {drift_score}")
if drift_score > 0.1:  # Threshold
    alert("Embedding drift detected!")