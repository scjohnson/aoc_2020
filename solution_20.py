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

def connect(edge, tile2):
    # print("e: ", edge)
    # print("tile: ", tile2)
    if np.all(edge == tile2[0,:]):
        return True
    if np.all(edge == tile2[-1,:]):
        return True
    if np.all(edge == tile2[:,0]):
        return True
    if np.all(edge == tile2[:,-1]):
        return True
    if np.all(edge == np.flip(tile2[0,:])):
        return True
    if np.all(edge == np.flip(tile2[-1,:])):
        return True
    if np.all(edge == np.flip(tile2[:, 0])):
        return True
    if np.all(edge == np.flip(tile2[:,-1])):
        return True

if __name__ == "__main__":

    file_name = "test_20.txt"
    array_size = 10
    image_size = 3
    # file_name = "input_20.txt"
    # image_size = 12

    tiles = read_tiles(file_name, array_size)
    mult = 1
    for tile_id1, tile1 in tiles.items():
        no_matches = [0,0,0,0]
        for tile_id2, tile2 in tiles.items():
            # print("tile1: ", tile1)
            # print("tile2: ", tile2)
            # print(tile1.shape, tile2.shape)
            if tile_id1 != tile_id2:
                if connect(tile1[0,:], tile2):
                    no_matches[0] = 1
                if connect(tile1[-1,:], tile2):
                    no_matches[1] = 1
                if connect(tile1[:,0], tile2):
                    no_matches[2] = 1
                if connect(tile1[:,-1], tile2):
                    no_matches[3] = 1
        if sum(no_matches) == 2:
            print(tile_id1)
            mult *= tile_id1
        print(sum(no_matches))
    print(mult) # 18449208814679



