# Task Manager CLI

A simple command-line task manager built with Python and JSON for data persistence.

## Features

* Create new tasks
* View all tasks
* Mark tasks as complete or incomplete
* Delete tasks
* Persist tasks using a JSON file
* Validate user input
* Handle missing or invalid JSON files

## Technologies

* Python 3
* JSON
* Git / GitHub

## Project Structure

```text
task-manager-cli/
├── main.py
├── .gitignore
├── README.md
└── data/
    └── my_tasks.json
```

## How to Run

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/csodcaceres/task-manager-cli.git
cd task-manager-cli
```

Run the application:

```bash
python main.py
```

## Usage

The application provides a simple interactive menu:

```text
----- Mini To-Do App -----
1. View Tasks
2. Add Task
3. Mark Task as Complete/Incomplete
4. Delete Task
5. Exit
```

Tasks are stored locally in a JSON file, allowing them to remain available between executions.

## Data Persistence

The application uses a JSON file as a lightweight data store.

Each task contains a description and a status:

```json
{
    "task": "Proyect Python",
    "status": "incomplete"
}
```

The task data file is excluded from version control through `.gitignore`.

## Future Improvements

Possible future improvements include:

* Add task priorities
* Add due dates
* Search and filter tasks
* Improve the command-line interface
* Replace JSON storage with a database

## Author

Oscar Caceres

Backend Developer | Python • FastAPI • AI | Building in public
