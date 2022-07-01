import json

def create_product(
    id_:int, price:int,
    name:str
):
    product = {
        'id': id_,
        'price': price,
        'name': name,
    }
    with open('db.json', 'r') as file:
        # Копируем старые данные
        json_data = json.load(file)
        products = json_data.get('products')
        # Обновляем их
        products.append(product)

    with open('db.json', 'w') as file:
        # Стираем старые данные и записываем новые
        json.dump(json_data, file)

# create_product(1, 45, 'bounty')

