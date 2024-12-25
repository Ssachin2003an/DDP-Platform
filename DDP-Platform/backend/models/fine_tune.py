import os
from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments
from datasets import load_dataset, DatasetDict

# Set device for training
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Paths
DATASET_PATH = "data/mcq_dataset.csv"  # Replace with your dataset path
MODEL_SAVE_PATH = "fine_tuned_model"

# Load Dataset
def load_and_prepare_data():
    """
    Load dataset and prepare it for fine-tuning.
    The dataset should have two columns: 'input_text' and 'target_text'.
    """
    dataset = load_dataset("csv", data_files={"train": DATASET_PATH})
    
    # Split into train and validation sets
    dataset = dataset["train"].train_test_split(test_size=0.1)
    print("Dataset loaded and split into train/validation sets.")
    return DatasetDict(train=dataset["train"], validation=dataset["test"])

# Tokenization
def preprocess_data(tokenizer, dataset):
    """
    Tokenize the dataset for model training.
    """
    def tokenize_function(examples):
        return tokenizer(
            examples["input_text"],
            max_length=512,
            truncation=True,
            padding="max_length"
        )

    tokenized_datasets = dataset.map(tokenize_function, batched=True)
    print("Dataset tokenized.")
    return tokenized_datasets

# Fine-tuning Function
def fine_tune_model():
    """
    Fine-tune the T5 model on the prepared dataset.
    """
    print("Loading tokenizer and model...")
    tokenizer = T5Tokenizer.from_pretrained("t5-small")
    model = T5ForConditionalGeneration.from_pretrained("t5-small").to(device)

    # Load and prepare data
    dataset = load_and_prepare_data()
    tokenized_datasets = preprocess_data(tokenizer, dataset)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=3,
        weight_decay=0.01,
        save_strategy="epoch",
        logging_dir="./logs",
        save_total_limit=2
    )

    # Define Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["validation"],
        tokenizer=tokenizer,
    )

    # Start fine-tuning
    print("Starting fine-tuning...")
    trainer.train()

    # Save the fine-tuned model
    model.save_pretrained(MODEL_SAVE_PATH)
    tokenizer.save_pretrained(MODEL_SAVE_PATH)
    print(f"Model saved to {MODEL_SAVE_PATH}.")

if __name__ == "__main__":
    fine_tune_model()
