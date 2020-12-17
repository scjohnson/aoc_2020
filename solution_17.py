from itertools import product
import numpy as np


def evolve_four(s):
    new_space = np.copy(s)
    for i, j, k, l in product(range(1, s.shape[0]-1),
                              range(1, s.shape[1]-1),
                              range(1, s.shape[2]-1),
                              range(1, s.shape[3]-1)):
        if s[i, j, k, l] == 1:
            if not (2 <= np.sum(s[i-1:i+2, j-1:j+2, k-1:k+2, l-1:l+2]) - 1 <= 3):
                new_space[i, j, k, l] = 0
        else:
            if np.sum(s[i-1:i+2, j-1:j+2, k-1:k+2, l-1:l+2]) == 3:
                new_space[i, j, k, l] = 1
    return new_space


def evolve(s):
    new_space = np.copy(s)
    for i, j, k in product(range(1, s.shape[0]-1),
                           range(1, s.shape[1]-1),
                           range(1, s.shape[2]-1)):
        if s[i, j, k] == 1:
            if not (2 <= np.sum(s[i-1:i+2, j-1:j+2, k-1:k+2]) - 1 <= 3):
                new_space[i, j, k] = 0
        else:
            if np.sum(s[i-1:i+2, j-1:j+2, k-1:k+2]) == 3:
                new_space[i, j, k] = 1
    return new_space


if __name__ == "__main__":

    file_name = "test_17.txt"
    file_name = "input_17.txt"
    start_size = 8
    num_cycles = 6

    space = np.zeros([start_size + num_cycles*2+2,
                      start_size + num_cycles*2+2,
                      1 + num_cycles*2+2], np.int)
    four_space = np.zeros([start_size + num_cycles*2+2,
                           start_size + num_cycles*2+2,
                           1 + num_cycles*2+2,
                           1 + num_cycles*2+2], np.int)
    for i, line in enumerate(open(file_name)):
        for j, c in enumerate(line.strip()):
            if c == '#':
                space[i+num_cycles+1, j+num_cycles+1, 1+num_cycles+1] = 1
                four_space[i+num_cycles+1, j+num_cycles +
                           1, 1+num_cycles, 1+num_cycles] = 1

    for cycle in range(num_cycles):
        space = evolve(space)
    print(np.sum(space))  # 230

    for cycle in range(num_cycles):
        four_space = evolve_four(four_space)

    print(np.sum(four_space))  # 1600
