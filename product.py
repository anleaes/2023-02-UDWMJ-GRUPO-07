from category import Category

class Product(Category):
    def __init__(self, name, description, date_fabrication, is_active)
    super().__init__(id, name, description)
    self._name = name
    self._description = description
    self._date_fabrication = date_fabrication
    self._is_active = is_active