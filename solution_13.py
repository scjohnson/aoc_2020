import numpy as np
from sympy.ntheory.modular import crt

if __name__ == "__main__":

    file_name = "test_13.txt"
    file_name = "input_13.txt"

    f = open(file_name)
    minutes = int(f.readline())
    busses = f.readline().strip().split(',')
    times, offsets = np.array([], np.int), np.array([], np.int)
    
    for offset, b in enumerate(busses):
        if b.isnumeric():
            times = np.append(times, int(b))
            offsets = np.append(offsets, offset)
    mins = (times-minutes) % times

    print(min(mins)*times[mins == min(mins)][0])  # 4207
    # Yikes ... lots of struggling before remembering/finding Chinese Remainder Theorem
    # If you wanna be really lazy
    print(crt(times, (times-offsets) % times)[0])

    # The old way:
    # M = np.product(times)
    # bs = np.array([M//o for o in times], int)
    # bsp = np.array([pow(int(b), -1, t) for b, t in zip(bs, times)])
    # print(np.sum(-offsets*bs*bsp) % M)  # 725850285300475
