# Load large teacher model
teacher_model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")