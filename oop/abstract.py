"=================Абстракция====================="
# абстракция - принцип ООП, в котором создается абстрактный класс (класс - пустышка), в котором задаются названия аттрибутов и методов, для того, чтобы в дочерних классах переопределить их нужным образом. от абстрактных классов мы не создаем объектов, потому что в них есть только названия и нет логики

from abc import ABC, abstractmethod, abstractproperty

class AbstractAnimal(ABC):
    @abstractmethod
    def voice(self):
        ...
    
    @abstractproperty
    def legs(self):
        ...

# obj = AbstractAnimal() # TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs, voice

class Dog(AbstractAnimal):
    ...

# obj = Dog() # TypeError: Can't instantiate abstract class Dog with abstract methods legs, voice

class Dog(AbstractAnimal):
    def voice(self):
        print("гав-гав")

# obj = Dog() # TypeError: Can't instantiate abstract class Dog with abstract methods legs

class Dog(AbstractAnimal):
    legs = 4

    def voice(self):
        print("гав-гав")

class Cat(AbstractAnimal):
    legs = 4

    def voice(self):
        print("мяу-мяу")

dog1 = Dog()
dog1.voice() # гав-гав

cat1 = Cat()
cat1.legs # 4
