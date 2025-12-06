# todo_app.py — Todo In-Memory Python Console App with Rich CLI

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt

console = Console()
tasks = []
next_id = 1

# ------------------------------
# Functions
# ------------------------------
def add_task():
    """Add a new task with title and optional description."""
    global next_id
    title = Prompt.ask("Enter task title").strip()
    if not title:
        console.print("[red]Error:[/red] Title cannot be empty.")
        return
    description = Prompt.ask("Enter task description (optional)", default="").strip()
    task = {
        "id": next_id,
        "title": title,
        "description": description,
        "status": "Incomplete"
    }
    tasks.append(task)
    console.print(f"[green]Task added successfully with ID {next_id}.[/green]")
    next_id += 1

def view_tasks():
    """List all tasks with ID, title, description, and status."""
    if not tasks:
        console.print("[yellow]No tasks found.[/yellow]")
        return
    table = Table(title="Todo Tasks")
    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Description", style="white")
    table.add_column("Status", justify="center", style="green")
    for task in tasks:
        status_color = "green" if task["status"] == "Complete" else "red"
        table.add_row(str(task["id"]), task["title"], task["description"], f"[{status_color}]{task['status']}[/{status_color}]")
    console.print(table)

def update_task():
    """Update the title and/or description of a task by ID."""
    try:
        task_id = IntPrompt.ask("Enter task ID to update")
    except ValueError:
        console.print("[red]Error:[/red] Invalid ID.")
        return
    for task in tasks:
        if task["id"] == task_id:
            new_title = Prompt.ask(f"Enter new title (leave blank to keep '{task['title']}')", default="").strip()
            new_description = Prompt.ask("Enter new description (leave blank to keep current)", default="").strip()
            if new_title:
                task["title"] = new_title
            if new_description:
                task["description"] = new_description
            console.print(f"[green]Task ID {task_id} updated successfully.[/green]")
            return
    console.print(f"[red]Error:[/red] Task with ID {task_id} not found.")

def delete_task():
    """Delete a task by ID."""
    try:
        task_id = IntPrompt.ask("Enter task ID to delete")
    except ValueError:
        console.print("[red]Error:[/red] Invalid ID.")
        return
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            console.print(f"[green]Task ID {task_id} deleted successfully.[/green]")
            return
    console.print(f"[red]Error:[/red] Task with ID {task_id} not found.")

def toggle_task_status():
    """Toggle task status between Complete and Incomplete by ID."""
    try:
        task_id = IntPrompt.ask("Enter task ID to toggle status")
    except ValueError:
        console.print("[red]Error:[/red] Invalid ID.")
        return
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Complete" if task["status"] == "Incomplete" else "Incomplete"
            console.print(f"[green]Task ID {task_id} status changed to {task['status']}.[/green]")
            return
    console.print(f"[red]Error:[/red] Task with ID {task_id} not found.")

# ------------------------------
# Main CLI Loop
# ------------------------------
def main():
    while True:
        console.print("\n[bold blue]--- Todo App Menu ---[/bold blue]")
        console.print("1. Add Task")
        console.print("2. View Tasks")
        console.print("3. Update Task")
        console.print("4. Delete Task")
        console.print("5. Mark Complete / Incomplete")
        console.print("6. Exit")
        choice = Prompt.ask("Select an option (1-6)").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            toggle_task_status()
        elif choice == "6":
            console.print("[bold green]Exiting Todo App. Goodbye![/bold green]")
            break
        else:
            console.print("[red]Invalid option.[/red] Please select a number between 1 and 6.")

# ------------------------------
# Entry Point
# ------------------------------
if __name__ == "__main__":
    main()
