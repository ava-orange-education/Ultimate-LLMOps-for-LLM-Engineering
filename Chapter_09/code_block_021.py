# 8. Create the Trainer
trainer = Trainer(
    model=peft_model,  # Use the PEFT model
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    # eval_dataset=tokenized_datasets["validation"], # If you have a validation set
    data_collator=lambda data: {
        'input_ids': torch.stack([f['input_ids'] for f in data]),
        'attention_mask': torch.stack([f['attention_mask'] for f in data]),
        'labels': torch.stack([f['labels'] for f in data])
    }
)