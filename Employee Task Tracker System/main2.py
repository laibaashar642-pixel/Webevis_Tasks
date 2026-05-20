# Employee Task Tracker System

Employees = {}

# Add employee
def add_employee(employee_name):
    if employee_name not in Employees:
        Employees[employee_name] = []
        print(f"{employee_name} added successfully")
    else:
        print("Employee already exists")


# Assign task
def assign_task(employee_name, task_name):
    if employee_name in Employees:

        task = {
            "task_name": task_name,
            "status": "Pending"
        }

        Employees[employee_name].append(task)

        print(f"Task '{task_name}' assigned to {employee_name}")

    else:
        print("Employee not found")


# Complete task
def complete_task(employee_name, task_name):

    if employee_name in Employees:

        for task in Employees[employee_name]:

            if task["task_name"] == task_name:
                task["status"] = "Completed"

                print(f"Task '{task_name}' completed")
                return

        print("Task not found")

    else:
        print("Employee not found")


# Get all tasks of employee
def get_employee_tasks(employee_name):

    if employee_name in Employees:
        return Employees[employee_name]

    return "Employee not found"


# Get pending tasks only
def get_pending_tasks():

    pending_tasks = {}

    for employee_name, tasks in Employees.items():

        pending_list = []

        for task in tasks:

            if task["status"] == "Pending":
                pending_list.append(task)

        if pending_list:
            pending_tasks[employee_name] = pending_list

    return pending_tasks


# Testing

add_employee("Ali")
add_employee("Sara")

assign_task("Ali", "Design Website")
assign_task("Ali", "Fix Bugs")
assign_task("Sara", "Create API")

complete_task("Ali", "Fix Bugs")

print("\nAll Employee Tasks:")
print(Employees)

print("\nAli Tasks:")
print(get_employee_tasks("Ali"))

print("\nPending Tasks:")
print(get_pending_tasks())