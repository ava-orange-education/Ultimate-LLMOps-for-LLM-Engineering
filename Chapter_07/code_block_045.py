class ModelRouter:
    def __init__(self, model_a, model_b, traffic_split=0.5):
        self.model_a = model_a  # Current production model
        self.model_b = model_b  # New candidate model
        self.traffic_split = traffic_split  # % to route to model_b
        self.metrics = {'model_a': [], 'model_b': []}
    def route_request(self, prompt: str, user_id: str) -> Dict[str, Any]:
        # Consistent routing per user
        use_model_b = hash(user_id) % 100 < (self.traffic_split * 100)
        model = self.model_b if use_model_b else self.model_a
        model_name = 'model_b' if use_model_b else 'model_a'
        # Generate response and track metrics
        response = model.generate(prompt)
        self.metrics[model_name].append({
            'latency': response.latency,
            'quality_score': self.evaluate(response)
        })
        return {'response': response.text, 'model': model_name}
    def get_performance_comparison(self):
        # Compare metrics between models
        return {
            'model_a': self._compute_stats(self.metrics['model_a']),
            'model_b': self._compute_stats(self.metrics['model_b'])
        }