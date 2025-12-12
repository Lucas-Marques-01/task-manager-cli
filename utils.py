import storage
def list_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    
    show_all = input("Do you want to see all tasks? (yes/no): ").lower()
    
    if show_all == "no":
        print("\nListing only pending tasks:\n")
        tasks = [task for task in tasks if task["status"] == "pending"]
    else:
        print("\nListing all tasks:\n")
    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Status: {task['status']}")
        print(f"Deadline: {task['deadline']}")
        print(f"Description: {task['description']}")
        print(f"Date Created: {task['date_created']}")
        print("-" * 20)