import os

from fastapi import HTTPException
from json import load, JSONDecodeError


JSON_DIR = os.path.abspath('res/json/')


def read_json(file_name):
    try:
        with open(JSON_DIR+file_name, 'r', encoding='utf-8') as file:
            return load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except JSONDecodeError:
        raise HTTPException(status_code=400, detail="Error decoding JSON")
