class Book:
    def read_page(self, page):
        return f'Reading page {page}'

class BatteryPowered:
    def battery_status(self, level):
        return f'Battery at {level}%'

class EBookReader(Book, BatteryPowered):
    pass

e1 = EBookReader()
print( e1.read_page(10))
#############################################################################
class Flyer:
    def fly(self, height):
        return f'Flying at {height} meters'

class Camera:
    def take_photo(self, location):
        return f'Photo taken at {location}'

class Drone(Flyer, Camera):
    pass

d1 = Drone()
print( d1.fly(50))
############################################################################3
class Developer:
    def code(self):
        return f'{self.name} is coding'

class Designer:
    def design(self):
        return f'{self.name} is designing'

class HybridWorker(Developer, Designer):
    def __init__(self, name):
        self.name=name

h1 = HybridWorker("Ava")
print( h1.code())
