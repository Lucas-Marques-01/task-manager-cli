# Task Manager CLI

Simple command-line task manager written in Python.  
Tasks are stored in a JSON file so they persist between executions.

## Features

- Add new tasks with title and description.
- List all tasks in the terminal.
- Mark tasks as done.
- Remove tasks.
- Data persistence using a local `tasks.json` file.

## Project structure

- `main.py`  
  Entry point of the application. Handles the menu/CLI and calls the helper functions.

- `storage.py`  
  Responsible for reading and writing the `tasks.json` file (load/save functions).

- `utils.py`  
  Utility functions used by the CLI (formatting, validation, helpers, etc.).

- `tasks.json`  
  Example data file with initial tasks. New tasks are saved here at runtime.

## Requirements

- Python 3.10+  
- Only standard library modules are used (`json`, `os`, etc.), so no extra dependencies are required.

## How to run

Inside the project folder:

python main.py


Follow the on-screen menu to create, list, complete or delete tasks.

## Notes

- `tasks.json` is a simple JSON file; you can edit or reset it manually if needed.
- Feel free to extend this project with categories, due dates, priorities or a future API/web backend.
