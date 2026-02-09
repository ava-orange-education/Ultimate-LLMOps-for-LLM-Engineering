# Adaptability testing with edge cases
def test_adaptability(chain):
    edge_cases = [
        "",  # Empty input
        "a" * 10000,  # Very long input
        "Find sales for product 'DROP TABLE users; --'",  # SQL injection attempt
        "🎵🎶 Musical notes in query 🎵🎶",  # Unicode/emoji
        "What is the meaning of life?",  # Off-topic query
    ]
    results = []
    for case in edge_cases:
        try:
            result = chain.invoke({"input": case})
            results.append({"input": case, "success": True, "output": result})
        except Exception as e:
            results.append({"input": case, "success": False, "error": str(e)})
    return results