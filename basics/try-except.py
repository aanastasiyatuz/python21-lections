"==================Exceptions===================="
# Исключения (ошибки) - обьекты, которые прерывают работу кода, если были вызваны 

SyntaxError #  исключение, которое выходит, когда в коде допущенна синтаксическая ошибка

# (   - SyntaxError: unexpected EOF while parsing 
# (когда мы не закрыли скобочку или кавычку)

# a =      - SyntaxError: invalid syntax
# (когда мы что-то сделали не по синтаксису питона)


NameError # исключение, которое выходит, когда мы обращаемся к несуществующей переменной

# ditfhgdjtfg   - NameError: name 'ditfhgdjtfg' is not defined


IndexError # исключение, которое выходит, когда мы обращаемся по несуществующему индексу

list_ = [1,2,3,4]
# list_[1000]   - IndexError: list index out of range
# list_.pop(1000)   - IndexError: pop index out of range


KeyError # исключение, которое выходит, когда мы обращаемся по несуществующему ключу

dict_ = {"a":1}
# dict_['b']   - KeyError: 'b'
# dict_.pop('b')    - KeyError: 'b'

print(dict_.get('b'))  # не ошибка, выйдет None если ключа нет


ValueError # выходит когда мы пытаемся распаковать какую-то последовательность, где количество переменных и элементов в последовательности не совпадает
# или когда мы в функцию передаем некорректный для нее тип данных

# a,b,c = 'ab'    - ValueError: not enough values to unpack (expected 3, got 2)
a,b = 'ab'  # 2 символа могут распаковаться на 2 переменные

# int('10d')   - ValueError: invalid literal for int() with base 10: '10d'


TypeError # когда мы пытаемся использовать методы не свойственные какому-то типу данных
# или когда мы пытаемся передать в функцию больше или меньше аргументов, чем принимает функция

# for i in 12345678:   - TypeError: 'int' object is not iterable

# 5 + "5"    - TypeError: unsupported operand type(s) for +: 'int' and 'str'

# "5" + 5    - TypeError: can only concatenate str (not "int") to str

# hash([1,2])     - TypeError: unhashable type: 'list'

# {[1,2,3]:"hello"}   - TypeError: unhashable type: 'list'

# input('hello', 1)   - TypeError: input expected at most 1 argument, got 2

# [].append()   - TypeError: append() takes exactly one argument (0 given)

# [].append(1,2)   - TypeError: append() takes exactly one argument (2 given)


IndentationError # когда мы не правльно используем отступы
#    a = 4    - IndentationError: unexpected indent

# for i in range(1):
# print(i)      - IndentationError: expected an indented block


ZeroDivisionError # выходит при делении на 0

# 45 / 0     - ZeroDivisionError: division by zero
# 3 // 0     - ZeroDivisionError: integer division or modulo by zero
# 3 % 0      - ZeroDivisionError: integer division or modulo by zero


AttributeError # выходит когда мы обращаемся к несуществующему аттрибуту или методу обьекта

# [].replace('a', '')   - AttributeError: 'list' object has no attribute 'replace'
# ''.pop(0)   - AttributeError: 'str' object has no attribute 'pop'


"============Обработка исключений================"
# чтобы код не прекращал свою работу при некорректных данных

try:
    код, который может вызвать ошибку

except Ошибка, которая может возникнуть:
    код, который сработает, если в try ошибка вышла

else:
    код, который сработает, если в try ошибка не вышла

finally:
    код, который сработает в любом случае


try:
    num = int(input())
except ValueError:
    print('введите число')
else:
    print('введенное число', num)
# если в input придет число - выйдет то, что мы написали в else
# если в input придет не число - выйдет то, что мы написали в except

# raise  - вызвать ошибку

try:
    raise SyntaxError
except (ValueError, TypeError, KeyError, SyntaxError): # отлавливаются только те ошибки, которые мы указали
    print('была обработана одна ошибка из (ValueError, TypeError, KeyError, SyntaxError)')

try:
    raise NameError
except:   # отлавливает все ошибки
    print("была обработана ошибка")

try:
    print("hello")
    raise
except:
    print("except")
else:
    print('else')
finally:
    print('finally')

try:
    5 + '5'
except Exception as error: # отловятся все ошибки + мы их записываем в переменную error
    print(error)
else:
    print("все ок")
finally:
    print('finally')
