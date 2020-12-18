import re


class Int():
    def __init__(self, i):
        self.val = i

    def line_relace(line):
       line = line.replace("(", " ( ").replace(")", " ) ")
       return line.replace("*", "-")
    
    def IntReplace(i):
        return "Int("+i+")"

    def __add__(self, other):
        return Int(self.val + other.val)

    def __sub__(self, other):
        return Int(self.val * other.val)


class IntRev():
    def __init__(self, i):
        self.val = i
    
    def line_relace(line):
       line = line.replace("(", " ( ").replace(")", " ) ")
       return line.replace("*", "-").replace("+", "*").replace("-", "+") 

    def IntReplace(i):
        return "IntRev("+i+")"

    def __add__(self, other):
        return IntRev(self.val * other.val)

    def __mul__(self, other):
        return IntRev(self.val + other.val)


def evaluate(line, IntClass=Int):
    line = IntClass.line_relace(line)

    splits = line.split(" ")
    for i, split in enumerate(splits):
        try:
            j = int(split)
            splits[i] = IntClass.IntReplace(split)
        except:
            pass
    line = " ".join(splits)

    return eval(line).val


if __name__ == "__main__":

    file_name = "test_18a.txt"
    file_name = "input_18.txt"

    print(sum(evaluate(line.strip())
              for line in open(file_name)))  # 50956598240016
    print(sum(evaluate(line.strip(), IntRev)
              for line in open(file_name)))  # 535809575344339
