class Student:
    def __init__(self, name, student_id):
        self.name=name
        self.student_id=student_id

class Graduate(Student):
    def __init__(self, name, student_id, degree):
        super().__init__(name,student_id)
        self.degree=degree

    def get_graduate_info(self):
        return f'{self.name} ({self.student_id}) - {self.degree}'


g1 = Graduate("Bob", "G001", "MBA")
print( g1.get_graduate_info())
################################################################################3
class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price

class DiscountedProduct(Product):
    def __init__(self, name, price, discount_percent):
        super().__init__(name,price)
        self.discount_percent=discount_percent

    def get_discounted_price(self):
        self.price-=(self.discount_percent/100)*self.price
        return self.price

p1 = DiscountedProduct("Phone", 10000, 10)
print( p1.get_discounted_price())
################################################################################
class Vehicle:
    def __init__(self, vehicle_type, speed):
        self.vehicle_type=vehicle_type
        self.speed=speed

class Flight(Vehicle):
    def __init__(self, vehicle_type, speed, flight_number, duration):
        super().__init__(vehicle_type,speed)
        self.flight_number=flight_number
        self.duration=duration

    def flight_summary(self):
        return f'Flight {self.flight_number} ({self.vehicle_type}) travels at {self.speed} km/h for {self.duration} hours'

f1 = Flight("Airbus", 700, "A123", 3)
print( f1.flight_summary())
