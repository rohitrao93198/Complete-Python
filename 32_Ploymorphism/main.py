"""Polymorphism --> The ability of an object to take on many forms. It allows us to use a single interface to represent different types of objects. In Python, polymorphism is achieved through method overriding and duck typing."""

"""Polymorphism ka matlab hota hai ki ek object kai tarah ke roop le sakta hai. Iska matlab hai ki hum ek hi interface ka use karke alag-alag types ke objects ko represent kar sakte hain. Python mein, polymorphism method overriding aur duck typing ke through achieve hota hai."""


# class Animal:
#     name = "Lion"

#     def speak(self):
#         print("Hello i roar")


# class Bird:
#     name = "Sparrow"

#     def speak(self):
#         print("Hello i tweet")


# obj = Animal()
# obj2 = Bird()

# obj.speak()
# obj2.speak()


# method overriding
class Animal:
    name = "Lion"

    def speak(self):
        print("hello i roar")


class Human(Animal):
    name = "Rohit"

    def speak(self):
        # super().speak()
        print("hello my name is rohit")


obj = Human()
obj.speak()
