import sys

summ = sum(int(i) for i in sys.argv if i.isdigit())

print(summ)