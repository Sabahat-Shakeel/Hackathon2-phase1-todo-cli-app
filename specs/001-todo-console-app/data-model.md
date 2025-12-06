# Data Model for TODO Console App

**Feature Branch**: `001-todo-console-app`
**Created**: 2025-12-06
**Source**: `specs/001-todo-console-app/spec.md`

## Entity: Task

Represents a single to-do item within the application. Tasks are stored in-memory.

| Attribute    | Type      | Description                                     | Constraints                                         |
| :----------- | :-------- | :---------------------------------------------- | :-------------------------------------------------- |
| `id`         | `integer` | A unique identifier for the task.               | Unique, Persistent (non-recycled)                   |
| `description`| `string`  | The textual content of the task.                | Cannot be empty.                                    |
| `completed`  | `boolean` | The completion status of the task.              | Default `False` (incomplete)                        |
| `created_at` | `datetime`| Timestamp when the task was created.            | Auto-generated on creation                          |
| `updated_at` | `datetime`| Timestamp when the task was last updated.       | Auto-generated on creation and any subsequent update|

## Relationships

- No explicit relationships with other entities in this minimal application.

## State Transitions

- **Initial State**: A task is created with `completed` set to `False`.
- **Completion State**: `completed` can be toggled between `True` and `False` by the user.

## Data Volume / Scale Assumptions

- Assumed to be low, as tasks are stored in-memory and lost upon application exit. Not designed for large-scale task management.
