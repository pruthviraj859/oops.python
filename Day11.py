class Person:
    def __init__(self, name, emp_id):
        self.name=name
        self.emp_id=emp_id

class Manager(Person):
    def __init__(self, name, emp_id, department):
        super().__init__(name,emp_id)
        self.department=department

    def get_profile_data(self):
        return f'{self.name} (ID: {self.emp_id}) is a manager of {self.department} department.'

class Engineer(Person):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name,emp_id)
        self.specialization=specialization

    def get_profile_data(self):
        if len(self.specialization)>1:
            self.name1= self.specialization[0].lower() + self.specialization[1:]
            return f'{self.name} (ID: {self.emp_id}) is a {self.name1} engineer.'
        else: 
            return f'{self.name} (ID: {self.emp_id}) is a {self.specialization} engineer.'

m1 = Manager("Kavita", 101, "HR")
print( m1.get_profile_data())

e1 = Engineer("Ravi", 102, "Software")
print( e1.get_profile_data())
############################################################################################################################
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name,age)
        self.grade=grade

    def get_details(self):
        return f'{self.name} is {self.age} years old and studies in {self.grade} grade.'

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name,age)
        self.subject=subject

    def get_details(self):
        return f'{self.name} is {self.age} years old and teaches {self.subject}.'

s1 = Student("Asha", 15, "10th")
print( s1.get_details())
###############################################################################################################################
class Vehicle:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand,model)
        self.doors=doors

    def description(self):
        return f'{self.brand} {self.model} with {self.doors} doors.'

class Bike(Vehicle):
    def __init__(self, brand, model, engine):
        super().__init__(brand,model)
        self.engine=engine

    def description(self):
        return f'{self.brand} {self.model} with {self.engine} engine.'

c1 = Car("Toyota", "Camry", 4)
print( c1.description())
