import re


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


def evaluate(line, rev=False):
    if rev:
        line = line.replace("*", "-").replace("+", "*").replace("-", "+")
    else:
        line = line.replace("*", "-")
    line = line.replace("(", " ( ").replace(")", " ) ")

    splits = line.split(" ")
    for i, split in enumerate(splits):
        try:
            j = int(split)
            if rev:
                splits[i] = "IntRev("+split+")"
            else:
                splits[i] = "Int("+split+")"
        except:
            pass
    line = " ".join(splits)

    return eval(line).val


if __name__ == "__main__":

    file_name = "test_18a.txt"
    file_name = "input_18.txt"

    print(sum(evaluate(line.strip())
              for line in open(file_name)))  # 50956598240016
    print(sum(evaluate(line.strip(), True)
              for line in open(file_name)))  # 535809575344339
