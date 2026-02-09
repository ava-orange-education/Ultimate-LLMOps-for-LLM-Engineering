# Track satisfaction over time
feedbacks_by_day = group_feedbacks_by_day(recent_feedbacks)
trends = analyzer.calculate_satisfaction_trend(feedbacks_by_day)
print(f"Weekly satisfaction trend: {trends}")