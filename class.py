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

    def jump(self, metesr, pet = None):
        print (f'Pets Jump {metesr}' if not pet else f'{pet} Jump {metesr}')

    def birthday(self):
        self.age+=1

    def voise(self):
        pass


class Dog(Pet):

    def voise(self):
        print('bark bark')

    def jump(self, metesr, pet = 'Dog'):
        print(f'Dogs cannot jump so high' if metesr > 0.5 else super().jump(metesr, pet))


class Cat(Pet):

    def voise(self):
        print('meov')

    def jump(self, metesr, pet="cat"):
        print(f'Cats cannot jump so high' if metesr > 2 else super().jump(metesr, pet))


class Parrot(Pet):
    def __init__(self, name, age, master, height, weight, species):
        super().__init__(name, age, master, height, weight)
        self.species = species

    def voise(self):
        print('chirk-chirik')

    def set_name(self, new_name=None):
        if new_name and len(new_name)>0:
            self.name = new_name
        else:
            print('Wrong Name')

    def fly(self):
        print('This parrot cannot fly.') if self.weight > 0.1 else print ('Fly')


    def jump(self, metesr, pet='parrot'):
        if metesr > 0.05:
            print('Parrot cannot jump so high')
        else:
            super().jump(metesr, pet)

        #print(f'Parrot cannot jump so high' if metesr > 0.05 else super().jump(metesr, pet))

    def change_weight(self, new_weight=None):
        self.weight = new_weight if new_weight else self.weight + 0.5

    def cnage_height(self, new_height=None):
        self.height = new_height if new_height else self.height + 0.5

class MyTime():
    
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __eq__(self, other):
        if self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds:
            return False
        else:
            return True

    def __add__(self, other):
        total = (self.hours  * 3600 + self.minutes * 60 + self.seconds + other.hours * 3600 + other.minutes * 60 + other.seconds)
        print (f'{total // 3600}:{(total % 3600) // 60}:{total % 60}')
        
    def __sub__(self, other):
        total = (self.hours * 3600 + self.minutes * 60 + self.seconds - (other.hours * 3600 + other.minutes * 60 + other.seconds))
        sign = "-" if total < 0 else ""
        t = abs(total)
        h, m, s = t // 3600, (t % 3600) // 60, t % 60
        print(f"{sign}{h}:{m}:{s}")        

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'
        
 
        
class Car:
    __last_model = None
    __counter = None
    
    def __init__(self, model, counter):
        self.model = model
        Car.__last_model = model
        Car.__counter = counter
    
    @classmethod
    def get_last_model(cls):
        return cls.__last_model

    @classmethod
    def get_counter(cls):
        return cls.__counter

    @staticmethod
    def is_model_ok(count):
        return count > 9

car1 = Car('Sirroco', 8)
countt = car1.get_counter()
print(Car.is_model_ok(countt))