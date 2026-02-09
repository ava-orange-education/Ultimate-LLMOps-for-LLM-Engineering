# Training phase: Learn normal behavior
historical_metrics = np.array([
    [latency, token_count, error_count],  # Features from normal operation
    # ... collect data over baseline period
])