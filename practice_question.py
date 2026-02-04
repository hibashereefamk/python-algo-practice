# inheritencde example
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    pass

d = Dog()
d.sound()
# polymorphism(Method Overriding) example
class Cat(Animal):
    def sound(self):
        print("Cat meows")
class Cow(Animal):
    def sound(self):
        print("Cow moos")
c = Cat()
c.sound()
w = Cow()
w.sound()                                                                                                                   
# polymorphism(method overloading) example

class Math:
    def add(self, *args):
        return sum(args)

m = Math()
print(m.add(2, 3))
print(m.add(2, 3, 4))


class Bird:
    def fly(self):
        print("Bird can fly")

class Airplane:
    def fly(self):
        print("Airplane can fly")

def make_fly(obj):
    obj.fly()

make_fly(Bird())
make_fly(Airplane())

# polymorphism(Operator Overloading) example
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

n1 = Number(10)
n2 = Number(20)


print(n1 +n2)
# duck typeing example
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

a = Dog()
a.sound()

# encaputulisation example
class Bank:
    def __init__(self):
        self.__balance = 1000   # private

    def get_balance(self):
        return self.__balance
