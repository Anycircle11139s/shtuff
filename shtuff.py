tasks = []

def show_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

while True:
    action = input("Enter 'add' to add a task, 'show' to view tasks, or 'quit' to exit: ").strip().lower()
    if action == 'add':
        task = input("Enter task: ")
        add_task(task)
    elif action == 'show':
        show_tasks()
    elif action == 'quit':
        break
    else:
        print("Invalid action.")