# Задание 1: форматирование строк через генератор списков

strings = ["python", "lambda", "list comprehension", "decorator"]


def format_strings(items: list[str]) -> list[str]:
    return [f"{i} - {s}" for i, s in enumerate(items)]


def main():
    result = format_strings(strings)
    for line in result:
        print(line)


if __name__ == "__main__":
    main()