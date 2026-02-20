from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class square(Shape):
    def __init__(self,side):
        self.side =side
    def area(self):
        print('Area:',self.side*self.side)
s=square(4)
s.area()

from abc import ABC ,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    
    def sound(self):
        print('bow..boww')
        
class Cat(Animal):
    def sound(self):
        print('meow')
g=Dog()
g.sound()
c=Cat()
c.sound()


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(Vehicle):
    def start(self):
        print('car started')
class Bike(Vehicle):
    def start(self):
        print('Bike started')
        
c=car()
c.start()
b=Bike()
b.start()

class Bank(ABC):
    @abstractmethod
    def interest_rate(self):
        pass
class SBI(Bank):
    def interest_rate(self):
        print('interset rate 10%')
        
class HDFC(Bank):
    def interest_rate(self):
        print('interset rate 20%')
        
s=SBI()
s.interest_rate()
h=HDFC()
h.interest_rate()

        
class Employee (ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    
class FullTimeEmployee(Employee):
    def __init__(self,slary_hr,days):
        self.slary_hr=slary_hr
        self.days=days
        
    def calculate_salary(self):
        salary=self.slary_hr*12*days
        print(salary)

class PartTimeEmployee(Employee):
    def __init__(self,slary_hr,days):
        self.slary_hr=slary_hr
        self.days=days
        
    def calculate_salary(self):
        salary=self.slary_hr*4*self.days
        print(salary)
        
f=FullTimeEmployee(67,25)
f.calculate_salary()

f=PartTimeEmployee(23,45)
f.calculate_salary()
    

    
