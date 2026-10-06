
# Multiple inheritance without constructor.
class camera:
    def take_photo(self):
        print("camera: Taking a photo")
class Musicplayer:
    def play_music(self):
        print("Music player: playing music")
class Smartphone(camera,Musicplayer):
    def make_call(self):
        print("Smartphone :Making a call")
s=Smartphone()
s.take_photo()
s.play_music()
s.make_call()
# ------------------------------------------------------------------
print("--------person Details----------")
# Multiple inheritance with Constructor.
class person:
    def __init__(self,name):
        self.name = name
    def display_name(self):
        print("Name:",self.name)
class Address:
    def __init__(self,city):
        self.city = city
    def display_city(self):
        print("City:",self.city)
class Employee(person,Address):
    def __init__(self,name,city):
        person.__init__(self,name)
        Address.__init__(self,city)
e = Employee("Teja","Hyderabad")
e.display_name()
e.display_city()
# ----------------------------------------------------------------
print("-----------Teachers subject---------")
# Multiple inheritance with constructor + super().
class Teacher:
    def __init__(self,subject):
        self.subject = subject
    def display_subject(self):
        print("Subject:",self.subject)
class Researcher:
    def __init__(self,research):
        self.research = research
    def display_research(self):
        print("Research Area:",self.research)
class Professor(Teacher,Researcher):
    def __init__(self,subject,research):
        Teacher.__init__(self,subject)
        Researcher.__init__(self,research)
        self.subject = subject
        self.research = research
p=Professor("python","Artificial Intelligence")
p.display_subject()
p.display_research()
# -------------------------------------------------------------
print("------Electric car----------")
# Multiple inheritance with constructor + super().Real world Example.
class Engine:
    def __init__(self,engine_type):
        self.engine_type = engine_type
class Battery:
    def __init__(self,battery_capacity):
        self.battery_capacity = battery_capacity
class ElectricCar(Engine,Battery):
    def __init__(self,engine_type,battery_capacity):
        Engine.__init__(self,engine_type)
        Battery.__init__(self,battery_capacity)
    def display_details(self):
        print("Engine Type :",self.engine_type)
        print("Battery Capacity:",self.battery_capacity,"KWh")
car =ElectricCar("Electric Motor ",75)
car.display_details()