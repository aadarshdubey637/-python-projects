def task():
    task=[] #empty list
    print("<-----WELCOME TO THE TASK MANAGEMENT AAP----->")

    total_task=int(input("Enter how many task you want to add =")) #4
    for i in range(1,total_task+1): # user input 4 loop run 5 time 
        task_name=input(f"Enter task {i} = ")
        task.append(task_name)

    print(f"Today task are\n{task}")

    while True:
        opreration=int(input("Enter 1-Add\n2-update\n3-Delete\n4-View\n5-Exit/stop."))
        if opreration==1:
            add=input("Enter task you want to add = ")
            task.append(add)
            print(f"Task {add} has been successfully added..")

        elif opreration ==2:
            update_val=input("Enter the task name you want to update = ")
            if update_val in task:
                up=input("Enter new task = ")
                ind=task.index(update_val)
                task[ind]=up
                print(f"Update task {up}")
        elif opreration == 3:
            del_val=input("Whic task you want to delete = ")
            if del_val in task:
                ind=task.index(del_val)
                del task[ind]
                print(f"Task {del_val} has been deleted...")

        elif opreration == 4:
            print(f"Total Task = {task}")

        elif opreration == 5:
            print("Closing the program.THANKYOU ")
            break
        else:
            print("invalid input ")            
task()
    
