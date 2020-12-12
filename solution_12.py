import numpy as np
from itertools import product


def take_step(dir, pos, step):
    d = step[0]
    num = int(step[1:])

    if d == 'F':
        pos += num*dir
    elif d == 'E':
        pos += num*np.array([0, 1])
    elif d == 'S':
        pos += num*np.array([-1, 0])
    elif d == 'W':
        pos += num*np.array([0, -1])
    elif d == 'N':
        pos += num*np.array([1, 0])
    elif d == 'R' or d == 'L':
        if d == 'R':
            rot = np.array([[0, -1], [1, 0]])
        else:
            rot = np.array([[0, 1], [-1, 0]])
        if num == 90:
            dir = np.matmul(rot, dir)
        elif num == 180:
            dir = -dir
        elif num == 270:
            dir = np.matmul(-rot, dir)
        else:
            print("different angle: ", num)
    else:
        print("unknown command", d, num)
    return dir, pos


def take_step_way(pos, way, step):
    d = step[0]
    num = int(step[1:])

    if d == 'F':
        pos += num*way
    elif d == 'E':
        way += num*np.array([0, 1])
    elif d == 'S':
        way += num*np.array([-1, 0])
    elif d == 'W':
        way += num*np.array([0, -1])
    elif d == 'N':
        way += num*np.array([1, 0])
    elif d == 'R' or d == 'L':
        if d == 'R':
            rot = np.array([[0, -1], [1, 0]])
        else:
            rot = np.array([[0, 1], [-1, 0]])
        if num == 90:
            way = np.matmul(rot, way)
        elif num == 180:
            way = -way
        elif num == 270:
            way = np.matmul(-rot, way)
        else:
            print("different angle: ", num)
    else:
        print("unknown command", d, num)
    return pos, way


if __name__ == "__main__":

    file_name = "test_12.txt"
    file_name = "input_12.txt"

    direction, position = np.array([0, 1]), np.array([0, 0])
    for step in [line.strip() for line in open(file_name)]:
        (direction, position) = take_step(direction, position, step)
    print(np.sum(np.abs(position)))  # 362

    position, waypoint = np.array([0, 0]), np.array([1, 10])
    for step in [line.strip() for line in open(file_name)]:
        (position, waypoint) = take_step_way(position, waypoint, step)
    print(np.sum(np.abs(position)))  # 29895
