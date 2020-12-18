from itertools import product
import numpy as np
import sympy


class Int():
    def __init__(self, i):
        self.val = i

    def __add__(self, other):
        return Int(self.val + other.val)

    def __sub__(self, other):
        return Int(self.val * other.val)


class IntRev():
    def __init__(self, i):
        self.val = i

    def __add__(self, other):
        return IntRev(self.val * other.val)

    def __mul__(self, other):
        return IntRev(self.val + other.val)


def evaluate(line):
    line = line.strip()
    line = line.replace("*", "-")
    line = line.replace("(", " ( ")
    line = line.replace(")", " ) ")

    splits = line.split(" ")
    for i, split in enumerate(splits):
        try:
            j = int(split)
            splits[i] = "Int("+split+")"
        except:
            pass
    line = " ".join(splits)

    return eval(line).val


def evaluate_rev(line):
    line = line.strip()
    line = line.replace("*", "-")
    line = line.replace("+", "*")
    line = line.replace("-", "+")
    line = line.replace("(", " ( ")
    line = line.replace(")", " ) ")

    splits = line.split(" ")
    for i, split in enumerate(splits):
        try:
            j = int(split)
            splits[i] = "IntRev("+split+")"
        except:
            pass
    line = " ".join(splits)

    return eval(line).val


if __name__ == "__main__":

    file_name = "test_18a.txt"
    file_name = "input_18.txt"

    print(sum(evaluate(line) for line in open(file_name)))  # 50956598240016
    print(sum(evaluate_rev(line) for line in open(file_name)))
