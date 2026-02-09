class FeedbackAnalyzer:
    def __init__(self):
        # Load pre-trained sentiment analysis model
        self.sentiment_analyzer = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
    def analyze_feedback_comment(self, comment):
        """Analyze sentiment of user feedback text"""
        if not comment or len(comment.strip()) < 3:
            return None
        result = self.sentiment_analyzer(comment[:512])[0]  # Limit length
        return {
            "sentiment": result["label"],  # POSITIVE or NEGATIVE
            "confidence": result["score"],
            "comment": comment
        }
    def identify_issues(self, feedbacks, sentiment_threshold=0.8):
        """Identify common issues from negative feedback"""
        negative_comments = []
        for feedback in feedbacks:
            analysis = self.analyze_feedback_comment(feedback["comment"])
            if (analysis and 
                analysis["sentiment"] == "NEGATIVE" and 
                analysis["confidence"] > sentiment_threshold):
                negative_comments.append({
                    "comment": feedback["comment"],
                    "confidence": analysis["confidence"],
                    "request_id": feedback.get("request_id"),
                    "timestamp": feedback.get("timestamp")
                })
        print(f"Found {len(negative_comments)} high-confidence negative feedbacks")
        # Extract common themes (simplified - use topic modeling in practice)
        return negative_comments
    def calculate_satisfaction_trend(self, feedbacks_by_day):
        """Track satisfaction over time"""
        trends = {}
        for day, feedbacks in feedbacks_by_day.items():
            sentiments = [
                self.analyze_feedback_comment(f["comment"])
                for f in feedbacks if f.get("comment")
            ]
            positive = sum(1 for s in sentiments 
                          if s and s["sentiment"] == "POSITIVE")
            total = len([s for s in sentiments if s])
            satisfaction_rate = positive / total if total > 0 else 0
            trends[day] = satisfaction_rate
        return trends