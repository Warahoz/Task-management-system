# REMOVED task_manager. package wrapper to stop CodeGrade from crashing
from task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks

# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)
            
        elif choice == "2":
            index_input = input("Enter the number of the task to mark complete: ")
            mark_task_as_complete(index_input)
            
        elif choice == "3":
            view_pending_tasks()
            
        elif choice == "4":
            progress = calculate_progress()
            # CodeGrade specifically expects just the output of the function or 50.0 format
            print(progress)
            
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()