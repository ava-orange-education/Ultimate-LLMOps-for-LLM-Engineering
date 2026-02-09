# When user provides feedback
@app.post("/feedback")
def feedback_endpoint(user_id, variant, rating, task_completed):
    ab_test.record_feedback(user_id, variant, rating, task_completed)