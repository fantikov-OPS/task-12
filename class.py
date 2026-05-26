class Dog:
    def __init__(self, name, age, height, weight, master, address='Minsk'):
        self.__name = name
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__master = master
        self.__address = address

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, new_master):
        self.__master =new_master

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        self.__address = new_address

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def bark(self):
        print('bark bark')

    def run(self):
        print('Run!')

    def jump(self):
        print ('Jump!')


dog = Dog('Bob', 10, 15, 25, 'Alice', 'Grodno')

dog.address = 'Minsk'

class Pet:

    def __init__(self, name, age, master, height, weight):
        self.name = name
        self.age = age
        self.master = master
        self.height = height
        self.weight = weight

    def change_weight(self, plus_weight=None):
        self.weight = self.weight + plus_weight if plus_weight else self.weight + 0.2

    def cnage_height(self, plus_height=None):
        self.height = self.height + plus_height if plus_height else self.weight + 0.2

    def run(self):
        print('run!')

    def jump(self):
        print ('Jump!')

    def birthday(self):
        self.age+=1


class Dog(Pet):

    def bark(self):
        print('bark bark')

        
class Cat(Pet):

    def meow(self):
        print('meov')


class Parrot(Pet):

    def set_name(self, new_name=None):
        if new_name and len(new_name)>0:
            self.name = new_name
        else:
            print('Wrong Name')

    def fly(self):
        print('This parrot cannot fly.') if self.weight > 0.1 else print ('Fly')


    def jump(self):
        return print('Parrot dont jump')



parrot = Parrot('Gosha', 5, 'Petya', 3, 0.05)
dog  = Dog('Myxtar', 3, 'Tola',30, 45 )

parrot.jump()
dog.jump()