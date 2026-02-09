# 8. Save the fine-tuned model and tokenizer
trainer.save_model("./fine_tuned_model")
tokenizer.save_pretrained("./fine_tuned_model")