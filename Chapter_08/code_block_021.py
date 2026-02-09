# Example: Cost tracking for LLM API calls
class CostTracker:
    def __init__(self):
        # Example pricing (OpenAI GPT-4 style)
        self.input_price_per_1k = 0.03   # $0.03 per 1k input tokens
        self.output_price_per_1k = 0.06  # $0.06 per 1k output tokens
    def calculate_cost(self, input_tokens, output_tokens):
        """Calculate cost for a single request"""
        input_cost = (input_tokens / 1000) * self.input_price_per_1k
        output_cost = (output_tokens / 1000) * self.output_price_per_1k
        total_cost = input_cost + output_cost
        return total_cost
    def log_request_cost(self, request_id, input_tokens, output_tokens):
        """Log cost for monitoring and alerting"""
        cost = self.calculate_cost(input_tokens, output_tokens)
        # Log to monitoring system
        log_metric("llm_cost_per_request", cost, {"request_id": request_id})
        # Example alert: expensive request
        if cost > 0.10:  # $0.10 threshold
            alert(f"High-cost request: ${cost:.4f} for {request_id}")
        return cost