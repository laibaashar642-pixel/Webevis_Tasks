Employees={}
def add_employee(employee_name):
    if employee_name not in Employees:
        Employees[employee_name]=[]
        print(f"{employee_name}added successfully")
        
    else:
        print("Employee Already Exists")
def assign_task(employee_name,task_name):
    if task_name  in Employees:
        task={
            'task_name':'Login_System',
            'status':'Pending',
        }
    Employees[employee_name].append('task')
    print(f"Task'{task_name}' assigned to'{employee_name}")
    else:
    print("Employee Not Found")
def complete_task(employee_name,task_name):
    if employee_name in Employees:
        for task in Employees[employee_name]:
          if task["task_name"]==task_name:
               task["status"]="Completed"
               print(f"Task'{task_name}'completed")
               return
          print("task Not Found")
        else:
            print("Employee Not Found")
def get_employee_tasks(employee_name):
    if employee_name in Employees:
        return Employees[employee_name]
    return "Employee Not Found"
def get_pending_tasks():
    pending_tasks=[]
    for employee_name,tasks in Employees.items():
        pending_lists=[]
        for task in tasks:
            if task["status"]=="Pending":
                pending_lists.append(task)
                if pending_lists:
                    pending_tasks[employee_name]=pending_lists
                    return pending_tasks
add_employee("Ahmad")
add_employee("Laiba")
add_employee("Ashar")
assign_task("Ahmad","Designing")
assign_task("Ashar","Fix Bugs")
assign_task("Laiba","Frontend")
complete_task("Laiba","Frontend")
print("\n All Employees task")
print("\n Ahamd Task")
print(get_employee_tasks("Ahmad"))
print("\n Pending Tasks")
print(get_pending_tasks())