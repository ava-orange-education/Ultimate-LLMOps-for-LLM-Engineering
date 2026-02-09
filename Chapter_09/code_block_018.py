# 6. Preprocess the dataset
def preprocess_function(examples):
    inputs = [doc for doc in examples["question"]]
    model_inputs = tokenizer(inputs, max_length=128, truncation=True, padding="max_length")
    model_inputs["labels"] = model_inputs["input_ids"].clone()
    return model_inputs