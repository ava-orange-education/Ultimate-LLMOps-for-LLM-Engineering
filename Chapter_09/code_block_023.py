# 10. Save the PEFT model and tokenizer
peft_model.save_pretrained("./peft_fine_tuned_model")
tokenizer.save_pretrained("./peft_fine_tuned_model")