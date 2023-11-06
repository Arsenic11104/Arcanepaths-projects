to_do_list = []
def add_task(task):
    to_do_list.append(task)
    print(f"Task '{task}' has been added to the to-do list.")
def remove_task(task):
    if task in to_do_list:
        to_do_list.remove(task)
        print(f"Task '{task}' has been removed from the to-do list.")
    else:
        print(f"Task '{task}' not found in the to-do list.")
def display_to_do_list():
    print("\nTo-Do List:")
    for index, task in enumerate(to_do_list, start=1):
        print(f"{index}. {task}")
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display to-do list")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "3":
        display_to_do_list()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
