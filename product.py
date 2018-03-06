class Product(object):
    def __init__(self, name, price, weight, brand):
        self.name = name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
        self.display()
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

shoe = Product("White Shoes", 100, 5, "Nike")
print(shoe.sell().ret("opened").display().tax(0.15))