"================Работа с файлами==================="
# open - функция, которая позволяет открыть файл
"=========Режимы=========="
# r  - read (только для чтения)
# w  - write (только для записи (сначала все из файла удаляется, а потом записывается))
# a  - append (дозапись (все новое добавляется в конец))
# x  - создает файл. если он уже существует - ошибка
# rb  - чтение в бинарном виде
# wb  - запись в бинарном виде
# ab  - дозапись в бинарном виде

"когда мы не указываем режим - по умолчанию чтение"
# open("test.txt")  FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'

"когда мы открываем файл в режиме w - он создает пустой файл и потом туда записывает данные"
# open("test.txt", "w")    - создает пустой файл

"когда файла нет - он создает его"
# open("test.txt", "a")


"===================READ======================"
file = open("test.txt") # открываем файл в режиме чтения
res = file.read() # считаывет весь файл и возвращает строку
print(file.read(5)) # пустая строка, потому что каретка находится в самом конце файла
file.seek(0) # каретка переходит в индекс 0 (в начало файла)
print(file.read(5))  # 'hello' (считал 5 символов)
print(file.read(5))  # ' worl' (считал следующие символы)
print(file.tell())  # 10  (показывает текущее положение каретки)
file.readlines()  # ['d\n', 'Makers Bootcamp\n', 'line1\n', 'line2\n', 'line3\n']
file.seek(0)
print(file.readlines()) # ['hello world\n', 'Makers Bootcamp\n', 'line1\n', 'line2\n', 'line3\n']
print(file.tell()) # 46
file.close()


"===================WRITE====================="
file = open("test.txt", "w") # открыл файл, почистил
# res = file.read()   io.UnsupportedOperation: not readable
# метод read нельзя использовать при режиме записи и дозаписи
file.write("hello world\n") # в файл записали строку hello world
file.write("Makers Bootcamp\n") # после этого продолжает писать строку Makers Bootcamp
file.writelines(["line1\n", "line2\n", "line3\n"]) # принимает список со строками и дозаписывает их в файл
file.close() # обязательно закрываем файл




"==============With================="
# with - конструкция, которая в начале конструкции вызывает метод __enter__, а в конце вызывает __exit__
class Test:
    def __enter__(self):
        print("Начало работы")
        return self
    
    def __exit__(self, *args, **kwargs):
        print("Конец работы")
    
    def hello(self):
        print("Hello world")

with Test() as test:
    test.hello()

# Начало работы
# Hello world
# Конец работы


file1 = open("test.txt", "w")
file1.write("hello")
file1.close()
file2 = open("test.txt", "w")
file2.write("world")
# file1.write("fdgirwsukgh")  # ValueError: I/O operation on closed file.
# потому что file1 мы закрыли
file2.close()


with open("test.txt", 'w+') as file:
    file.write("Hello world\nMakers\nBootcamp")
    file.seek(0)
    res = file.read()
    file.seek(0)
    file.write("New lines\n")
    file.write(res)

with open("test.txt") as file:
    print(file.read())
    print(file.closed) # False
print(file.closed) # True

