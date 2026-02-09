# Analyze single feedback
feedback = {"comment": "The response was completely wrong and unhelpful!"}
sentiment = analyzer.analyze_feedback_comment(feedback["comment"])
print(f"Sentiment: {sentiment['sentiment']} (confidence: {sentiment['confidence']:.2f})")