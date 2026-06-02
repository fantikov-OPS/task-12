import random
from time import sleep


def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i*i

def my_animal_generator():
    yield 'cow'
    for animal in ['cat', 'dog', 'bear']:
        yield animal
    yield 'kit'

def inf_gen(diff = 10):
    first = True
    a, b = 1, 10
    while True:
        if first:
            yield random.randint(a,b)
            first = False
            sleep(0.3)
        else:
            a, b = a + diff, b + diff
            yield random.randint(a, b)
            sleep(0.3)

def main():
    for random_int in inf_gen():
        print(random_int)

if __name__ == "__main__":
    main()