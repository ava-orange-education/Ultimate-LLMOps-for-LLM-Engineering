# In your API endpoint
@app.post("/chat")
def chat_endpoint(prompt, user_id):
    variant = ab_test.assign_variant(user_id)
    response = ab_test.get_response(prompt, variant, user_id)
    return {"response": response, "variant": variant}