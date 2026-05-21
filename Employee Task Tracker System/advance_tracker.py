#Main Logic  firstly we need to understand whether manager exists or not check employee exists or not check duplicate task check task record  add into employee taask so actual implementation made data stored in the form of dictionary tasks move through  functions or if else structure functions make checking by using if else structure
Employees={
   "Umair":{"Role":"Manager",
            "Task":"Designing"},
   "Laiba":{"Role":"Employee",
            "Task":"Development"},
   "Ashar":{"Role":"Employee",
            "Task":"Testing"},
   "Zainab":{"Role":"Employee",
            "Task":"Documentation"},
   "Sana":{"Role":"Employee",
            "Task":"Maintenance"},
   "Zain":{"Role":"Employee",
            "Task":"Support"},
   "Mahnoor":{"Role":"HR"},
   "Kajal":{"Role":"Employee"},
   "Sadeeq":{"Role":"Supervisor"},
}
name=input("Enter Employee Name:")
if name in Employees:
    print("Employee Exists")

    role_check = Employees[name]["Role"] == "Manager"

    if role_check:
        print("Manager Exists")
    else:
        print("Not a Manager")

else:
    print("Employee Not Exists")
#Actual Implementation is Assigning Task System Where the logic starts here Assigning Task System
task_name=input("Enter Task Name:")
if  Employees[name]["Task"]==task_name:
    print("Task Exists")
else:
    print("Task Not Exists")