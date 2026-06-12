from datetime import datetime

def validate_task_title(title):
    # Matches: Check validation – Check for if len()
    if len(title.strip()) == 0:
        print("Task title cannot be empty.")
        return False
    return True

def validate_task_description(description):
    if len(description.strip()) == 0:
        print("Task description cannot be empty.")
        return False
    return True

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
        return True
    except ValueError:  # Matches: Check validation – Check for ValueError
        print("Invalid date format. Use YYYY-MM-DD.")
        return False