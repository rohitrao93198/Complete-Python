"""Abstraction --> Hiding the internal details and showing only the functionality to the user.Abstraction is achieved through abstract classes and interfaces in Python."""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Hello i make woof sound")

    def hello(self):
        print("i am a dog")


obj = Dog()
obj.hello()
