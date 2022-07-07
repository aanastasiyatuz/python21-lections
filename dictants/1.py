"""
Создать список из чисел в диапазоне от 1 до 10
"""
# 1.
list1 = [1,2,3,4,5,6,7,8,9,10]
# 2.
list1 = list(range(1,11))
# 3.
list1 = [*range(1,11)]
# 4.
list1 = [i for i in range(1,11)]
# 5.
list1 = []
for i in range(1,11):
    list1.append(i)
# 6.
string1 = '1 2 3 4 5 6 7 8 9 10'
list1 = list( map(int, string1.split()) )


"""
Найти сумму всех чисел в списке
"""
# 1.
list_sum = sum(list1)
# 2.
from functools import reduce
list_sum = reduce( lambda x,y: x+y, list1 )
# 3.
list_sum = 0
for i in list1:
    list_sum = list_sum + i
    # list_sum += i


"""
Запросите число у пользователя
"""
num = int(input("Введите число: "))


"""
Найти остаток от деления суммы на число
"""
# 1
remainder = list_sum % num
# 2
div, remainder = divmod(list_sum, num)


"""
В список добавить по индексу 2 число 11
"""
# 1
list1.insert(2, 11)
# 2
list1 = list1[:2] + [11] + list1[2:]
# 3
new_list = []
index = 0
for i in list1:
    if index == 2:
        new_list.append(11)
    new_list.append(i)
    index += 1


"""
Заменить значение в списке под индексом 5 на строку "hello"
"""
# 1
list1[5] = 'hello'
# 2
list1.pop(5)
list1.insert(5, 'hello')
# 3
list1 = list1[:5] + ['hello'] + list1[6:]
# 4
class MyList(list):
    def change(self, index, value):
        self[index] = value
list1 = MyList(list1)
list1.change(5, 'hello')


"""
Поднять в верхний регистр строку в списке
"""
# 1
upper_string = list1[5].upper()
# 2
upper_string = ''
for i in list1:
    if type(i) == str:
        upper_string = i.upper()
# 3
class MyList(list):
    def get(self, index, default=None):
        try:
            return self[index]
        except:
            return default
list1 = MyList(list1)
upper_string = list1.get(5, '').upper()
# 4
strings = list( filter( lambda x: type(x) == str, list1) )
upper_strings = [s.upper() for s in strings]


"""
Создайте список с числами от 1 до 5 в виде строк
"""
# 1
list2 = ["1", "2", "3", "4", "5"]
# 2
list2 = "1 2 3 4 5".split()
# 3
list2 = list("12345")
# 4
list2 = list( map( str, range(1,6) ) )
# 5
list2 = list( map( lambda x: str(x), range(1,6) ) )
# 6
list2 = [str(i) for i in range(1,6)]
# 7
list2 = []
for i in range(1,6):
    list2.append(str(i))

"""
Переведите каждый элемент в списке в число
"""
# 1
list3 = [1,2,3,4,5]
# 2
list3 = [int(i) for i in list2]
# 3
list3 = list( map( int, list2 ) )
# 4
list3 = []
for i in list2:
    list3.append(int(i))


"""
Создайте класс Person с аттрибутами класса arms=2, legs=2 и аттрибутом обьекта name
"""
# 1
class Person:
    arms = 2
    legs = 2

    def __init__(self, name):
        self.name = name
"""
Создайте обьект от класса со своим именем
"""
obj = Person("Настя")

# 2
class Person:
    arms = 2
    legs = 2
    name = None 

obj = Person()
obj.name = "Настя"
