# Example: Golden Dataset structure
golden_dataset = [
    {
        "id": "golden_001",
        "category": "product_info",
        "prompt": "What are your business hours?",
        "expected_content": ["9 AM", "5 PM", "Monday-Friday"],
        "quality_criteria": {
            "min_relevance_score": 0.8,
            "max_latency_ms": 2000,
            "should_not_contain": ["unsure", "don't know"]
        }
    },
    {
        "id": "golden_002",
        "category": "refund_policy",
        "prompt": "How do I get a refund?",
        "expected_content": ["30 days", "contact support", "receipt"],
        "quality_criteria": {
            "min_relevance_score": 0.85,
            "max_latency_ms": 2000,
            "must_be_factual": True
        }
    },
    # ... more golden examples
]