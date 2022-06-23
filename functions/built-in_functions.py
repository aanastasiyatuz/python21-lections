"==============Build-in functions================="


"lambda" # анониимная функция
# lambda параметры: что функция возвращает
add = lambda a, b: a + b
print(add(5,4)) # 9

"map" # фунция, которая принимает первым аргументом функцию, вторым итерируемый обьект. map возвращает генератор, в котором все элементы - результат принимаемой функции, в которую мы передали элемент из последовательности

map_gen = map(int, ["1", "2", "3", "4"])
print(map_gen) # <map object>
print(list(map_gen))

# map(int, ["1", "2", "3", "4"])
# int("1") -> 1
# int("2") -> 2
# int("3") -> 3
# int("4") -> 4
# list( map(int, ["1", "2", "3", "4"]) ) -> [1, 2, 3, 4]

res = list( map(lambda a: a + 1, [1,2,3,4,5]) )
print(res) # [2,3,4,5,6]

"=====map на цикле for======"
func = lambda e: e + 1
# def func(e):
#      return e + 1
res = []

for e in [1,2,3,4,5]:
    res.append(func(e))
print(res) # [2,3,4,5,6]




"filter" # функция, которая возвращает генератор, принимает функцию и итерируемый обьект. результат будет последовательность из елементов итерируемого обьекта, которые прошли фильтр (проверку)

list_ = ["Эртай", "Оомат", "Арген", "Манас", "Бекзат", "Даниэль", "Эркайым"]

def startswith_vowels(name):
    vowels = 'УЕЁЫАОЭЯИЮEYUOAI'
    return name.upper().startswith(tuple(vowels))

res = list( filter(startswith_vowels, list_) )
print(res) # ['Эртай', 'Оомат', 'Арген', 'Эркайым']

vowels = 'УЕЁЫАОЭЯИЮEYUOAI'
res = list( filter(lambda name: name.upper().startswith(tuple(vowels)), list_) )
print(res) # ['Эртай', 'Оомат', 'Арген', 'Эркайым']

"=====filter на цикле for======"
def startswith_vowels(name):
    vowels = 'УЕЁЫАОЭЯИЮEYUOAI'
    return name.upper().startswith(tuple(vowels))

list_ = ["Эртай", "Оомат", "Арген", "Манас", "Бекзат", "Даниэль", "Эркайым"]

res = []
for name in list_:
    if startswith_vowels(name):
        res.append(name)
print(res) # ["Эртай", "Оомат", "Арген", "Эркайым"]


"reduce" # нужно импортировать из библеотеки functools
# эта функция принимает функцию и итерируемый обьект и возвращает 1 результат

from functools import reduce

list_ = [1,2,3,4,5,6,7,8,9]

def mul(a, b):
    return a * b

res = reduce(mul, list_)
print(res)

"============Reduce на цикле for=============="
list_ = [1,2,3,4,5,6,7,8,9]

def mul(a, b):
    return a * b

res = list_[0]
for b in list_[1:]:
    res = mul(res, b)
print(res)


"enumerate" # функция, которая принимает последовательность. возвращает генератор, в котором каждый элемент - tuple состоящий из числа и элемента из последовательности
# (enumerate - нумерует элементы (по дефолту начиная с 0))

list_ = ['a', 'b', 'c', 'd']

for i in enumerate(list_):
    print(i)
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')

for index, elem in enumerate(list_):
    print("index -", index, " : ", "elem -", elem)
# index - 0  :  elem - a
# index - 1  :  elem - b
# index - 2  :  elem - c
# index - 3  :  elem - d

for i in enumerate(list_[1:]):
    print(i)
# (0, 'b')
# (1, 'c')
# (2, 'd')

for i in enumerate(list_[1:], 10):
    print(i)
# (10, 'b')
# (11, 'c')
# (12, 'd')


"zip" # содединяет последовательности
list1 = [1, 2, 3, 4, 5, 6]
list2 = ["a", "b", "c", "d", "e", "f"]
print(zip(list1, list2)) # <zip object>
print(list(zip(list1, list2)))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f')]
print(dict(zip(list1, list2)))
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}

list1 = [1, 2, 3, 4, 5, 6]
list2 = ["a", "b", "c"]
print(list(zip(list1, list2)))
# [(1, 'a'), (2, 'b'), (3, 'c')]

list1 = [1, 2, 3, 4, 5, 6]
list2 = ["a", "b", "c", "d", "e", "f"]
list3 = [1.9, 2.7, 3.0, 4.5]
print(list(zip(list1, list2, list3)))
# [(1, 'a', 1.9), (2, 'b', 2.7), (3, 'c', 3.0), (4, 'd', 4.5)]

list1 = [1, 2, 3, 4, 5, 6]
list2 = ["a", "b", "c", "d", "e", "f"]
list3 = [1.9, 2.7, 3.0, 4.5]
list4 = [(1,2), (3,4)]
print(list(zip(list1, list2, list3, list4)))
# [(1, 'a', 1.9, (1, 2)), (2, 'b', 2.7, (3, 4))]
