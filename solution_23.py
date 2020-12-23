from tqdm import tqdm


def dplay(cups, dest):
    c1 = cups[dest]
    c2 = cups[c1]
    c3 = cups[c2]
    cups[dest] = cups[c3]

    search_val = (dest-1) % len(cups)
    while search_val in [c1, c2, c3]:
        search_val = (search_val-1) % len(cups)

    cups[c3] = cups[search_val]
    cups[search_val] = c1
    dest = cups[dest]

    return cups, dest


def list_to_dict(l):
    dcups = {}
    for i in range(len(cups)-1):
        dcups[cups[i]-1] = cups[i+1]-1
    dcups[cups[-1]-1] = cups[0]-1
    return dcups


if __name__ == "__main__":

    # cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    cups = [8, 5, 3, 1, 9, 2, 6, 4, 7]

    dcups = list_to_dict(cups)
    dest = cups[0]-1
    for _ in tqdm(range(100)):
        dcups, dest = dplay(dcups, dest)

    res = [0]
    for _ in range(8):
        res.append(dcups[res[-1]])
    print("".join([str(s+1) for s in res[1:]]))  # 97624853

    cups=cups + list(range(10, 1000001))

    dcups=list_to_dict(cups)
    dest=cups[0]-1
    for _ in tqdm(range(10000000)):
        dcups, dest=dplay(dcups, dest)
    print((dcups[0]+1)*(dcups[dcups[0]]+1))  # 664642452305
