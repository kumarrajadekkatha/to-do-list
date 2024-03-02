import json
import os
import sys
from datetime import datetime, timedelta

# Function to load tasks from a JSON file
def load_tasks():
    if os.path.exists('tasks_dataFile.json'):
        with open('tasks_dataFile.json', 'r') as file:
            return json.load(file)
    else:
        return []

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks_dataFile.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to add a task
def add_task(tasks, description, priority, due_date):
    task = {
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description}")

# Function to remove a task
def remove_task(tasks, task_no):
    if task_no < 0 or task_no >= len(tasks):
        print("Invalid task number.")
        return
    removed_task = tasks.pop(task_no)
    save_tasks(tasks)
    print(f"Task removed: {removed_task['description']}")

# Function to mark a task as completed
def complete_task(tasks, task_no):
    if task_no < 0 or task_no >= len(tasks):
        print("Invalid task number.")
        return
    tasks[task_no]['completed'] = True
    save_tasks(tasks)
    print(f"Task marked as completed: {tasks[task_no]['description']}")

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            status = "Done" if task['completed'] else "Not Done"
            dd = datetime.strptime(task['due_date'], "%Y-%m-%d")
            time_left = dd - datetime.now()
            print(f"{i + 1}. {task['description']} (Priority: {task['priority']}, Due Date: {time_left}, Status: {status})")

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Mark a task as completed")
        print("4. List tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter task priority (high, medium, low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, description, priority, due_date)
        elif choice == '2':
            task_no = int(input("Enter the task number to remove: ")) - 1
            remove_task(tasks, task_no)
        elif choice == '3':
            task_no = int(input("Enter the task number to mark as completed: ")) - 1
            complete_task(tasks, task_no)
        elif choice == '4':
            display_tasks(tasks)
        elif choice == '5':
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()