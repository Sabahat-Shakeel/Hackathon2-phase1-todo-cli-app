# Quickstart Guide: TODO Console App

**Feature Branch**: `001-todo-console-app`
**Created**: 2025-12-06

## Introduction

This guide provides a quick overview of how to get started and use the In-Memory TODO Python Console App.

## Prerequisites

*   Python 3.10+ installed on your system.
*   The `Rich` library for enhanced CLI output. Install using pip:
    ```bash
    pip install rich
    ```

## Installation (Conceptual)

As a single-file application, direct installation is not typically required. You will run the `todo_app.py` script directly.

1.  **Clone the repository**: (If applicable)
    ```bash
    git clone [REPOSITORY_URL]
    cd [REPOSITORY_NAME]
    ```
2.  **Navigate to the application directory**:
    ```bash
    cd [PATH_TO_APP_DIRECTORY] # e.g., cd src
    ```

## Usage

Run the application from your terminal:

```bash
python todo_app.py
```

Upon starting, you will be presented with a menu of options.

### Available Commands

*   **`add <description>`**: Adds a new task.
    *   Example: `add Buy groceries`
*   **`list`**: Displays all current tasks in a formatted table.
*   **`update <task_id> <new_description>`**: Updates the description of an existing task.
    *   Example: `update 1 Buy milk and eggs`
*   **`delete <task_id>`**: Deletes a task by its ID. Requires confirmation.
    *   Example: `delete 2`
*   **`mark <task_id>`**: Toggles the completion status of a task.
    *   Example: `mark 1`
*   **`exit`**: Closes the application.

### Example Workflow

1.  Start the app: `python todo_app.py`
2.  Add a task: `add Learn Gemini`
3.  Add another task: `add Prepare presentation`
4.  List tasks: `list`
5.  Mark "Learn Gemini" as complete (assuming it's ID 1): `mark 1`
6.  Update "Prepare presentation" (assuming it's ID 2): `update 2 Finish presentation slides`
7.  List tasks again: `list`
8.  Delete "Learn Gemini" (assuming it's ID 1, will prompt for confirmation): `delete 1`
9.  Exit the app: `exit`

## Notes

*   All data is stored in-memory and will be lost when the application exits.
*   Commands are case-insensitive.
*   Task IDs are persistent and do not change when other tasks are deleted.
