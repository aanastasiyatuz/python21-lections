import json

"========= JSON ========="
# JSON - Java Script Object Notation - это один из наиболее популярных типов данных, с которыми большинство языков программирования умеет работать
# with open('test.json', 'w') as file:
#     # Запись в JSON
#     dict_ = {
#         'products': [
#             {
#                 'id': 1,
#                 'name': 'snickers',
#                 'price': 45,
#             },
#             {
#                 'id': 2,
#                 'name': 'bounty',
#                 'price': 45,
#             }
#         ]
#     }
#     # dump - записывает словарь в файл, придерживаясь правил JSON формата
#     json.dump(dict_, file)


# with open('test.json', 'r') as file:
    # Чтение с JSON
    # dict_ = json.load(file)
    # print(dict_)


# dict ==DUMP==> JSON file
# file ==LOAD==> dict


# Работа с модулями похожа на работу с пакетами, но нужно указывать путь к папке/файлу
from product.models import create_product

create_product(1, 20, 'chips')


