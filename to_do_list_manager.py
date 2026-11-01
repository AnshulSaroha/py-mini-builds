#to-do list manager
#this program stores,views,removes the task from a to-do list

#list for storing tasks
tasks =[]
completed_tasks =[]

def add_task():
#adding a task
        add_task =input("Enter task: ")
        tasks.append(add_task)
        print("Task added")
        print()

def view_task():
    #viewing the list
    print("Your tasks: ")
    for index,task in enumerate(tasks,start=1):
        print(f"{index}. {task}")
    print()

def remove_task():
    task_number = int(input("Enter task number to mark as done: "))
    #validating user input
    if (task_number>0) and task_number<= len(tasks):
        task_removed = tasks.pop(task_number-1)
        completed_tasks.append(task_removed)
        print(f"\"{task_removed}\" done and removed!")
        print()
    else:
        print("Invalid Input! retry with correct input")
        print()

def show_completed_tasK():
    #viewing completed task
    print("Your completed tasks: ")
    for index,task in enumerate(completed_tasks,start=1):
        print(f"{index}. {task}")
    print()

def quit():
    #quit the program
    print("ThankYou See You Soon!!!")
    print()
    
#running the program until user quits
while True:
    #user choice menu
    print("-"*3,"To-Do List Manager","-"*3)
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark task as done")
    print("4. View completed tasks")
    print("5. Quit")
    user_choice = int(input("Choose an option: "))
    print()

    #Selecting a option
    if(user_choice==1):
        add_task()
    elif(user_choice==2):
        view_task()
    elif(user_choice==3):
       remove_task()
    elif(user_choice==4):
        show_completed_tasK()
    elif(user_choice==5):
       quit()
       break
    else:
        print("Invalid Input! Try Again from Options 1-4")
        print()
