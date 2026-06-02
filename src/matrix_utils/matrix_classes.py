import copy
import random

class Matrix:
    
    def __init__(self, *args):
        self.n = None
        self.m = None
        self.data = None
        
        if len(args) == 0:
            self.n = 5
            self.m = 5
            self.data = [[0 for _ in range(self.m) for _ in range(self.n)]]

        elif len(args) == 1 and isinstance(args[0], Matrix):
            other = args[0]
            self.n = other.n
            self.m = other.m
            self.data = copy.deepcopy(other.data)
        
        elif len(args) == 4:
            n, m, a, b = args
            self.validatye_size(n, m)
            if not isinstance(a, (int, float)) or not isinstance(b, (int , float)):
                raise TypeError("a и b должны быть числами")
            if a > b:
                raise ValueError("a не может быть больше b")
            self.n = n
            self.m = m
            low, high = int(a), int(b)
            self.data = [
                [random.randint(low, high) for _ in range(self.m)]
                for _ in range(self.n)
            ]
        else:
            raise TypeError("Проверить входящие данные")
        
    @staticmethod
    def validatye_size(n,m):
        if not isinstance(n, int) or not isinstance(m, int):
            raise TypeError("размеры должны быть числом")
        if n <= 0 or m <= 0:
            raise ValueError("размеры должны быть больше 0")

    def __str__(self):
        if not self.data:
            return "[]"
        col_widh = max(len(str(cell)) for row in self.data for cell in row)
        lines = []
        for row in self.data:
            cells = " ".join(str(cell).rjust(col_widh) for cell in row)
            lines.append(f"| {cells} |")
        return "\n".join(lines)