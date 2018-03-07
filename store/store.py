class Store(object):
    def __repr__(self):
        return "<Store object, products: {}, location: {}, owner: {}>".format(self.products, self.location, self.owner)
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

if __name__ == "__main__":
    walmart = Store([],"Chicago","Chris Poche")
    print(walmart.__repr__())