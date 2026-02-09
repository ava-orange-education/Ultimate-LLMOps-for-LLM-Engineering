# Fine-tune
trainer = Trainer(model=model, args=training_args, train_dataset=tokenized["train"])
trainer.train()