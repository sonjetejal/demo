# Simple To-Do List in Python

todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f'Added: {task}')

def view_tasks():
    if not todo_list:
        print('No tasks in the list.')
    else:
        print('To-Do List:')
        for index, task in enumerate(todo_list, start=1):
            print(f'{index}. {task}')

def remove_task(task_number):
    if 0 < task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f'Removed: {removed_task}')
    else:
        print('Invalid task number.')

while True:
    print("\nOptions: [1] Add Task  [2] View Tasks  [3] Remove Task  [4] Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        task_num = int(input("Enter task number to remove: "))
        remove_task(task_num)
    elif choice == '4':
        print("Exiting To-Do List. Have a productive day!")
        break
    else:
        print("Invalid choice, try again.")
