class Camera:
    def __init__(self, camera_quality): 
        self.camera_quality = camera_quality

    def display_camera_details(self):
        print("Camera Quality:", self.camera_quality)


class MusicPlayer:
    def __init__(self, sound_quality):
        self.sound_quality = sound_quality

    def display_music_details(self):
        print("Sound Quality:", self.sound_quality)


class SmartPhone(Camera, MusicPlayer):
    def __init__(self, brand, camera_quality, sound_quality):
        self.brand = brand
        Camera.__init__(self, camera_quality)
        MusicPlayer.__init__(self, sound_quality)

    def display_smartphone_details(self):
        print("Brand:", self.brand)


# Creating object
phone = SmartPhone("Samsung", "108MP", "Dolby Atmos")

# Displaying details
phone.display_smartphone_details()
phone.display_camera_details()
phone.display_music_details()
class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display_product(self):
        print("Product Name:", self.product_name)
        print("Price:", self.price)


class ElectronicProduct(Product):
    def __init__(self, product_name, price, brand, warranty):
        super().__init__(product_name, price)
        self.brand = brand
        self.warranty = warranty

    def display_electronic_product(self):
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)


class MobilePhone(ElectronicProduct):
    def __init__(self, product_name, price, brand, warranty, ram, storage):
        super().__init__(product_name, price, brand, warranty)
        self.ram = ram
        self.storage = storage

    def display_mobile_details(self):
        print("RAM:", self.ram)
        print("Storage:", self.storage)


# Creating object
mobile = MobilePhone("iPhone 15", 80000, "Apple", "1 Year", "8GB", "256GB")

# Displaying all details
mobile.display_product()
mobile.display_electronic_product()
mobile.display_mobile_details()
