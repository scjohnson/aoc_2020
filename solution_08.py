

def check(code):
    acc = 0
    index = 0
    visited = []
    while index not in visited:
        if index == len(code):
            return True, acc
        visited.append(index)
        ins, num = code[index].split(" ")
        if ins == 'acc':
            acc += int(num)
            index += 1
        elif ins == 'jmp':
            index += int(num)
        elif ins == 'nop':
            index += 1
    return False, acc


def variations(code):
    for i, c in enumerate(code):
        if c.split(' ')[0] == 'jmp':
            code[i] = code[i].replace('jmp', 'nop')
            yield code
            code[i] = code[i].replace('nop', 'jmp')
        elif c.split(' ')[0] == 'nop':
            code[i] = code[i].replace('nop', 'jmp')
            yield code
            code[i] = code[i].replace('jmp', 'nop')


if __name__ == "__main__":

    file_name = "test_08.txt"
    file_name = "input_08.txt"

    code = [line.strip() for line in open(file_name)]

    terminated, acc = check(code)
    print(acc)
    for variation in variations(code):
        terminated, acc = check(code)
        if terminated:
            print(acc)
