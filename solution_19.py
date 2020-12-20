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
            print(unconsolidated)
            # return consolidated
    return consolidated


if __name__ == "__main__":

    file_name = "test_19b.txt"
    file_name = "input_19.txt"
    fixes = True

    rules = {}
    section = 1
    matches = 0
    for line in open(file_name):
        if line.strip() == "":
            section = 2
            if fixes:
                rules[8] = [[42], [42, 8]]
                rules[11] = [[42, 31], [42, 11, 31]]
            rules = consolidate_rules(rules)
            rules[0] = str.replace(rules[0], '?R', '?1', 1)
            rules[0] = str.replace(rules[0], '?R', '?2', 1)
            continue
        if section == 1:
            rules[int(line.split(":")[0])] = rule(line.split(":")[1].strip())
        else:
            if regex.search("^" + rules[8], line.strip()):
                a = regex.search("^" + rules[8], line.strip())
                if regex.search("^" + rules[11] + "$", line.strip()[len(a.group(0)):]):
                    matches += 1
    # problem 1: 107
    print(matches) # x > 180
