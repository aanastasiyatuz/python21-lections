"================OOP==================="
# OOP - Object-oriented programming 
# ООП - обьектно-ориентированное программирование (парадигма)

class Person:
    name = "Настя"
    age = 12
    arms = 2
    legs = 2

    def walk(arg):
        print(arg)
        print("я иду")
    
    def add_age(self):
        self.age += 1

# person1 = Person()
# person1.add_age() # Новый вариант
# # Person.add_age(person1) # Старый вариант
# print(person1.age)

# Person.age = 17
# print(Person.age)

# person2 = Person()
# print(person2.age)


class Person:
    arms = 2
    legs = 2

    def __init__(self, name, age):
        """
        функция, которая вызывается, когда мы создаем обьект от класса
        self - ссылка на созданный обьект
        """
        self.name = name # мы добавляем в обьект self новый аттрибут name
        self.age = age # новый аттрибут age

    def add_age(self):
        """
        функция, которая принимает обьект и изменяет его возраст на 1
        """
        self.age += 1

    def __str__(self):
        """
        функция, которая вызывается, когда мы оборачиваем обьект в класс str или когда принтуем обьект
        функция __str__ ничего кроме self не принимает и обязательно должна возвращать строку
        """
        return f"{self.name} - {self.age} y.o"

person1 = Person("Настя", 50)
print(person1)

person2 = Person("Жаркынай", 15)
print(person2)


"===================Аттрибуты класса======================="
# аттрибуты класса - переменные внутри класса

"====================Методы класса========================="
# методы класса - функции внутри класса

"====================Обьекты класса======================"
# обьект, экземпляр, instance класса - обьект созданный по шаблону класса (он перенимает все аттрибуты и методы у класса)

"===============Аттрибуты и методы обекта=================="
# аттрибуты и методы, которые есть у обьекта, но возможно их нет у класса

class A:
    var1 = "переменная класса"

    def __init__(self):
        self.var2 = "переменная обьекта"

print(dir(A))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1']

obj = A()
print(dir(obj))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__var1', '__subclasshook__', '__weakref__', 'var1', 'var2']

print(A.var1)  # 'переменная класса'
# print(A.var2)  # AttributeError: type object 'A' has no attribute 'var2'

print(obj.var1) # 'переменная класса'
print(obj.var2) # 'переменная обьекта'

"Класс имеет доступ только к аттрибутам класса"
"Обьект имеет доступ и к аттрибутам класса, и к его аттрибутам"