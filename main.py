tasks = []


def addTask():
  task = input("please enter a task: ")
  tasks.append(task)
  print(f"Task '{task}' added to the list.")


def listTasks():
  if not tasks:
    print("There are no tasks currently.")
  else:
    print("Current Tasks:")
    for index, task in enumerate(tasks):
      print(f"task # {index}. {task}")

      ### Task #1. grocery


def deleteTask():
  listTasks()
  try:
    taskToDelete = int(input("Enter the # number to delete:"))
    if taskToDelete >= 0 and taskToDelete < len(tasks):
      tasks.pop(taskToDelete)
      print(f"Task {taskToDelete} has been removed.")
    else:
      print(f"Task #{taskToDelete} was not found.")
  except ValueError:
    print("Invalid input.")


if __name__ == "__main__":  #main function
  # create a loop to run the app
  print("Welcome to the To Do List app:)")
while True:
  print("\n")
  print("Please select one of the following one options")
  print("----------------------------------------------")
  print("1. Add a new task")
  print("2. Remove a task")
  print("3. View all tasks")
  print("4. Exit")

  choice = input("Enter your choice:")

  if (choice == "1"):
    addTask()
  elif (choice == "2"):
    deleteTask()
  elif (choice == "3"):
    listTasks()
  elif (choice == "4"):
    break
  else:
    print("Invalid input.Please try again.")

  print("GoodBye👋👋")
