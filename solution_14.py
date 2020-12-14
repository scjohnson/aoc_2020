import numpy as np
from itertools import product


def read_mask(line):
    mask = [0 for _ in range(36)]
    mask_values = [0 for _ in range(36)]
    for i, c in enumerate(line.split(" = ")[1]):
        if c != 'X':
            mask[i] = 1
            mask_values[i] = int(c)
    mask.reverse()
    mask_values.reverse()
    return mask, mask_values


def set_bit(bits, address, i, b):
    if b == 1:
        bits[address] = bits[address] | (b << i)
    else:
        m = (pow(2, 36)-1 - pow(2, i))
        bits[address] = bits[address] & m
    return bits


def apply(instruction, bits, mask, mask_values):
    ins, value = instruction.split(" = ")
    bit_value = [int(digit) for digit in bin(int(value))[2:]]
    address = int(ins.split('[')[1].split(']')[0])

    bit_value.reverse()
    for i, m in enumerate(mask):
        if not m:
            if i < len(bit_value):
                bits = set_bit(bits, address, i, int(bit_value[i]))
            else:
                bits = set_bit(bits, address, i, 0)
        else:
            bits = set_bit(bits, address, i, mask_values[i])
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

    max_line = 0
    for line in open(file_name):
        if 'mem' in line:
            address = int(line.split('[')[1].split(']')[0])
            max_line = max(max_line, address)

    bits = []
    for _ in range(max_line+1):
        bits.append(0x000000000000000000000000000000000000)
    for line in open(file_name):
        if "mask" in line:
            mask, mask_values = read_mask(line.strip())
        else:
            bits = apply(line.strip(), bits, mask, mask_values)
    print(sum(bits))  # 6631883285184

    bits = {}
    for line in open(file_name):
        if "mask" in line:
            mask = line.strip().split(" = ")[1]
            mask = [c for c in mask]
        else:
            bits = apply2(line.strip(), bits, mask)
    print(sum([v for _, v in bits.items()])) #3161838538691
