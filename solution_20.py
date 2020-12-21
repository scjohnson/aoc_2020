import numpy as np
import itertools
from operator import add


def read_tiles(file_name, tile_size):
    tiles = {}
    tile_id = 0

    y = 0
    for line in open(file_name):
        if "Tile" in line:
            tile_id = int(line.strip().split(" ")[1][:-1])
            y = 0
            tiles[tile_id] = np.zeros([tile_size, tile_size], np.int)
        elif line.strip == "":
            continue
        else:
            for i, c in enumerate(line.strip()):
                if c == "#":
                    tiles[tile_id][i, y] = 1
            y += 1

    return tiles


def tile_iters(tile):
    yield tile
    for _ in range(3):
        tile = np.rot90(tile)
        yield tile
    tile = np.fliplr(tile)
    yield tile
    for _ in range(3):
        tile = np.rot90(tile)
        yield tile


def try_fit(big_image, big_i, big_j, tile):
    if big_i != 0:
        y_start = big_j*9
        y_stop = y_start+10
        x_start = big_i*10-(big_i-1)-1
        to_match = big_image[y_start:y_stop, x_start]
        for t in tile_iters(tile):
            if np.all(to_match == t[:, 0]):
                big_image[y_start:y_stop, x_start:x_start+10] = t
                return True
    else:
        y_start = big_j*9
        x_start = 0
        x_stop = 10
        to_match = big_image[y_start, x_start:x_stop]
        for t in tile_iters(tile):
            if np.all(to_match == t[0, :]):
                big_image[y_start:y_start+10, x_start:x_stop] = t
                return True
    return False


def connect(tile1, tile2):
    for t in tile_iters(tile2):
        if np.all(tile1[0, :] == t[0, :]):
            return True
        if np.all(tile1[-1, :] == t[0, :]):
            return True
        if np.all(tile1[:, 0] == t[0, :]):
            return True
        if np.all(tile1[:, -1] == t[0, :]):
            return True
    return False


if __name__ == "__main__":

    # file_name = "test_20.txt"
    # image_size = 3
    tile_size = 10
    file_name = "input_20.txt"
    image_size = 12
    starting_corner = 2207

    tiles = read_tiles(file_name, tile_size)

    mult = 1

    # Find the corners and the starting one
    matches = {}
    for tid in tiles:
        matches[tid] = 0
    for tid1, tid2 in itertools.combinations(tiles, 2):
        if connect(tiles[tid1], tiles[tid2]):
            matches[tid1] += 1
            matches[tid2] += 1
    for tid, match in matches.items():
        if match == 2:
            mult *= tid

    print("part 1: ", mult)  # 18449208814679

    # Fit the pieces together
    big_i, big_j = 1, 0
    big_image_size = image_size*tile_size-(image_size-1)
    big_image = np.zeros([big_image_size, big_image_size], np.int)
    big_image[:tile_size, :tile_size] = tiles[starting_corner]
    used_tiles = [starting_corner]
    while len(used_tiles) != len(tiles):
        for tile_id, tile in tiles.items():
            if tile_id in used_tiles:
                continue
            if try_fit(big_image, big_i, big_j, tile):
                used_tiles.append(tile_id)
                big_i = (big_i+1) % image_size
                if big_i == 0:
                    big_j += 1

    # Now remove the strips in between tiles and at the end
    for big_i in range(big_image.shape[0]-1, -1, -(tile_size-1)):
        big_image = np.delete(big_image, big_i, 0)
        big_image = np.delete(big_image, big_i, 1)

    monster = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
                            1, 1, 0, 0, 0, 0, 1, 1, 1],
                        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]], np.int)

    for t in tile_iters(big_image):
        num_monsters = 0
        for i, j in itertools.product(range(t.shape[0]-monster.shape[0]), range(t.shape[1]-monster.shape[1])):
            sub_image = t[i:i+monster.shape[0], j:j+monster.shape[1]]
            if np.all(sub_image[monster == 1] == 1):
                num_monsters += 1
        if (num_monsters > 0):
            print("part 2: ", np.sum(big_image) -
                  num_monsters*np.sum(monster))  # 1559
            break
