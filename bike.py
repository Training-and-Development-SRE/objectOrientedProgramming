class Bike(object):
    def __init__(self, name, price, speed):
        self.name = name
        self.price = price
        if speed > 3:
            self.speed = speed
        else:
            print("Setting speed to minimmum.")
            self.speed = 3
        self.miles = 0
    def displayInfo(self):
        print(self.name + ": Price: $" + str(self.price) + " | Maximum Speed: " + str(self.speed) + " | Miles ridden: " + str(self.miles))
        return self
    def ride(self):
        print("Riding...")
        self.miles += self.speed
        return self
    def reverse(self):
        if self.miles - self.speed >= 0:
            print("Reversing...")
            self.miles -= self.speed
        else:
            print(self.name + " hasn't gone anywhere yet.")
        return self

bike1 = Bike("bike1", 100, 3)
bike2 = Bike("bike2", 200, 6)
bike3 = Bike("bike3", 150, 4)

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
