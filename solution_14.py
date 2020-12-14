from itertools import product


def apply(instruction, bits, mask):
    ins, value = instruction.split(" = ")
    bit_value = '{:036b}'.format(int(value))
    address = int(ins.split('[')[1].split(']')[0])

    if address not in bits:
        bits[address] = ['0'] * 36

    for i, m in enumerate(mask):
        if m == 'X':
            bits[address][i] = bit_value[i]
        else:
            bits[address][i] = m
    return bits


def apply2(instruction, bits, mask):
    ins, value = instruction.split(" = ")
    address = '{:036b}'.format(int(ins.split('[')[1].split(']')[0]))
    address = [b for b in address]

    pot_addresses = [0]*len(address)
    for i, m in enumerate(mask):
        if m == '0':
            pot_addresses[i] = str(address[i])
        elif m == '1':
            pot_addresses[i] = '1'
        else:
            pot_addresses[i] = 'X'

    indices = [i for i, x in enumerate(pot_addresses) if x == "X"]
    for replacements in product(['0', '1'], repeat=len(indices)):
        for i, r in zip(indices, replacements):
            pot_addresses[i] = r
        bits[(int(''.join(pot_addresses), 2))] = int(value)
    return bits


if __name__ == "__main__":

    file_name = "test_14.txt"
    file_name = "input_14.txt"

    funcs = [apply, apply2]
    for func in funcs:
        bits = {}
        for line in open(file_name):
            if "mask" in line:
                mask = line.strip().split(" = ")[1]
                mask = [c for c in mask]
            else:
                bits = func(line.strip(), bits, mask)
        if func == apply:
            print(sum([int("".join(b), 2) for _, b in bits.items()]))  # 6631883285184
        else:
            print(sum([v for _, v in bits.items()]))  # 3161838538691
