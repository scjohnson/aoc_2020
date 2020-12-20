import numpy as np
import itertools


def read_tiles(file_name, array_size):
    tiles = {}
    tile_id = 0
    y = 0

    tile = None
    for line in open(file_name):
        if "Tile" in line:
            tile_id = int(line.strip().split(" ")[1][:-1])
            y = 0
            tiles[tile_id] = np.zeros([array_size, array_size], np.int)
            # print(tiles[tile_id])
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
    for i in range(3):
        tile = np.rot90(tile)
        yield tile
    tile = np.fliplr(tile)
    yield tile
    for i in range(3):
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


def connect(edge, tile2):
    if np.all(edge == tile2[0, :]):
        return True
    if np.all(edge == tile2[-1, :]):
        return True
    if np.all(edge == tile2[:, 0]):
        return True
    if np.all(edge == tile2[:, -1]):
        return True
    if np.all(edge == np.flip(tile2[0, :])):
        return True
    if np.all(edge == np.flip(tile2[-1, :])):
        return True
    if np.all(edge == np.flip(tile2[:, 0])):
        return True
    if np.all(edge == np.flip(tile2[:, -1])):
        return True


if __name__ == "__main__":

    file_name = "test_20.txt"
    array_size = 10
    image_size = 3
    file_name = "input_20.txt"
    image_size = 12

    tiles = read_tiles(file_name, array_size)
    mult = 1
    starting_corner = 0
    for tile_id1, tile1 in tiles.items():
        no_matches = [0, 0, 0, 0]
        for tile_id2, tile2 in tiles.items():
            if tile_id1 != tile_id2:
                if connect(tile1[0, :], tile2):
                    no_matches[0] = 1
                if connect(tile1[-1, :], tile2):
                    no_matches[1] = 1
                if connect(tile1[:, 0], tile2):
                    no_matches[2] = 1
                if connect(tile1[:, -1], tile2):
                    no_matches[3] = 1
        if sum(no_matches) == 2:
            mult *= tile_id1
            if (no_matches[1] == 1 and no_matches[3] == 1):
                starting_corner = tile_id1
    print("part 1: ", mult)  # 18449208814679

    big_i, big_j = 1, 0
    big_image_size = image_size*array_size-(image_size-1)
    big_image = np.zeros([big_image_size, big_image_size], np.int)
    big_image[:array_size, :array_size] = tiles[starting_corner]
    used_tiles = [starting_corner]
    while len(used_tiles) != len(tiles):
        for tile_id, tile in tiles.items():
            if tile_id in used_tiles:
                continue
            if try_fit(big_image, big_i, big_j, tile):
                used_tiles.append(tile_id)
                big_i += 1
                if big_i == image_size:
                    big_j += 1
                    big_i = 0

    # Now remove the strips in between tiles and at the end
    for big_i in range(big_image.shape[0]-1, -1, -9):
        big_image = np.delete(big_image, big_i, 0)
        big_image = np.delete(big_image, big_i, 1)

    monster = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
                            1, 1, 0, 0, 0, 0, 1, 1, 1],
                        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]], np.int)

    for t in tile_iters(big_image):
        num_monsters = 0
        for i in range(0, t.shape[0]-monster.shape[0]):
            for j in range(0, t.shape[1]-monster.shape[1]):
                sub_image = t[i:i+monster.shape[0], j:j+monster.shape[1]]
                if np.all(sub_image[monster == 1] == 1):
                    num_monsters += 1
        if (num_monsters > 0):
            print("found monsters")
            print("part 2: ", np.sum(big_image)-num_monsters*np.sum(monster))  # 1559
            exit
