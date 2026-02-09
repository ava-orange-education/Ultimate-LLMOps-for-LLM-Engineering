class ABTestManager:
    def __init__(self):
        self.results = {"variant_A": [], "variant_B": []}
    def assign_variant(self, user_id):
        """Randomly assign user to A or B variant"""
        # Use consistent hashing for same user
        return "variant_A" if hash(user_id) % 2 == 0 else "variant_B"
    def get_response(self, prompt, variant, user_id):
        """Get response from appropriate model/prompt variant"""
        if variant == "variant_A":
            # Original model or prompt
            response = model_v1.generate(prompt)
            version = "v1.0"
        else:
            # New model or improved prompt
            response = model_v2.generate(prompt)  
            version = "v2.0"
        # Log for analysis
        self.log_interaction(user_id, prompt, response, variant, version)
        return response
    def record_feedback(self, user_id, variant, rating, task_completed):
        """Record user feedback for the variant they saw"""
        self.results[variant].append({
            "user_id": user_id,
            "rating": rating,
            "task_completed": task_completed
        })
    def analyze_results(self):
        """Compare performance between variants"""
        for variant in ["variant_A", "variant_B"]:
            data = self.results[variant]
            if not data:
                continue
            avg_rating = sum(r["rating"] for r in data) / len(data)
            completion_rate = sum(r["task_completed"] for r in data) / len(data)
            print(f"{variant}: Avg Rating={avg_rating:.2f}, "
                  f"Completion Rate={completion_rate:.2%}, n={len(data)}")
        # Statistical significance test would go here
        return self.results