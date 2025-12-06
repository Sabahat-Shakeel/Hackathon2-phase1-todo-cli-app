# Tasks: TODO Console App

**Input**: Design documents from `/specs/001-todo-console-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, research.md, quickstart.md

**Tests**: This plan includes unit test tasks for all CRUD operations.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `todo_app.py` at repository root
- **Tests**: `tests/test_todo_app.py` at repository root

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure: `todo_app.py` and `tests/test_todo_app.py`
- [X] T002 Install `rich` dependency: `pip install rich`
- [X] T003 Add basic `main` function structure with Rich Console display in `todo_app.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Define `Task` dataclass (id, description, completed, created_at, updated_at) in `todo_app.py`
- [X] T005 Implement in-memory task storage (e.g., a list of `Task` objects) in `todo_app.py`
- [X] T006 Implement a unique, persistent ID generation mechanism for tasks in `todo_app.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add a Task (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new tasks.

**Independent Test**: Add a task and verify it is successfully stored.

### Tests for User Story 1

- [X] T007 [P] [US1] Write unit tests for `add_task()` functionality in `tests/test_todo_app.py`

### Implementation for User Story 1

- [X] T008 [P] [US1] Implement `add_task()` function to create and store new tasks in `todo_app.py`
- [X] T009 [P] [US1] Implement input validation for `add_task()` (non-empty description) in `todo_app.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - List Tasks (Priority: P1)

**Goal**: Allow users to view all tasks in a formatted list.

**Independent Test**: Add several tasks and verify all are displayed correctly.

### Tests for User Story 2

- [X] T010 [P] [US2] Write unit tests for `view_tasks()` functionality in `tests/test_todo_app.py`

### Implementation for User Story 2

- [X] T011 [P] [US2] Implement `view_tasks()` function to retrieve and prepare tasks for display in `todo_app.py`
- [X] T012 [P] [US2] Implement Rich table display for tasks, including status indicators, in `todo_app.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 6 - Exit Application (Priority: P1)

**Goal**: Allow users to exit the application.

**Independent Test**: Start and exit the application to confirm graceful termination.

### Tests for User Story 6

- [X] T013 [P] [US6] Write unit tests for `exit_app()` functionality in `tests/test_todo_app.py`

### Implementation for User Story 6

- [X] T014 [P] [US6] Implement `exit_app()` function to terminate the application in `todo_app.py`

**Checkpoint**: User Story 6 is functional.

---

## Phase 6: User Story 3 - Update a Task (Priority: P2)

**Goal**: Allow users to modify existing task descriptions.

**Independent Test**: Update a task and verify the new description is saved.

### Tests for User Story 3

- [X] T015 [P] [US3] Write unit tests for `update_task()` functionality in `tests/test_todo_app.py`

### Implementation for User Story 3

- [X] T016 [P] [US3] Implement `update_task()` function to find and modify task descriptions by ID in `todo_app.py`
- [X] T017 [P] [US3] Implement input validation for `update_task()` (valid task ID, non-empty description) in `todo_app.py`

**Checkpoint**: User Story 3 is functional.

---

## Phase 7: User Story 4 - Delete a Task (Priority: P2)

**Goal**: Allow users to remove tasks after confirmation.

**Independent Test**: Delete a task and confirm it's removed after user confirmation.

### Tests for User Story 4

- [X] T018 [P] [US4] Write unit tests for `delete_task()` functionality, including confirmation, in `tests/test_todo_app.py`

### Implementation for User Story 4

- [X] T019 [P] [US4] Implement `delete_task()` function to remove tasks by ID in `todo_app.py`
- [X] T020 [P] [US4] Implement user confirmation prompt for `delete_task()` in `todo_app.py`
- [X] T021 [P] [US4] Implement input validation for `delete_task()` (valid task ID) in `todo_app.py`

**Checkpoint**: User Story 4 is functional.

---

## Phase 8: User Story 5 - Mark Task as Complete (Priority: P2)

**Goal**: Allow users to toggle the completion status of tasks.

**Independent Test**: Mark a task as complete/incomplete and verify its status changes.

### Tests for User Story 5

- [X] T022 [P] [US5] Write unit tests for `toggle_task_status()` functionality in `tests/test_todo_app.py`

### Implementation for User Story 5

- [X] T023 [P] [US5] Implement `toggle_task_status()` function to change task completion status by ID in `todo_app.py`
- [X] T024 [P] [US5] Implement input validation for `toggle_task_status()` (valid task ID) in `todo_app.py`

**Checkpoint**: All user stories should now be independently functional

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and overall application quality

- [X] T025 Implement `main()` loop to display menu, parse commands (case-insensitive), and dispatch to appropriate functions in `todo_app.py`
- [X] T026 Integrate Rich colored text for all error messages in `todo_app.py`
- [X] T027 Ensure plain text is used for all user prompts and general informational output (excluding tables/errors) in `todo_app.py`
- [ ] T028 Conduct full integration testing of all CRUD operations and command handling.
- [ ] T029 Review `todo_app.py` for code readability, maintainability, and adherence to Python best practices.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-8)**: All depend on Foundational phase completion
  - P1 stories (Add, List, Exit) can proceed in parallel once foundational is complete.
  - P2 stories (Update, Delete, Mark) can proceed after P1s or in parallel if needed.
- **Polish (Phase 9)**: Depends on all user stories being complete.

### User Story Dependencies

- All user stories are designed to be largely independent after the Foundational phase.

### Within Each User Story

- Tests MUST be written and FAIL before implementation.
- Core function implementation before validation/error handling.

### Parallel Opportunities

- All tasks marked [P] can run in parallel (within their respective phases and story contexts).
- Once the Foundational phase is complete, P1 user stories (Add, List, Exit) can be worked on in parallel.
- P2 user stories (Update, Delete, Mark) can follow.

---

## Implementation Strategy

### MVP First (Add, List, Exit Tasks)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3.  Complete Phase 3: User Story 1 (Add)
4.  Complete Phase 4: User Story 2 (List)
5.  Complete Phase 5: User Story 6 (Exit)
6.  **STOP and VALIDATE**: Test Add, List, Exit functionalities independently.
7.  Deploy/demo if ready.

### Incremental Delivery

1.  Complete Setup + Foundational → Foundation ready
2.  Add User Story 1 (Add) → Test independently → Deploy/Demo
3.  Add User Story 2 (List) → Test independently → Deploy/Demo
4.  Add User Story 6 (Exit) → Test independently → Deploy/Demo
5.  Add User Story 3 (Update) → Test independently → Deploy/Demo
6.  Add User Story 4 (Delete) → Test independently → Deploy/Demo
7.  Add User Story 5 (Mark) → Test independently → Deploy/Demo
8.  Each story adds value without breaking previous stories.

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
