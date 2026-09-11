"""
A simple command-line task manager built with Python and JSON for data persistence.
"""
import json
import os

# File for storing tasks
TASK_FILE = "data/my_tasks.json"

# Ensure the task file exists
def initialize_task_file():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w") as file:
            json.dump([], file)

# Step 1: Load tasks from the JSON file
def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

# Step 2: Save tasks to the JSON file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Step 3: Add a new task
def add_task():
    task_description = input("Enter the task description: ").strip()

    if not task_description:
        print("Task description cannot be empty.")
        return

    tasks = load_tasks()
    tasks.append({"task": task_description, "status": "incomplete"})
    save_tasks(tasks)
    print(f'Task "{task_description}" added successfully!')

# Step 4: View all tasks
def view_tasks():
    tasks = load_tasks()
    if tasks:
        print("\n----- To-Do List -----")
        for index, task in enumerate(tasks, start=1):
            status = "✅" if task["status"] == "complete" else "❌"
            print(f"{index}. {task['task']} - {status}")
    else:
        print("\nNo tasks found. Add a new task to get started!")

# Step 5: Mark a task as complete
def mark_task_complete():
    tasks = load_tasks()
    view_tasks()
    try:
        task_number = int(input("\nEnter the task number to mark as complete: ")) -1
        if 0 <= task_number < len(tasks):
            new_status = input("Enter the new status (complete/incomplete): ").strip().lower()

            if new_status not in ["complete", "incomplete"]:
                print("Invalid status. Please enter 'complete' or 'incomplete'.")
                return

            tasks[task_number]["status"] = new_status
            save_tasks(tasks)
            print(f'Task "{tasks[task_number]["task"]}" marked as {new_status}!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Step 6: Delete a task
def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_number = int(input("\nEnter the task number to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            save_tasks(tasks)
            print(f'Task "{removed_task["task"]}" deleted successfully!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Step 7: Main menu for the To-Do App
def display_menu():
    
    print("\n----- Mini To-Do App -----")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete/Incomplete")
    print("4. Delete Task")
    print("5. Exit")

# Step 8: Run the To-Do App
def main():
    initialize_task_file()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the To-Do App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()