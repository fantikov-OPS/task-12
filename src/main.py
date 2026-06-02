from matrix_utils.matrix_classes import Matrix
from matrix_utils.matrix_funcs import matrix_max, matrix_min, matrix_sum



def main():
    default = Matrix()
    print("по умолчания 5х5 нули")
    print(default)
    random_m = Matrix(3,4,1,9)
    print("случайная матрица 3х4 /// от 1 до 9")
    print(random_m)
    print(f"max - {matrix_max(random_m)}")
    print(f"min - {matrix_min(random_m)}")
    print(f" sum - {matrix_sum(random_m)}")
    copied = Matrix(random_m)
    print(id(random_m))
    print(id(copied))
    print(copied)



if __name__ == "__main__":
    main()