"========= Работа с файлами ========"
# try:
#     # open открывает файл для чтения
#     file = open('file.txt')
#     # Метод read() считывает файл полностью
#     # output = file.read()
#     # readline() # читает только одну строку
#     # output = file.readline()
#     # output2 = file.readline()
#     # readlines() читает все строки, возвращает список 
#     # output = file.readlines()
#     # print(output)
    
#     # seeker - курсор, считывающий файл
#     # s1 = file.read()
#     # file.seek(0) # передвигаем курсор в начало
#     # s2 = file.read()
#     # print("s1: ", s1)
#     # print("s2: ", s2)

#     # lineL1 = file.readline()
#     # print("➡ lineL1 :", lineL1)
#     # line2 = file.readline()
#     # print("➡ line2 :", line2)

#     # Считывание всех строк
#     # for line in file.readlines():
#     #     print(line)
# except:
#     pass
# finally:
#     file.close()

# Контекстный мененджнер
# with open('file.txt') as file:
#     print(file.read())

# Типы открытия файлов
# r (read) - станлартный тип открытия, только для чтения, если файла нет, вызывает ошибку
# w (write) - тип открытия только для записи, если файла нет, создает его, стирает
# with open('write_file.txt', 'w') as file:
    # write() записывает строку в файл
    # file.write('hello everyone')
    # writelines() записвает элементы итерируемого объекта в файл, не добваляет \n автоматически
    # file.writelines(['Hello', 'World'])
    # Если нужно чтобы каждая строка начиналась с новой строки
    # file.write('\n'.join(['hello', 'world']))

# a (append) - Добавляет новые записи в конец файла
# with open('write_file.txt', 'a') as file:
#     file.write('Hello world')

# w+ - открывает файл как для чтения, так и для записи, создает несуществуюший файл
# r+ - открывает файл, если его нет, вызывает ошибку
# a+ - открывает файл для записи в конец, при отсутствии файла создает его
# with open('non-exist-file.txt', 'w+'): pass


"========= Пакеты, Модули ========="
# import file_package
# file_package.sum_file()

# Один файл (file_package.py) - это пакет
# from file_package import sum_file, read_sum_file
# sum_file(5, 100)

# a = 10
# b = read_sum_file()
# print(a + b)

# Папка с пакетами - это модуль

