import numpy as np
from tqdm import tqdm

flip_inst = {}
flip_inst['e'] = [1, 0]
flip_inst['w'] = [-1, 0]
flip_inst['se'] = [0, -1]
flip_inst['sw'] = [-1, -1]
flip_inst['ne'] = [1, 1]
flip_inst['nw'] = [0, 1]


def flip_tile(instr, tiles):
    tile = np.array([0, 0])
    while instr:
        for fi, dir in flip_inst.items():
            if instr.startswith(fi):
                tile += dir
                instr = instr[len(fi):]
                continue

    if list(tile) in tiles:
        del tiles[tiles.index(list(tile))]
    else:
        tiles.append(list(tile))
    return tiles


def count_neighbors(matrix, x, y):
    num = 0
    for _, dir in flip_inst.items():
        if matrix[x + dir[0], y + dir[1]] == 1:
            num += 1
    return num


def evolve(matrix):
    to_flip = np.zeros(matrix.shape)
    for x in range(1, matrix.shape[0]-1):
        for y in range(1, matrix.shape[1]-1):
            neighbors = count_neighbors(matrix, x, y)
            # Any black tile with zero or more than 2 black tiles immediately
            # adjacent to it is flipped to white.
            if matrix[x, y] == 1:
                if neighbors == 0 or neighbors > 2:
                    to_flip[x, y] = 1
            # Any white tile with exactly 2 black tiles immediately adjacent to
            # it is flipped to black.
            else:
                if neighbors == 2:
                    to_flip[x, y] = 1
    matrix[to_flip == 1] = (matrix[to_flip == 1] + 1) % 2
    return matrix


if __name__ == "__main__":
    file_name = "test_24.txt"
    file_name = "input_24.txt"

    tiles = []
    for line in open(file_name):
        tiles = flip_tile(line.strip(), tiles)
    print(len(tiles))  # 521

    tiles = np.array(tiles)
    delx = max(tiles[:, 0]) - min(tiles[:, 0])
    dely = max(tiles[:, 1]) - min(tiles[:, 1])
    matrix = np.zeros([200 + delx, 200 + dely], np.int)
    for t in tiles:
        matrix[t[0]+100, t[1]+100] = 1

    for _ in tqdm(range(100)):
        matrix = evolve(matrix)
    print(np.sum(matrix))  # 4242
