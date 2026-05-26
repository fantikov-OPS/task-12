# Задание 4: универсальный декоратор — обратный порядок позиционных аргументов

def reverse_arguments(func):
    def wrapper(*args, **kwargs):
        return func(*args[::-1], **kwargs)
    return wrapper


@reverse_arguments
def concat(a: str, b: str, c: str) -> str:
    return a + b + c


@reverse_arguments
def subtract(a: int, b: int, c: int) -> int:
    return a - b - c


if __name__ == "__main__":
    print(concat("A", "B", "C"))       # CBA
    print(subtract(10, 3, 2))          # 2 - 3 - 10 = -11
