# 5. Define training arguments
training_args = TrainingArguments(
   output_dir="./fine_tuned_model",  # Directory to save the fine-tuned model
   overwrite_output_dir=True,
   num_train_epochs=3,  # Adjust as needed
   per_device_train_batch_size=4,  # Adjust based on your GPU memory
   save_steps=500,
   save_total_limit=2,
   learning_rate=5e-5,  # Adjust as needed
   report_to="none"  # Remove if you want to use TensorBoard or Weights & Biases
)