# Задание 2: lambda с именованными аргументами — ключи удвоенной длины

double_keys = lambda **kwargs: {key * 2: value for key, value in kwargs.items()}


if __name__ == "__main__":
    result = double_keys(abc=5, x=10, name="Alice")
    print(result)  # {'abcabc': 5, 'xx': 10, 'namename': 'Alice'}
