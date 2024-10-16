from src.product import Product


class Category:
    name: str
    description: str
    products: list

    count_category = 0
    count_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.count_category += 1
        Category.count_products = len(self.__products)

    @property
    def products(self):
        return self.__products


    def add_products(self, products_new: Product):
        self.__products.append(products_new)

        Category.count_products += 1

    @property
    def products_list(self):
        products_list = ""
        for product in self.__products:
            products_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_list
