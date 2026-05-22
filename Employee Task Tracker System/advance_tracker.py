#Main Logic  firstly we need to understand whether manager exists or not check employee exists or not check duplicate task check task record  add into employee taask so actual implementation made data stored in the form of dictionary tasks move through  functions or if else structure functions make checking by using if else structure
Employees={
   "Umair":{"Role":"Manager",
            "Tasks":[]},
   "Laiba":{"Role":"Employee",
            "Tasks":[]},
   "Ashar":{"Role":"Employee",
            "Tasks":[]},
   "Zainab":{"Role":"Employee",
            "Tasks":[]},
   "Sana":{"Role":"Employee",
            "Tasks":[]},
   "Zain":{"Role":"Employee",
            "Tasks":[]},
   "Mahnoor":{"Role":"HR",
              "Tasks":[]},
   "Kajal":{"Role":"Employee",
            "Tasks":[]},
   "Sadeeq":{"Role":"Supervisor",
             "Tasks":[]},
}

#Actual Implementation is Assigning Task System Where the logic starts here Assigning Task System

Tasks=["Designing","Testing","Documentation","Deployment"]

#Adding Functions
def add_employee(name,role):
    if name in Employees:
       print("Employee Already Exists")
    
    else:
        Employees[name]={"Role": role, "Tasks": []}
        print(f"Employee '{name}' added successfully")
def assign_task(manager_name,employee_name,task_name):
    if manager_name not in Employees:
     print("Manager Not Exists")
     return
    if Employees[manager_name]["Role"] != "Manager":
     print("Only Manager Can Assign Tasks")
     return
    if employee_name not in Employees:
        print("Employee Not Exists")
        return
    if manager_name==employee_name:
       print("Manager Cannot Assign Task To Themselves")
       return
   
    if task_name not in Tasks:
       print("Invalid Task")
       return
    
    for task in Employees[employee_name]["Tasks"]:
     if task["task_name"] == task_name:
            print("Task already assigned")
            return

   

    Employees[employee_name]["Tasks"].append(
       {"task_name": task_name, "Status": "Pending"})
    print(f"Task '{task_name}' assigned to {employee_name}")


# Testing the implementation
add_employee("Ali", "Employee")
assign_task("Umair", "Ali", "Designing")

print(Employees["Ali"]["Tasks"])





