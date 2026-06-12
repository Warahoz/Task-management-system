from datetime import datetime
# Import validation functions from our local package
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    # Validate using the validation module functions
    if (validate_task_title(title) and 
        validate_task_description(description) and 
        validate_due_date(due_date)):
        
        new_task = {
            "title": title.strip(),
            "description": description.strip(),
            "due_date": due_date.strip(),
            "completed": False
        }
        tasks.append(new_task)
        print("Task added successfully!")
        return True
    else:
        print("Failed to add task due to validation error.")
        return False

# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    try:
        idx = int(index) - 1 # Convert human choice to index breakdown
        if 0 <= idx < len(tasks):
            tasks[idx]["completed"] = True
            print("Task marked as complete!")
            return True
        else:
            print("Invalid task index.")
            return False
    except ValueError:
        print("Please enter a valid numeric index.")
        return False

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks found.")
        return
    
    print("\n--- Pending Tasks ---")
    # Display the actual total index array tracking for the user
    for idx, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{idx + 1}. Title: {task['title']} | Due: {task['due_date']}")
            print(f"   Description: {task['description']}")
    print("--------------------")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        print("No tasks available to track.")
        return 0.0
        
    completed_count = len([t for t in tasks if t["completed"]])
    progress = (completed_count / len(tasks)) * 100
    return progress