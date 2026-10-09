# Simple To-Do List Application

todo_list = []

def show_tasks():
    if not todo_list:
        print("\nYour to-do list is empty.\n")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(todo_list, start=1):
            status = "✔" if task["done"] else "✘"
            print(f"{i}. [{status}] {task['task']}")
        print()

while True:
    print("===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        task = input("Enter a new task: ")
        todo_list.append({"task": task, "done": False})
        print("Task added successfully!\n")

    elif choice == "3":
        show_tasks()
        try:
            task_num = int(input("Enter task number to mark as completed: "))
            todo_list[task_num - 1]["done"] = True
            print("Task marked as completed!\n")
        except (ValueError, IndexError):
            print("Invalid task number.\n")

    elif choice == "4":
        show_tasks()
        try:
            task_num = int(input("Enter task number to delete: "))
            removed = todo_list.pop(task_num - 1)
            print(f"Deleted task: {removed['task']}\n")
        except (ValueError, IndexError):
            print("Invalid task number.\n")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.\n")