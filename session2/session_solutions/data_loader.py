import csv
from typing import List, Dict

def load_csv_as_dicts(path: str) -> List[Dict[str, str]]:
    """
    Loads a CSV file from the given path and returns a list of dictionaries,
    where each dictionary represents a row with keys from the CSV header.
    Args:
        path (str): Path to the CSV file.
    Returns:
        List[Dict[str, str]]: List of rows as dictionaries.
    Raises:
        FileNotFoundError: If the file does not exist.
        Exception: For other IO or CSV errors.
    """
    with open(path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]
