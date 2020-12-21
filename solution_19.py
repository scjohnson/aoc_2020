import regex


def rule(r):
    ret_rules = []
    sub_rules = r.split(" | ")
    for sub_rule in sub_rules:
        if "\"" in sub_rule:
            return sub_rule.strip()[1:-1]
        else:
            ret_rules.append([int(i) for i in sub_rule.split(" ")])
    return ret_rules


def consolidate_rules(rs):
    consolidated = {}
    unconsolidated = {}
    for k, v in rs.items():
        if type(v) == str:
            consolidated[k] = v
        else:
            unconsolidated[k] = v
    while len(unconsolidated) != 0:
        changed = False
        delete_items = []
        for k, v in unconsolidated.items():
            for i, sub_rule in enumerate(v):
                if all([item in consolidated for item in sub_rule]):
                    unconsolidated[k][i] = "".join([consolidated[i]
                                                    for i in sub_rule])
                    changed = True

            if all([type(sub_rule) == str for sub_rule in v]):
                consolidated[k] = "(" + "|".join(v) + ")"
                delete_items.append(k)
                changed = True
        for k in delete_items:
            del unconsolidated[k]
        if not changed:
            for k, v in unconsolidated.items():
                for _, sub_rule in enumerate(v):
                    for sr in sub_rule:
                        if k == sr:
                            consolidated[k] = '(?R)'
                            print("replacing: ", k)
            # return consolidated
            # print(unconsolidated)
    return consolidated


if __name__ == "__main__":

    file_name = "test_19b.txt"
    file_name = "input_19.txt"
    fixes = False

    rules = {}
    section = 1
    matches1 = 0
    matches2 = 0
    for line in open(file_name):
        if line.strip() == "":
            section = 2
            if fixes:
                rules[8] = [[42], [42, 8]]
                rules[11] = [[42, 31], [42, 11, 31]]
            rules = consolidate_rules(rules)
            continue
        if section == 1:
            rules[int(line.split(":")[0])] = rule(line.split(":")[1].strip())
        else:
            if regex.search("^" + rules[8], line.strip()):
                a = regex.search("^" + rules[8], line.strip())
                if regex.match("^" + rules[11] + "$", line.strip()[len(a.group(0)):]):
                    matches1 += 1

            loc = 0
            num_42s = 0
            num_31s = 0
            line = line.strip()
            while regex.search("^" + rules[42], line[loc:]):
                loc += len(regex.search("^" + rules[42], line[loc:]).group(0))
                num_42s += 1
            if num_42s > 0:
                while regex.search("^" + rules[31], line[loc:]):
                    loc += len(regex.search("^" +
                                            rules[31], line[loc:]).group(0))
                    num_31s += 1
                if num_42s > num_31s and num_31s > 0 and loc == len(line):
                    matches2 += 1

    print(matches1)  # 107
    print(matches2)  # 321
