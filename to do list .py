import json
import os
from datetime import datetime

DATA_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save tasks to file
def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!\n")
        return

    print("\nYour To-Do List:")
    print("="*50)
    for idx, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx}. {task['task']} | Due: {task['due_date']} | Priority: {task['priority']} | Status: {status}")
    print("="*50 + "\n")

# Add a new task
def add_task(tasks):
    task_name = input("Enter task: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    priority = input("Priority (Low/Medium/High): ").capitalize().strip()
    if priority not in ["Low", "Medium", "High"]:
        priority = "Low"

    # Validate date
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format! Setting as 'None'.")
            due_date = "None"

    tasks.append({"task": task_name, "due_date": due_date, "priority": priority, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

# Mark a task as completed
def complete_task(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark completed: "))
        tasks[choice-1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    except (ValueError, IndexError):
        print("Invalid task number!")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
        deleted = tasks.pop(choice-1)
        save_tasks(tasks)
        print(f"Deleted task: {deleted['task']}")
    except (ValueError, IndexError):
        print("Invalid task number!")

# Search tasks
def search_tasks(tasks):
    keyword = input("Enter keyword to search: ").lower()
    results = [t for t in tasks if keyword in t["task"].lower()]
    if results:
        view_tasks(results)
    else:
        print("No matching tasks found!")

# Sort tasks
def sort_tasks(tasks):
    print("\nSort by: 1) Due Date  2) Priority")
    choice = input("Enter choice: ").strip()
    if choice == "1":
        tasks.sort(key=lambda x: (x["due_date"] if x["due_date"] != "None" else "9999-12-31"))
    elif choice == "2":
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        tasks.sort(key=lambda x: priority_order[x["priority"]])
    save_tasks(tasks)
    print("Tasks sorted!")

# Main Menu
def main():
    tasks = load_tasks()
    while True:
        print("""
========= TO-DO LIST =========
1. View Tasks
2. Add Task
3. Mark Task as Completed
4. Delete Task
5. Search Task
6. Sort Tasks
7. Exit
""")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            search_tasks(tasks)
        elif choice == "6":
            sort_tasks(tasks)
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
