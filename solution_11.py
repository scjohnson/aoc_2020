import numpy as np
from itertools import product


def create_seats(char_seats):
    seats = np.zeros((len(char_seats)+2, len(char_seats[0])+2), np.int)
    for i, line in enumerate(char_seats):
        for j, seat in enumerate(line):
            if seat == ".":
                seats[i+1, j+1] = 0
            elif seat == "#":
                seats[i+1, j+1] = 1
            else:
                seats[i+1, j+1] = 2
    return seats


def evolve(seats):
    new_seats = np.copy(seats)
    for x in range(1, seats.shape[0]-1):
        for y in range(1, seats.shape[1]-1):
            if seats[x, y] == 1:
                if np.sum(seats[x-1:x+2, y-1:y+2] == 2) == 0:
                    new_seats[x, y] = 2
            elif seats[x, y] == 2:
                if np.sum(seats[x-1:x+2, y-1:y+2] == 2) - 1 >= 4:
                    new_seats[x, y] = 1
    return new_seats


def closest_seat(seats, x_mid, y_mid, delx, dely):
    x, y = x_mid + delx, y_mid + dely
    while x < seats.shape[0] and y < seats.shape[1] and x > 0 and y > 0:
        if seats[x, y] == 1:
            return 0
        elif seats[x, y] == 2:
            return 1
        x += delx
        y += dely
    return 0


def count_seats(seats, x, y):
    tot_seats = 0
    for delx, dely in product([-1, 0, 1], repeat=2):
        if delx == 0 and dely == 0:
            continue
        tot_seats += closest_seat(seats, x, y, delx, dely)
    return tot_seats


def evolve2(seats):
    new_seats = np.copy(seats)
    for x in range(1, seats.shape[0]-1):
        for y in range(1, seats.shape[1]-1):
            if seats[x, y] == 1:
                if count_seats(seats, x, y) == 0:
                    new_seats[x, y] = 2
            elif seats[x, y] == 2:
                if count_seats(seats, x, y) >= 5:
                    new_seats[x, y] = 1
    return new_seats


if __name__ == "__main__":

    file_name = "test_11.txt"
    file_name = "input_11.txt"

    seats = create_seats([line.strip() for line in open(file_name)])
    while(True):
        new_seats = evolve(seats)
        if np.array_equal(new_seats, seats):
            print(np.sum(new_seats == 2))  # 2251
            break
        seats = new_seats

    seats = create_seats([line.strip() for line in open(file_name)])
    while(True):
        new_seats = evolve2(seats)
        if np.array_equal(new_seats, seats):
            print(np.sum(new_seats == 2))  # 2019
            break
        seats = new_seats
