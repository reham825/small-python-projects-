tasks = ["study english", "walking"]


def View_Tasks():
    if not tasks:
        print("no tasks to display")
    else:
        for i, task in enumerate(tasks, 1):
            print(f'{i}-{task}')


def Add_a_Task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("done :) ")


def Remove_a_task(task_number):
    del tasks[task_number - 1]
    print("done :) ")


print('''Todo List Menu:
 1. View Tasks
 2. Add a Task
 3. Remove a Task
 4. Exit''')
while True:
    choice = input("Enter your choice: ")
    if choice == '1':
        View_Tasks()
    elif choice == '2':
        Add_a_Task()
    elif choice == '3':
        task_number = int(input("Enter the number of task you want to remove : "))
        Remove_a_task(task_number)
    else:
        break
