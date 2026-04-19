# core/file_loader.py
import pandas as pd
import os

def load_file(path: str):
    if not path:
        raise ValueError("No file path provided")

    # Clean input
    path = path.strip()

    # Check existence
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    # Extract extension safely
    _, ext = os.path.splitext(path)
    ext = ext.lower()

    try:
        if ext == ".csv":
            return pd.read_csv(path)

        elif ext == ".parquet":
            return pd.read_parquet(path)

        elif ext == ".json":
            return pd.read_json(path)

        else:
            raise ValueError(f"Unsupported file format: {ext}")

    except Exception as e:
        raise RuntimeError(f"Failed to load file: {e}")