import json
import os

FILE_PATH = "tasks.json"
def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


