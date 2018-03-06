class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print("Current health: " + str(self.health))
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog,self).__init__(name, 150)
    def pet(self):
        self.health += 5
        return self


class Dragon(Animal):
    def __init__(self, name):
        super(Dragon,self).__init__(name,170)
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon,self).display_health()
        print("I am a dragon!")
        return self

# generic = Animal("Jenny", 100)
# generic.walk().walk().walk().run().run().display_health()
# generic.pet()
# generic.fly()

# fido = Dog("Fido")
# fido.walk().walk().walk().run().run().pet().display_health()
# fido.fly()

# draco = Dragon("Draco")
# draco.fly().fly().fly().display_health()
# draco.pet()