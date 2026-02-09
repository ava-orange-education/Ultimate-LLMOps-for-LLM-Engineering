# Deploy model to endpoint
predictor = huggingface_model.deploy(
    initial_instance_count=1,
    instance_type="ml.g5.xlarge",  # GPU instance
    endpoint_name="llm-endpoint"
)