# Train model on normal data
anomaly_detector = IsolationForest(contamination=0.1, random_state=42)
anomaly_detector.fit(historical_metrics)