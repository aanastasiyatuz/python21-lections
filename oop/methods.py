"==================Class, static, instance methods===================="
# instance метод (метод обьекта) - метод, который принимает первым аргументом self (обьект). Вызываем instance методы у обьекта

class A:
    def instance_method(self):
        print("метод обьекта")

obj_a = A()
obj_a.instance_method() # вызываем у обьекта, и он автоматически попадает как аргумент в метод
A.instance_method(obj_a) # вызываем у класса, нужно передать обьект


# class methods (методы класса) - метод, который принимает первым аргументом cls (класс). чтобы создать метод класса, нужно метод задекорировать classmethod.

class A:
    @classmethod
    def class_method(cls):
        print(cls)
        print("Метод класса")

A.class_method()
A().class_method()

class Pizza:
    def __init__(self, radius, *ingredients):
        self.ingredients = ingredients
        self.r = radius

    def cook(self):
        print(f"Пицца размером {self.r} см\nИнгредиенты:\n{self.ingredients}")

    @classmethod
    def pepperoni(cls, r):
        return cls(r, "Пепперони", "Помидоры")

    @classmethod
    def four_cheeze(cls, r):
        return cls(r, "Моцарелла", "Дор блю", "Еще сыр", "И еще сыр")

pizza1 = Pizza(30, "сыр", "помидоры", "грибы")
pizza2 = Pizza.pepperoni(30)
pizza3 = Pizza.pepperoni(35)
pizza4 = Pizza.four_cheeze(25)
pizza5 = Pizza.four_cheeze(40)

pizzas = [pizza1, pizza2, pizza3, pizza4, pizza5]
for pizza in pizzas:
    pizza.cook()



# static методы - просто функции внутри класса, которые не взамодействуют ни с классом, ни с обектом

class Square:
    def __init__(self, a):
        self.a = a
        self.s = self.get_s(a)
    
    @staticmethod
    def get_s(a):
        return a ** 2

obj = Square(4)
print(obj.s)

