@app.post("/chatbot/feedback")
def submit_feedback(request_id, rating, comment):
    feedback_collector.collect_feedback(
        request_id=request_id,
        user_id=get_current_user(),
        response=get_response_from_cache(request_id),
        rating=rating,
        comment=comment
    )