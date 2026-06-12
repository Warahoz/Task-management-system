from datetime import datetime

def validate_task_title(title):
    # Check if the title is empty using len()
    if len(title.strip()) == 0:
        print("Task title cannot be empty.")
        return False
    return True

def validate_task_description(description):
    # Check if description is empty using len()
    if len(description.strip()) == 0:
        print("Task description cannot be empty.")
        return False
    return True

def validate_due_date(due_date):
    try:
        # Tries to parse YYYY-MM-DD format
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
        return True
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return False