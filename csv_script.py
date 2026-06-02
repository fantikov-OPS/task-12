import argparse


def add_person(first_name, last_name, age):
    with open('test.csv', 'a', encoding='utf-8') as f:
        f.write(f'\n{first_name},{last_name},{age}\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first-name', required=True)
    parser.add_argument('-ln', '--last-name', required=True)
    parser.add_argument('-a', '--age', required=True)
    args = parser.parse_args()
    add_person(args.first_name, args.last_name, args.age)