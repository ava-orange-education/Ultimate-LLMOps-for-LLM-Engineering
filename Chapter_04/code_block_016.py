def validate_payload(s: str):
    try:
        data = json.loads(s)
    except Exception as e:
        raise ValueError(f"Malformed JSON: {e}")
    required = {"product", "month", "goal"}
    missing = required - set(data.keys())
    if missing:
        raise ValueError(f"Missing keys: {missing}")
    if not isinstance(data["product"], str) or not isinstance(data["month"], str) or not isinstance(data["goal"], str):
        raise ValueError("Fields must be strings")
    return data