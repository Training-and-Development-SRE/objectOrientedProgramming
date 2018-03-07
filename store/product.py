class Product(object):
    def __repr__(self):
        return "<Product object: {}, price: {}, weight: {}, brand: {}>".format(self.name, self.price, self.weight, self.brand)
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

if __name__ == "__main__":
    shoe2 = Product("tennis shoe", 30, 5, "Nike")
    shoe2.display()
    print(shoe2.__repr__())