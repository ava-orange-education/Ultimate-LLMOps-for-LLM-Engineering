# Define model configuration
huggingface_model = HuggingFaceModel(
    model_data="s3://your-bucket/model.tar.gz",
    role="arn:aws:iam::<ACCT_ID>:role/SageMakerRole",
    transformers_version="4.26",
    pytorch_version="1.13",
    py_version="py39",
)