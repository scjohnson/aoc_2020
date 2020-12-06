import numpy


def score2(group):
    s = {}
    for c in range(ord('a'), ord('z')+1):
        s[chr(c)] = 0
    for person in group:
        for c in person:
            s[c] += 1
    return sum([s[k] == len(group) for k in s])


def score(group):
    s = {}
    for person in group:
        for c in person:
            s[c] = 1
    return sum([s[k] for k in s])


def groups(file_name):
    group = []
    for line in open(file_name):
        if line.strip() == "":
            yield group
            group = []
        else:
            group.append(line.strip())
    yield group


if __name__ == "__main__":

    file_name = "test_06.txt"
    file_name = "input_06.txt"

    scores = [score(group) for group in groups(file_name)]
    scores2 = [score2(group) for group in groups(file_name)]
    print(sum(scores))
    print(sum(scores2))
