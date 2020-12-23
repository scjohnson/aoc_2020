from collections import deque
from tqdm import tqdm


def play(cups):
    l = len(cups)
    t = cups.popleft()
    hold_out = [cups.popleft() for _ in range(3)]
    dest_cup = (t-1) % l
    while dest_cup in hold_out:
        dest_cup = (dest_cup-1) % l
    dest_index = cups.index(dest_cup) + 1
    cups.insert(dest_index, hold_out[0])
    cups.insert(dest_index+1, hold_out[1])
    cups.insert(dest_index+2, hold_out[2])
    cups.append(t)
    return cups


def dplay(cups, dest):
    c1 = cups[dest]
    c2 = cups[cups[dest]]
    c3 = cups[cups[cups[dest]]]
    c4 = cups[cups[cups[cups[dest]]]]

    search_val = (dest-1) % len(cups)
    while search_val in [c1, c2, c3]:
        search_val = (search_val-1) % len(cups)
    cups[c3] = cups[search_val]
    cups[search_val] = c1

    cups[dest] = c4
    dest = c4

    return cups, dest


if __name__ == "__main__":

    cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    cups = [8, 5, 3, 1, 9, 2, 6, 4, 7]

    cupsd = deque([i-1 for i in cups])
    for _ in range(10):
        cupsd = play(cupsd)
    print([cupsd.popleft()+1 for i in range(len(cups))])  # 97624853

    dcups = {}
    for i in range(len(cups)-1):
        dcups[cups[i]-1] = cups[i+1]-1
    dcups[cups[-1]-1] = cups[0]-1

    dest = cups[0]-1
    for _ in range(10):
        dcups, dest = dplay(dcups, dest)
    print(dcups)

    cups = cups + list(range(10, 1000001))
    for i in range(len(cups)-1):
        dcups[cups[i]-1] = cups[i+1]-1
    dcups[cups[-1]-1] = cups[0]-1

    dest = cups[0]-1
    print(len(dcups))
    for _ in tqdm(range(10000000)):
        dcups, dest = dplay(dcups, dest)
    print((dcups[0]+1)*(dcups[dcups[0]]+1))
