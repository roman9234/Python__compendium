from abc import ABC, abstractmethod
class Pet:
    _type = None
    def __init__(self, name, age, sex):
        self._name = name
        self._age = age
        self._sex = sex

    @abstractmethod
    def get_info(self):
        pass

class Dog(Pet):
    _type = "dog"

    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self._breed = breed

    def woof(self):
        print("woof")

    def get_info(self):
        print(f"A {self._type} named {self._name} at the age of {self._age} which is a {self._sex}, breed - {self._breed}")

class Cat(Pet):
    _type = "cat"
    def __init__(self, name, age, sex, color):
        super().__init__(name, age, sex)
        self._color = color

    def meow(self):
        print("meow")

    def get_info(self):
        print(f"A {self._type} named {self._name} at the age of {self._age} which is a {self._sex}, color - {self._color}")


cat1 = Cat("Tom", 7, "male", "grey")
cat1.meow()
cat1.get_info()

dog1 = Dog("Akira", 5, "female", "Labrador Retriever")
dog1.woof()
dog1.get_info()