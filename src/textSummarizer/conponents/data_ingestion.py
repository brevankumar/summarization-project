import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import DataIngestionConfig
from pathlib import Path
from datasets import load_dataset




class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_files_from_huggingface(self):

        # Specify the dataset you want to download
        dataset_name = self.config.DATASET_NAME  

        # Load the dataset
        dataset = load_dataset(dataset_name)

        folder_path = "artifacts/data_ingestion/newsroom_dataset"
        os.makedirs(folder_path, exist_ok=True)

        # Save the dataset to the target folder
        dataset.save_to_disk(folder_path)

        print(f"Dataset {dataset_name} saved to {folder_path}") 

        
