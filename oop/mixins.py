``"=====================Миксины======================="
# Миксин - класс, который будет использоваться для наследования. от миксинов не создаются обьекты.

class CreateMixin:
    def product_create(self, title, price):
        # self.__class__ - обращение к классу, который наследовался от этого миксина
        model = self.__class__

        obj = model()
        _id = model._id
        obj.title = title
        obj.price = price
        obj.id = _id
        model.objects[_id] = obj
        model._id += 1

class ReadMixin:
    def product_detail(self, p_id):
        from pprint import pprint
        model = self.__class__
        obj = model.objects.get(p_id)
        pprint({"id":obj.id, "title":obj.title, "price":obj.price})

class UpdateMixin:
    ...

class DeleteMixin:
    def delete_product(self, p_id):
        model = self.__class__
        model.objects.pop(p_id)

class ProductCRUD(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    objects = {}
    _id = 1

    def __str__(self):
        return f"{self.id} -> {self.title}"
