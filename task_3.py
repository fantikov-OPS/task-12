# Задание 3: декоратор — удаление чётных элементов из списка чисел

def remove_even_numbers(func):
    def wrapper(numbers, *args, **kwargs):
        filtered = [n for n in numbers if n % 2 != 0]
        return func(filtered, *args, **kwargs)

    return wrapper


@remove_even_numbers
def sum_numbers(numbers):
    return sum(numbers)


@remove_even_numbers
def product_numbers(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7]
    print(f"Исходный список: {data}")
    print(f"Сумма нечётных: {sum_numbers(data)}")
    print(f"Произведение нечётных: {product_numbers(data)}")
