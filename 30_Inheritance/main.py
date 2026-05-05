"""Inheritance --> child class parent class ki properties ko access kr skta hai, i simple worlds me agar hum ek class banate hai aur uske andar kuch properties define krte hai to hum us class ko as a parent class use kr skte hai aur uske child class bana skte hai jisme hum parent class ki properties ko access kr skte hai aur apne hisab se modify kr skte hai"""

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"your name is - {self.name} and your age is - {self.age}")


# class Human(Animal):
#     def __init__(self, name, age, number, city):
#         super().__init__(name, age)
#         self.number = number
#         self.city = city

#     def info(self):
#         print(
#             f"your name is - {self.name}, your age is - {self.age}, your no is - {self.number} and your city is - {self.city}"
#         )


# obj1 = Animal("Lion", 8)
# obj2 = Human("Rohit", 22, 8765432123, "rewari")

# obj1.info()
# obj2.info()


# multilevel inheritance
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"your name is - {self.name} and your age is - {self.age}")


# class Human(Animal):
#     def __init__(self, name, age, number, city):
#         super().__init__(name, age)
#         self.number = number
#         self.city = city


# class Robots(Human):
#     def __init__(self, name, age, number, city, imie):
#         super().__init__(name, age, number, city)
#         self.imei = self.imei


# multiple inheritance
# class Animal:
#     name = "lion"


# class Human:
#     name = "Rohit"


# class Robots(Animal, Human):
#     pass


# hireechale inheritance
# class Animal:
#     pass


# class Human(Animal):
#     pass


# class Robots(Animal):
#     pass
