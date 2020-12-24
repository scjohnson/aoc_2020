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
    while(instr):
        if instr[0] == 'e':
            tile += [1, 0]
            instr = instr[1:]
        elif instr[0] == 'w':
            tile += [-1, 0]
            instr = instr[1:]
        elif instr[0:2] == 'nw':
            tile += [0, 1]
            instr = instr[2:]
        elif instr[0:2] == 'sw':
            tile += [-1, -1]
            instr = instr[2:]
        elif instr[0:2] == 'ne':
            tile += [1, 1]
            instr = instr[2:]
        elif instr[0:2] == 'se':
            tile += [0, -1]
            instr = instr[2:]
        else:
            print("??", instr)

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
    to_flip = []
    for x in range(1, matrix.shape[0]-1):
        for y in range(1, matrix.shape[0]-1):
            neighbors = count_neighbors(matrix, x, y)
            # Any black tile with zero or more than 2 black tiles immediately
            # adjacent to it is flipped to white.
            if matrix[x, y] == 1:
                if neighbors == 0 or neighbors > 2:
                    to_flip.append([x, y])
            # Any white tile with exactly 2 black tiles immediately adjacent to
            # it is flipped to black.
            else:
                if neighbors == 2:
                    to_flip.append([x, y])
    for flip in to_flip:
        matrix[flip[0], flip[1]] = (matrix[flip[0], flip[1]] + 1) % 2
    return matrix


if __name__ == "__main__":
    file_name = "test_24.txt"
    file_name = "input_24.txt"

    tiles = []
    for line in open(file_name):
        tiles = flip_tile(line.strip(), tiles)

    print(len(tiles))

    minx = min(np.array(tiles)[:, 0]) - 2
    maxx = max(np.array(tiles)[:, 0]) + 2
    miny = min(np.array(tiles)[:, 1]) - 2
    maxy = max(np.array(tiles)[:, 1]) + 2

    delx = maxx-minx
    dely = maxy-miny
    matrix = np.zeros([202 + delx, 202 + dely], np.int)
    for t in tiles:
        matrix[t[0]+101, t[1]+101] = 1
    for _ in tqdm(range(100)):
        matrix = evolve(matrix)
    print(np.sum(matrix))
