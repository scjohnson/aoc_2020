import numpy as np
from sympy.ntheory.modular import crt

if __name__ == "__main__":

    file_name = "test_13.txt"
    file_name = "input_13.txt"

    f = open(file_name)
    minutes = int(f.readline())
    busses = f.readline().strip().split(',')
    times = []
    offsets = []
    for offset, b in enumerate(busses):
        if b.isnumeric():
            times.append(int(b))
            offsets.append(offset)
    offsets = np.array(offsets)

    mins = [time-minutes % time for time in times]

    print(min(mins)*times[mins.index(min(mins))])  # 4207
    # If you wanna be really lazy
    print(crt(np.array(times), (times-offsets) % times)[0])

    # Yikes ... lots of struggling before remembering/finding Chinese Remainder Theorem
    # M = np.product(times)
    # bs = np.array([M//o for o in times], int)
    # bsp = np.array([pow(int(b), -1, t) for b, t in zip(bs, times)])
    # print(np.sum(-offsets*bs*bsp) % M)  # 725850285300475
