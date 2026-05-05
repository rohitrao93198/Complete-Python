"""Encapsulation --> Encapsulation is the process of hiding the internal details of an object and only exposing a public interface. It is one of the fundamental principles of object-oriented programming (OOP) and helps to protect the integrity of the data and prevent unauthorized access."""

"""Encapsulation ka matlab hai ki hum apne class ke andar ke details ko chhupa dete hain aur sirf ek public interface provide karte hain. Isse hum apne data ko protect kar sakte hain aur unauthorized access se bach sakte hain."""


class Animal:
    __name = "Lion"

    def speak(self):
        print("Hello I will roar")


class Human(Animal):
    def say(self):
        print(f"Hello my name is {super().name}")


obj = Human()
obj.say()
