import pickle
import json
from pathlib import Path

def ensure_dir(dirname):
    dirname = Path(dirname)
    if not dirname.is_dir():
        dirname.mkdir(parents=True, exist_ok=False)

# json

def load_json(file_name):
    with open(file_name, 'r+') as file:
        return json.load(file)

def save_json(obj, file_name):
    with open(file_name, 'w+') as file:
        json.dump(obj, file, indent=4, sort_keys=False)
