class Car(object):
    def __init__(self, name, price, fuel, speed, mileage, tax):
        self.name = name
        self.price = price
        self.speed = speed
        self.mileage = mileage
        self.fuel = fuel
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()
    def display_all(self):
        print("=====" + self.name + "=====")
        print("Price: $" + str(self.price))
        print("Speed: " + str(self.speed) + "mph")
        if self.fuel == 1.0:
            print ("Fuel: Full")
        else:
            print("Fuel: " + str(self.fuel*100) + "%")
        print("Mileage: " + str(self.mileage) + "mph")
        print("Tax: " + str(self.tax*100) + "%")

honda       = Car("Honda",   10000,     1.0,    60,   10,     0.10)
toyota      = Car("Toyota",  30000,     1.0,    70,   15,     0.10)
ford        = Car("Honda",   40000,     0.5,    80,   20,     0.10)
corvette    = Car("Honda",   50000,     0.25,   90,   25,     0.10)
bmw         = Car("Honda",   60000,     0.75,   100,  35,     0.10)
hyundai     = Car("Honda",   70000,     1.25,   1000, 1000,   0.10)