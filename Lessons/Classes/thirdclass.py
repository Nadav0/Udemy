class Animal():
    def __init__(self):
        print("animal created")

    def who_am_i(self):
        return "i am an animal"

    def eat(self):
        return "i am eating"


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print ("Dog created")


    def who_am_i(self):
        return "i am a dog"

    def bark(self):
        return "Woof!"


my_dog = Dog()
print(my_dog.eat())
print(my_dog.who_am_i())
print(my_dog.bark())