# Usage in monitoring loop
is_anomalous, score = check_for_anomalies(
    current_latency=2500,  # ms
    current_tokens=350,
    current_errors=5
)