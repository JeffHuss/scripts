class robot_dog:
    def __init__(self, name_val, breed_val):
        self.name = name_val
        self.breed = breed_val
    def bark(self):
        print('Woof woof!')

my_dog = robot_dog('Finn', 'Chihuahua')

print(my_dog.name)
print(my_dog.breed)
my_dog.bark()