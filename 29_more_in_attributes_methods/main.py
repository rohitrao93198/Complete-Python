# class Animal:
#     gender = "Male"  # class attribute

#     def __init__(self, name, age):
#         self.name = name  # instance attribute
#         self.age = age  # instance attribute

#     def info(self):  # instance method
#         print("This is a method")

#     @classmethod
#     def clmethod(cls):  # class method
#         print(f"{cls.gender} is your gender")

#     @staticmethod
#     def hello():  # static method
#         print("hello i am a static method")


# obj = Animal("Lion", 10)

# obj.info()

# obj.clmethod()

# obj.hello()


"""*******  Question   ***********"""

# Student registration system ask for name, age, number, blood group and register 3 students


class Registration:
    def __init__(self, name, age, number, blood):
        self.name = name
        self.age = age
        self.number = number
        self.blood = blood

    def show(self):
        print(
            f"hello your name is {self.name}\nyour age is {self.age}\nyour number is {self.number}\nyou bollod group is {self.blood}"
        )


student1 = Registration("Rohit", 22, 7878363535, "B+")
student2 = Registration("Neeraj", 27, 7878367635, "A+")
student3 = Registration("Vipin", 29, 7878363900, "O+")

student1.show()
student2.show()
