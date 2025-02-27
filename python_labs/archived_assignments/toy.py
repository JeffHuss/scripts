# Define class object for "robot_dog"
class robot_dog:
    def __init__(self, name_val, breed_val):
        # add name and breed
        self.name = name_val
        self.breed = breed_val
    def bark(self):
        # Barks
        print('Woof woof!')


my_dog = robot_dog('Finn', 'Chihuahua')

print(my_dog.name)
print(my_dog.breed)
my_dog.bark()