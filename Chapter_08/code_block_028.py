# Production monitoring
def check_for_anomalies(current_latency, current_tokens, current_errors):
    """Check if current metrics are anomalous"""
    current_metrics = np.array([[current_latency, current_tokens, current_errors]])
    # Predict: -1 for anomaly, 1 for normal
    prediction = anomaly_detector.predict(current_metrics)
    # Get anomaly score (more negative = more anomalous)
    anomaly_score = anomaly_detector.score_samples(current_metrics)[0]
    if prediction[0] == -1:
        alert(f"Anomaly detected! Score: {anomaly_score:.3f}")
        return True, anomaly_score
    return False, anomaly_score