print("TO DO LIST")
import json
confirm=input("Please confirm by using 1 if you have any available Json file or 2 for new file:")
path= input("Please enter the path of the json:")
if confirm=="1":
    try:
        with open(path, "r") as file:
            task = json.load(file)
    except:
        print("File not found or error in loading file, creating New file:")
        task= []
        with open(path, "w") as file:
            json.dump(task, file)

elif confirm=="2":
    #name=input("Please enter the name for the file:")
    task = []
    with open(path, "w") as file:
            json.dump(task, file)
while True:
    user= input("Press 1 to add task \n Press 2 to view task \n Press 3 to mark the task done \n Press 4 to delete the tasks \n Press 5 to edit \n Press 6 to save  \n Press 7 for exit:  ")
    if (user=="1"):
        while True:
            add= input("Please add the task here:")
            task.append({"task": add, "done": False})
            print(task)
            more= input("Want to add more:")
            if (more=="yes" or more=="Yes"):
                continue
            else:
                break
    
    
    elif (user=="2"):
        print(task)



    elif (user=="3"):
        print(task)
        dic= input("Please enter the number of the task: ")
        index= int(dic)-1
        if index >= 0 and index < len(task):
            task[index]["done"] = True
        else:
            print("INVALID NUMBER")


    elif (user=="4"):
        print(task)
        remove=input("Enter the number of the task that you want to remove: ")
        index2=int(remove)-1
        if index2>= 0 and index2 < len(task):
            task.pop(index2)
        else:
            print("InVALID INPUT")
        
    elif (user=="5"):
        print(task)
        edit=input("Enter the position of the task that you want to alter:")
        index3=int(edit)-1
        if index3 >=0 or index3< len(task):
            edit2=input("Please confirm 1 if you want to update/replace the current details or use 2 to  insert new value:")            
            replace=input("Insert the new value here:")
            if edit2=="1":
                task[index3]["task"]=replace
                print(task)
            if edit2=="2":
                task.insert(index3, {"task":replace,"done": False})
                print(task)
        else:
            print("INVALID")


    elif (user=="6"):
        with open(path, "w") as file:
            json.dump(task, file)
    
    elif (user=="7"):
        print("CHEERS!")
        break
    else:
        print("INVALID INPUT")