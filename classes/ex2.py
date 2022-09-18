class Employee:
    #constructor
    def __init__(self, name , desig, dept, salary, skills=None ):
        self.name = name
        self.designation = desig
        self.department = dept
        self.salary = salary
        self.skills = skills

    def do_task(self,task):
        print(f"Employee {self.name}.is doing task:{task}")

    def info(self):
        print("Employee Details")
        print(f"Name:{self.name}")
        print(f"Department:{self.department}")
        print(f"Designation:{self.designation}")
        print(f"salary:{','.join(self.skills)}")
    
    def add_skill(self,skillname):
        if self.skills is None:
            self.skill=[skillname]
        else:
            self.skills.append(skillname)

e1 = Employee("Raj","Assistant 2","Sales", 40000 ,["talking"])
e2 = Employee("sonu","staff officer","finance",70000,["management","leadreship"])

e1.info()
e2.info()
e1.do_task("Make some sales")
e2.do_task("Make coffee")
e1.add_skill("python programing")

e1.info()







    