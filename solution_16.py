from itertools import permutations
import numpy as np


def read_file(file_name):
    section = 0
    rules = {}
    my_ticket = []
    tickets = []
    for line in open(file_name):
        if section == 0:
            if line.strip() == "":
                section = 1
                continue
            name, r = line.split(": ")
            first, second = r.split(" or ")
            rules[name] = [[int(first.split("-")[0]), int(first.split("-")[1])],
                           [int(second.split("-")[0]), int(second.split("-")[1])]]
        elif section == 1:
            if line.strip() == "":
                section = 2
                continue
            elif "your" not in line:
                my_ticket = [int(l) for l in line.strip().split(",")]
        else:
            if "nearby" not in line:
                ticket = [int(l) for l in line.strip().split(",")]
                tickets.append(ticket)

    return rules, my_ticket, tickets


def valid_item(limit1, limit2, t):
    if ((limit1[0] <= t <= limit1[1]) or
            (limit2[0] <= t <= limit2[1])):
        return True
    return False


def invalid_numbers(rules, ticket):
    invalid = []
    for t in ticket:
        valid = False
        for _, limits in rules.items():
            if valid_item(limits[0], limits[1], t):
                valid = True
                break
        if not valid:
            invalid.append(t)
    return invalid


def which_field(rule, valid_tickets):
    which = [1]*len(valid_tickets[0])
    for t in valid_tickets:
        for i in range(len(valid_tickets[0])):
            if not valid_item(rule[0], rule[1], t[i]):
                which[i] = 0
    return which


if __name__ == "__main__":

    file_name = "test_16.txt"
    file_name = "input_16.txt"

    rules, my_ticket, tickets = read_file(file_name)

    invalid_values = []
    valid_tickets = []
    for t in tickets:
        inv = invalid_numbers(rules, t)
        if len(inv) == 0:
            valid_tickets.append(t)
        invalid_values.extend(inv)
    print(sum(invalid_values))  # 20048

    whiches = [which_field(rule, valid_tickets) for _, rule in rules.items()]
    names = [rule_name for rule_name, _ in rules.items()]

    while True:
        for (w1, w2) in permutations(whiches, 2):
            if sum(w1) == 1:
                w2[w1.index(1)] = 0
        if sum([sum(x) for x in whiches]) == len(whiches):
            break

    muls = [my_ticket[which.index(1)] for name, which in zip(names, whiches) if "departure" in name]
    print(np.prod(muls)) # 4810284647569
