# 4. Preprocess the dataset
def preprocess_function(examples):
   inputs = [doc for doc in examples["question"]]
   model_inputs = tokenizer(inputs, max_length=128, truncation=True, padding="max_length")
   # For causal language modeling, the labels are the same as the input IDs, shifted to the right
   model_inputs["labels"] = model_inputs["input_ids"].clone()
   return model_inputs