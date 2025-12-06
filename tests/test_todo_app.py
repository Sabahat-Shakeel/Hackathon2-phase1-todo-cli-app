# test_todo_app.py — Unit tests for todo_app.py using unittest and mock

import unittest
from unittest.mock import patch
import todo_app
from rich.table import Table

class TestTodoApp(unittest.TestCase):

    def setUp(self):
        # Reset tasks list and next_id before each test
        todo_app.tasks.clear()
        todo_app.next_id = 1

    @patch('builtins.input', side_effect=["Test Task", "Test description"])
    @patch.object(todo_app.console, 'print')
    def test_add_task_creates_task(self, mock_print, mock_input):
        todo_app.add_task()
        self.assertEqual(len(todo_app.tasks), 1)
        self.assertEqual(todo_app.tasks[0]['title'], "Test Task")
        self.assertEqual(todo_app.tasks[0]['description'], "Test description")
        self.assertEqual(todo_app.tasks[0]['status'], "Incomplete")
        self.assertEqual(todo_app.next_id, 2)
        mock_print.assert_called_once()

    @patch('builtins.input', side_effect=["", "Some description"])
    @patch.object(todo_app.console, 'print')
    def test_add_task_empty_title(self, mock_print, mock_input):
        todo_app.add_task()
        self.assertEqual(len(todo_app.tasks), 0)
        self.assertEqual(todo_app.next_id, 1)
        mock_print.assert_called_once_with("[red]Error:[/red] Title cannot be empty.")

    @patch.object(todo_app.console, 'print')
    def test_view_tasks_empty(self, mock_print):
        todo_app.view_tasks()
        mock_print.assert_called_once_with("[yellow]No tasks found.[/yellow]")

    @patch('builtins.input', side_effect=["Task1", "Desc1", "Task2", "Desc2"])
    @patch.object(todo_app.console, 'print')
    def test_view_tasks_with_tasks(self, mock_print, mock_input):
        todo_app.add_task()
        todo_app.add_task()
        todo_app.view_tasks()
        # console.print should be called at least once with a Table instance
        args, kwargs = mock_print.call_args
        self.assertIsInstance(args[0], Table)

    @patch('builtins.input', side_effect=["1", "Updated Task", "Updated Desc"])
    @patch.object(todo_app.console, 'print')
    def test_update_task_success(self, mock_print, mock_input):
        todo_app.tasks.append({'id': 1, 'title': 'Old', 'description': 'Old Desc', 'status': 'Incomplete'})
        todo_app.update_task()
        self.assertEqual(todo_app.tasks[0]['title'], "Updated Task")
        self.assertEqual(todo_app.tasks[0]['description'], "Updated Desc")
        mock_print.assert_called_with("[green]Task ID 1 updated successfully.[/green]")

    @patch('builtins.input', side_effect=["99", "New Title", "New Desc"])
    @patch.object(todo_app.console, 'print')
    def test_update_task_not_found(self, mock_print, mock_input):
        todo_app.tasks.append({'id': 1, 'title': 'Task', 'description': 'Desc', 'status': 'Incomplete'})
        todo_app.update_task()
        mock_print.assert_called_with("[red]Error:[/red] Task with ID 99 not found.")

    @patch('builtins.input', side_effect=["1"])
    @patch.object(todo_app.console, 'print')
    def test_delete_task_success(self, mock_print, mock_input):
        todo_app.tasks.append({'id': 1, 'title': 'Task', 'description': 'Desc', 'status': 'Incomplete'})
        todo_app.delete_task()
        self.assertEqual(len(todo_app.tasks), 0)
        mock_print.assert_called_with("[green]Task ID 1 deleted successfully.[/green]")

    @patch('builtins.input', side_effect=["99"])
    @patch.object(todo_app.console, 'print')
    def test_delete_task_not_found(self, mock_print, mock_input):
        todo_app.tasks.append({'id': 1, 'title': 'Task', 'description': 'Desc', 'status': 'Incomplete'})
        todo_app.delete_task()
        self.assertEqual(len(todo_app.tasks), 1)
        mock_print.assert_called_with("[red]Error:[/red] Task with ID 99 not found.")

    @patch('builtins.input', side_effect=["1"])
    @patch.object(todo_app.console, 'print')
    def test_toggle_task_status_complete(self, mock_print, mock_input):
        todo_app.tasks.append({'id': 1, 'title': 'Task', 'description': 'Desc', 'status': 'Incomplete'})
        todo_app.toggle_task_status()
        self.assertEqual(todo_app.tasks[0]['status'], 'Complete')
        mock_print.assert_called_with("[green]Task ID 1 status changed to Complete.[/green]")

    @patch('builtins.input', side_effect=["1"])
    @patch.object(todo_app.console, 'print')
    def test_toggle_task_status_incomplete(self, mock_print, mock_input):
        todo_app.tasks.append({'id': 1, 'title': 'Task', 'description': 'Desc', 'status': 'Complete'})
        todo_app.toggle_task_status()
        self.assertEqual(todo_app.tasks[0]['status'], 'Incomplete')
        mock_print.assert_called_with("[green]Task ID 1 status changed to Incomplete.[/green]")

    @patch('builtins.input', side_effect=["99"])
    @patch.object(todo_app.console, 'print')
    def test_toggle_task_status_not_found(self, mock_print, mock_input):
        todo_app.tasks.append({'id': 1, 'title': 'Task', 'description': 'Desc', 'status': 'Incomplete'})
        todo_app.toggle_task_status()
        self.assertEqual(todo_app.tasks[0]['status'], 'Incomplete')
        mock_print.assert_called_with("[red]Error:[/red] Task with ID 99 not found.")

if __name__ == "__main__":
    unittest.main()
