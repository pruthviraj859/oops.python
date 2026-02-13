class Person:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name


class Faculty(Person):
    def __init__(self, subject, **kwargs):
        super().__init__(**kwargs)
        self.subject = subject

    def teach(self):
        pass


class Staff(Person):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department

    def work(self):
        pass


class Administrator(Faculty, Staff):
    def __init__(self, name, subject, department):
        super().__init__(name=name, subject=subject, department=department)

    def profile_data(self):
        return f'{self.name} teaches {self.subject} and works in {self.department} department.'


a1 = Administrator("Rakesh", "Math", "Operations")
print(a1.profile_data())

###############################################################################################################################3333
class User:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name


class Driver(User):
    def __init__(self, car, **kwargs):
        super().__init__(**kwargs)
        self.car = car


class Rider(User):
    def __init__(self, pickup_location, **kwargs):
        super().__init__(**kwargs)
        self.pickup_location = pickup_location


class Trip(Driver, Rider):
    def __init__(self, name, car, pickup_location):
        super().__init__(
            name=name,
            car=car,
            pickup_location=pickup_location
        )

    def summary(self):
        return f'{self.name} will pick up the rider from {self.pickup_location} using {self.car}.'


t1 = Trip("Amit", "Honda City", "Sector 21")
print(t1.summary())
##########################################################################################################################
class Device:
    def __init__(self, brand):
        self.brand=brand

class VoiceControl(Device):
    def __init__(self,brand):
        super().__init__(brand)
    
    def voice_activate(self):
        pass

class AppControl(Device):
    def __init__(self,brand):
        super().__init__(brand)
    
    def app_activate(self):
        pass

class SmartSpeaker(VoiceControl, AppControl):
    def __init__(self,brand):
        VoiceControl.__init__(self,brand)
        AppControl.__init__(self,brand)
    
    def control_methods(self):
        return f'{self.brand} can be controlled via voice and app.'

s1 = SmartSpeaker("Echo")
print( s1.control_methods())
