# todo.py
import os
import json

# Path to the file where to-do items will be stored
TODO_FILE = "todos.json"


# Load existing todos from the file
def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []


# Save todos to the file
def save_todos(todos):
    with open(TODO_FILE, "w") as file:
        json.dump(todos, file)


# Display the to-do list
def display_todos(todos):
    if not todos:
        print("No tasks to show.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(todos, 1):
            print(f"{index}. {task}")


# Add a new to-do task
def add_task(todos, task):
    todos.append(task)
    save_todos(todos)
    print(f"Task '{task}' added!")


# Remove a to-do task
def remove_task(todos, task_number):
    try:
        removed_task = todos.pop(task_number - 1)
        save_todos(todos)
        print(f"Task '{removed_task}' removed!")
    except IndexError:
        print("Invalid task number!")


def main():
    todos = load_todos()

    while True:
        print("\n1. Show To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_todos(todos)
        elif choice == "2":
            task = input("Enter task description: ")
            add_task(todos, task)
        elif choice == "3":
            display_todos(todos)
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(todos, task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
