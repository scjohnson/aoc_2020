from itertools import permutations


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
            elif "your" not in line.strip():
                my_ticket = [int(l) for l in line.strip().split(",")]
        elif section == 2:
            if "nearby" not in line.strip():
                ticket = [int(l) for l in line.strip().split(",")]
                tickets.append(ticket)

    return rules, my_ticket, tickets


def invalid_numbers(rules, ticket):
    invalid = []
    for t in ticket:
        valid = False
        for _, limits in rules.items():
            if ((t >= limits[0][0] and t <= limits[0][1]) or
                    (t >= limits[1][0] and t <= limits[1][1])):
                valid = True
                break
        if not valid:
            invalid.append(t)
    return invalid


def which_field(rule, valid_tickets):
    which = [1]*len(valid_tickets[0])
    for t in valid_tickets:
        for i in range(len(valid_tickets[0])):
            if ((t[i] < rule[0][0] or t[i] > rule[0][1]) and
                    (t[i] < rule[1][0] or t[i] > rule[1][1])):
                which[i] = 0
    return which


if __name__ == "__main__":

    file_name = "test_16.txt"
    file_name = "input_16.txt"

    rules, my_ticket, tickets = read_file(file_name)
    invalid = []
    valid_tickets = []
    for t in tickets:
        inv = invalid_numbers(rules, t)
        if len(inv) == 0:
            valid_tickets.append(t)
        invalid.extend(invalid_numbers(rules, t))
    print(sum(invalid))  # 20048

    whiches = []
    names = []
    for rule_name, rule in rules.items():
        whiches.append(which_field(rule, valid_tickets))
        names.append(rule_name)

    while True:
        for (w1, w2) in permutations(whiches, 2):
            if sum(w1) == 1:
                w2[w1.index(1)] = 0
        if sum([sum(x) for x in whiches]) == len(whiches):
            break

    mul = 1
    for name, which in zip(names, whiches):
        if "departure" in name:
            mul *= my_ticket[which.index(1)]
    print(mul)  # 4810284647569
