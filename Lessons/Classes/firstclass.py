mylist = [1,2,3]
myset = set()
print(type(myset))
print(type(mylist))


class Dog:

    species = 'mammal'

    def __init__(self, breed, name):


        self.name = name
        self.breed = breed

    def bark(self, number):
        return "woof! my name is {} and the number is {} barks".format(self.name, number)



my_dog = Dog(breed="Shooki", name= "Maple")
other_dog = Dog(breed= 'jack russel', name= 'Shooshi')
print(my_dog.breed)
print(my_dog.name)
print(other_dog.bark(10))
