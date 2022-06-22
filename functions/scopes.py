"================Области видимости и пространства имен=================="
locals()  # - возвращает словарь со всеми локальными переменными
globals()  # - возвращает словарь со всеми глобальными переменными

# LEGB - local, enclosed, global, build-in

"Build-in"  # - встроенное пространство имен (все втроенные переменные (print, input, sum, max, min, len, abs, int, str, dict ...))

"Global" # - глобальное пространство имен (все переменные внутри файла, которые создали мы) 
# чтобы узнать, что находится в глобальном пространстве, можно использовать функцию globals

"Enclosed" # - пространство находящееся между двумя пространствами

"Local" # - какое-то закрытое пространство

a = 10
d = 7

def func(b, c):
    # локальное пространство
    a = 5
    print(locals())
    # {'b': 5, 'c': 2, 'a': 5}
# func(5,2)

def func():
    # enclosed пространство
    a = "func"
    def inner_func():
        # local пространство
        a = "inner_func"
        print(locals()) # {'a': 'inner_func'}
    inner_func()
    print(locals()) # {'a': 'func', 'inner_func': <function func.<locals>.inner_func at 0x7fa171fa8d30>}

# func()

эртай = 'алиби'

def func():
    nastya = 'python21'
    print(эртай) # алиби

# func()
# print(nastya)   - NameError: name 'nastya' is not defined


count = 0

def add():
    print(count)
    count += 1 # UnboundLocalError: local variable 'count' referenced before assignment

def add():
    global count # доступ на изменение глобальной переменной count
    count += 1
    print(count)

add()
add()
add()
print(count)
# 1 2 3 3


a = 'global'

def outer_func():
    a = 'enclosed'

    def inner_func():
        a = 'local'
        print(a) # local
    
    print(a) # enclosed
    inner_func()

print(a) # global
outer_func()

# global enclosed local


def count(i):
    counter = 0
    
    def add():
        nonlocal counter # доступ на чтение и изменение локальной переменной counter 
        print(counter)
        counter += 1
    
    for _ in range(i):
        add()

count(10)
# 0 1 2 3 4 5 6 7 8 9

def func():
    a = '1'
    def inner_func():
        def inner2_func():
            nonlocal a # доступ на чтение и изменение локальной переменной a
            a = 2
        inner2_func()
    inner_func()
    print(a)
func() # 2

