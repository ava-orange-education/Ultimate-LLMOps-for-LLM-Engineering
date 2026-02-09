# Prepare dataset
dataset = load_dataset("your_custom_dataset")
tokenized = dataset.map(lambda x: tokenizer(x["text"], truncation=True))