
def read_bags(file_name):
    bags_structure = {}
    for line in open(file_name):
        line = line.strip()
        container, contains = line.split('bags contain')
        contains = contains.split(',')
        contains = [c.replace('bags', '').replace(
            'bag', '').replace('.', '').replace('no other', '').strip() for c in contains]
        bags_structure[container.strip()] = contains
    return bags_structure


def can_hold(bags_def, color):
    holders = []
    for container, contains in bags_def.items():
        if color in [c.split(" ", 1)[-1] for c in contains]:
            holders.append(container)
            holders.extend(can_hold(bags_def, container))
    return set(holders)


def num_contains(bags_def, color):
    num = 0
    for b in bags_def[color]:
        if b:
            num += int(b.split(' ', 1)[0])
            num += int(b.split(' ', 1)[0]) * \
                num_contains(bags_def, b.split(' ', 1)[-1])
    return num


if __name__ == "__main__":

    file_name = "test_07b.txt"
    file_name = "input_07.txt"

    bags_def = read_bags(file_name)

    print(len(can_hold(bags_def, "shiny gold")))  # 257
    print(num_contains(bags_def, "shiny gold"))  # 1038
