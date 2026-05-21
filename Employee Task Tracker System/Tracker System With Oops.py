class Employee:
    Employee_Registry={}
    def __init__(self,employee_name):
         self.employee_name=employee_name
         self.tasks=[]

    def add_employee(self):
         if self.employee_name not in Employee.Employee_Registry:
            Employee.Employee_Registry[self.employee_name] = self
            print(f"Employee '{self.employee_name}'added successfully")
         else:
           print("Employee already exists")
    def assign_task(self,task_name):
        if self.employee_name in Employee.Employee_Registry:
           task={
            "task_name":task_name,
            "Status":"Pending"
        }
           self.tasks.append(task)
           print(f"Task '{task_name}' assigned to {self.employee_name}")
        else:
         print("Employee Not found")
    def complete_task (self,task_name):
         for task in self.tasks:
            if task["task_name"]==task_name:
                 task["Status"]="Completed"
                 print(f"Task '{task_name}'completed")
                 return
            else:
                 print("Task not found")
    def get_employee_tasks(self):
            if self.employee_name in Employee.Employee_Registry:
             return Employee.Employee_Registry[self.employee_name]
            return "Employee not found"
    def get_pending_tasks(self):
          pending_tasks=[]
          for self.employee_name,emp_object in Employee.Employee_Registry.items():
            for task in emp_object.tasks:
                if task["Status"]=="Pending":
                    pending_tasks.append({"employee":self.employee_name,"task_name":task["task_name"]})
          return pending_tasks

e1=Employee("Laiba")
e2=Employee("Ashar")
e3=Employee("Kajal")

print(e1.assign_task("Designing"))
print(e2.assign_task("Crafting"))
print(e3.assign_task("Testing"))
print(e1.complete_task("Designing"))
print(e2.complete_task("Crafting"))
print(e3.complete_task("Testing"))
print(e1.get_employee_tasks())
print(e2.get_employee_tasks())
print(e3.get_employee_tasks())
print(e1.get_pending_tasks())
print(e2.get_pending_tasks())
print(e3.get_pending_tasks())



#employee_registry = {}   ← sab employees yahan store honge
#Actual Logic Implementation
""" class Employee:
    __init__(self, employee_name)
        self.name = ?        ← tum bharo
        self.tasks = ?       ← tum bharo

    assign_task(self, task_name)
        self.tasks mein ?    ← task append karo

    complete_task(self, task_name)
        self.tasks mein ?    ← loop karo, status change karo

    get_my_tasks(self)
        return ?             ← self.tasks return karo """