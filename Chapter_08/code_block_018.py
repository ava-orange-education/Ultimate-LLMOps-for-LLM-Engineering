class FeedbackCollector:
    def collect_feedback(self, request_id, user_id, response, 
                        rating=None, comment=None):
        """Collect and store user feedback"""
        feedback = {
            "timestamp": datetime.utcnow().isoformat(),
            "request_id": request_id,
            "user_id": user_id,
            "rating": rating,  # e.g., 1-5 or thumbs up/down
            "comment": comment,
            "response_length": len(response),
        }
        # Store in database/log system
        self.store_feedback(feedback)
        # Real-time alerting on negative feedback
        if rating and rating <= 2:
            self.alert_on_negative_feedback(feedback)
        return feedback
    def analyze_feedback_trends(self, time_window="24h"):
        """Analyze aggregated feedback"""
        feedbacks = self.get_recent_feedback(time_window)
        positive = sum(1 for f in feedbacks if f['rating'] >= 4)
        negative = sum(1 for f in feedbacks if f['rating'] <= 2)
        satisfaction_rate = positive / len(feedbacks) if feedbacks else 0
        print(f"Satisfaction rate: {satisfaction_rate:.2%}")
        return satisfaction_rate