import random 
import string

from abc import ABC, abstractmethod

class Pet(ABC):

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

    @staticmethod
    def get_random_name():
        charrates = string.ascii_letters
        return f'{"".join(random.choices(charrates, k=1))}-{random.randint(10,99)}'


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


class Hourse(Pet):

    def voise(self):
        return 'Igogo'


class Donkey(Pet):

    def voise(self):
        return print('Ia')


class Mule(Donkey):
    pass


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

class MyExc(Exception):
    def __init__(self, message = 'Somth Error'):
        super().__init__(message)


class BookError(Exception):
    pass


class BookValidationsErrors(BookError):
    pass


class InvalidPages(BookValidationsErrors):
    pass


class InvalidYears(BookValidationsErrors):
    pass


class InvalidAuthor(BookValidationsErrors):
    pass


class InavlidPrice(BookValidationsErrors):
    pass

class Book:

    def __init__(self, year, price, author, page):
        self.price = self.validate_price(price)
        self.year = self.validete_year(year)
        self.page = self.validate_page(page)
        self.author = self.validate_author(author)

    @staticmethod
    def validate_author(author):
        if not isinstance(author, str):
            raise InvalidAuthor('Автор должен быть строкой')
        if not author.strip():
            raise InvalidAuthor('Строка не должна быть пустой')
        if len(author) > 10:
            raise InvalidAuthor('Имя не может быть больше 10 символов')
        return author

    @staticmethod
    def validate_page(page):
        if not isinstance(page, int) or isinstance(page, bool):
            raise InvalidPages('Колличество страниц должно быть числом')
        if page <= 0:
            raise InvalidPages('Колличество страниц должно быть больще 0')
        return page

    @staticmethod
    def validate_price(price):
        if not isinstance(price , (int, float)) or isinstance(price, bool):
            raise InavlidPrice('Цена должна быть числом')
        if price < 0:
            raise InavlidPrice('Цена должна быть больще 0')
        return float(price)

    @staticmethod
    def validete_year(year):
        if not isinstance(year, int) or isinstance(year, bool):
            raise InvalidYears('Год должен быть числом')
        current_year = date.today().year
        if year < 0 or year > current_year:
            raise InvalidYears(f'Год должен быть от 0 до {current_year}')
        return year

    def __str__(self):
        return (f'{self.author} - год.{self.year} - стр.{self.page} - цена.{self.price}')

class Animal(ABC):

    @abstractmethod
    def feline(self):
        raise NotImplemented
    
    @abstractmethod
    def canine(self):
        raise NotImplemented


class Pet(Animal):
    pass


class Cat(Pet):
    
    def feline(self):
        return True
    
    def canine(self):
        return False


class Dog(Pet):
    pass


class WildAnimal(Animal):
    pass


class Lios(WildAnimal):
    pass


class Wolf(WildAnimal):
    pass



if __name__ == '__main__':
    cat1=Cat()
    print(cat1.canine())