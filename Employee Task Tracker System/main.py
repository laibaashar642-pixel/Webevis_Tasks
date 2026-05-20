Employees={}
def add_employee(employee_name):
    if employee_name not in Employees:
        Employees[employee_name]=[]
        print(f"Employee '{employee_name}'added successfully")
    else:
        print("Employee already exists")
def assign_task(employee_name,task_name):
    if employee_name in Employees:
        task={
            "task_name":task_name,
            "Status":"Pending"
        }
        Employees[employee_name].append(task)
        print(f"Task '{task_name}' assigned to {employee_name}")
    else:
        print("Employee not found")
def complete_task (employee_name,task_name):
    if employee_name in Employees:
        for task in Employees[employee_name]:
            if task["task_name"]==task_name:
                task["Status"]="Completed"
                print(f"Task '{task_name}'completed")
                return 
            print("Task not found")
        else:
            print("Employee not found")
def get_employee_tasks(employee_name):
    if employee_name in Employees:
        return Employees[employee_name]
    return "Employee not found"
def get_pending_tasks():
    pending_tasks=[]
    for employee in Employees:
        for task in Employees[employee]:
            if task["Status"]=="Pending":
                pending_tasks.append({"employee":employee,"task_name":task["task_name"]})
                return pending_tasks

add_employee("Alla")
add_employee("Ayesha")
add_employee("Laiba")
assign_task("Alla","Create a presentation")
assign_task("Ayesha","Create a SRS document")
assign_task("Laiba","Create a Report")
complete_task("Laiba","Create a Report")
print(get_employee_tasks("Alla"))
print(get_employee_tasks("Ayesha"))
print(get_employee_tasks("Laiba"))
print(get_pending_tasks())

