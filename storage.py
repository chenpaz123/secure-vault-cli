import json
import os


class StorageManager:
    def __init__(self, file_path: str):
        """constructor method
        args:
            file_path (str): The path to the JSON file for storage.
        """
        self.file_path = file_path

    def save_data(self, data: dict):
        """Saves the given data dictionary to a JSON file.

        Args:
            data (dict): The data to be saved.
        """
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load_data(self) -> dict:
        """Loads data from the JSON file.

        Returns:
            dict: The loaded data. Returns an empty dictionary if the file does not exist.
        """
        if not os.path.exists(self.file_path):
            return {}
        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)
