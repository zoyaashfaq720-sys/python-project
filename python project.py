
task = []
while True:
    print("========================\n\tTO-DO LIST\t\n========================\n")
    print("1-Add Task\n2-View Task\n3-Remove Task\n4-Exit\n")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        
        my_task = input("Enter Your task : ")
        print("Task added successfully! \n")
        task.append(my_task)
    elif choice == 2:
        print(task)
    elif choice == 3:
        remove_task = input("Which task do you want to remove? ")
        task.remove(remove_task)
        print("Task removed successfully!")
    elif choice == 4:
        break
    else:
        print("Invalid choice!")
        
