# Usage: Gradually increase traffic_split if model_b performs well
router = ModelRouter(current_model, new_model, traffic_split=0.1)