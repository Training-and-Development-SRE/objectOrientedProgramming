class Product(object):
    def __init__(self, name, price, weight, brand):
        self.name = name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def tax(self, tax):
        total_price = (1 + tax)*self.price
        return "$" + str(total_price)
    def ret(self, reason):
        if reason == "defective":
            self.status = reason
            self.price = 0
        elif reason == "in box":
            self.status = "for sale"
        elif reason == "opened":
            self.status = "used"
            self.price *= 0.8
        return self
    def display(self):
        print("=====" + self.name + "=====")
        print("$" + str(self.price))
        print(str(self.weight) + "kg")
        print("Brand: " + self.brand)
        print(self.status)
        return self

class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner
    def add_product(self, name, price, weight, brand):
        newProduct = Product(name, price, weight, brand)
        self.products.append(newProduct)
        return self
    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
        return self
    def inventory(self):
        for product in self.products:
            product.display()

walmart = Store([], "Chicago", "Alex Leibowitz")
walmart.add_product("shoes", 100, 5, "Nike")
walmart.add_product("blender", 30, 5, "Blenda")
walmart.add_product("computer", 500, 30, "IBM")
walmart.remove_product("blender").inventory()