import storage
import utils
import datetime

def menu_principal():
    while True:
        tasks = storage.load_tasks()
        user_choice = input("What's your next task? ").lower()
        
        
        if user_choice == "list":
            utils.list_tasks(tasks)
            
        elif user_choice == "add":
            new_task = {
                "id": max([task["id"] for task in tasks], default=0) + 1,
                "title": input("Enter task title: "),
                "status": "pending",
                "deadline": input("Enter task deadline: "),
                "description": input("Enter task description: "),
                "date_created": str(datetime.date.today())
            }
            tasks.append(new_task)
            storage.save_tasks(tasks)
            print("Task added successfully!")
            
        elif user_choice == "conclude":
            task_id = int(input("Enter the task ID to conclude: "))
            for task in tasks:
                if task["id"] == task_id:
                    task["status"] = "concluded"
                    storage.save_tasks(tasks)
                    print("Task concluded successfully!")
                    break
            else:
                print("Task ID not found.")

        elif user_choice == "remove":
            task_id = int(input("Enter the task ID to remove: "))
            tasks = [task for task in tasks if task["id"] != task_id]
            storage.save_tasks(tasks)
            print("Task removed successfully!")

        elif user_choice == "exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Please type a valid input")

menu_principal()



