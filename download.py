from datasets import load_dataset
import os

# Specify the dataset you want to download
dataset_name = "Revankumar/News_room"  # Change this to the dataset you want to use

# Load the dataset
dataset = load_dataset(dataset_name)

folder_path = "artifacts/Data ingestion"
os.makedirs(folder_path, exist_ok=True)

# Save the dataset to the target folder
dataset.save_to_disk(folder_path)

print(f"Dataset {dataset_name} saved to {folder_path}")
