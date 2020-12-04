
def valid_value(key, value):
    if key == "byr":
        if int(value) < 1920 or int(value) > 2002:
            return False
    elif key == "iyr":
        if int(value) < 2010 or int(value) > 2020:
            return False
    elif key == "eyr":
        if int(value) < 2020 or int(value) > 2030:
            return False
    elif key == "hgt":
        if value[-2:] == "cm":
            if int(value[:-2]) < 150 or int(value[:-2]) > 193:
                return False
        elif value[-2:] == "in":
            if int(value[:-2]) < 59 or int(value[:-2]) > 76:
                return False
        else:
            return False
    elif key == "hcl":
        if len(value[1:]) != 6:
            return False
        a = int(value[1:], 16)
        for e in value[1:]:
            if e < '0' or e > 'f':
                return False
    elif key == "ecl":
        vals = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if value not in vals:
            return False
    elif key == "pid":
        if len(value) != 9:
            return False
        for v in value:
            if v < '0' or v > '9':
                return False
    return True


def valid_passport(passport):
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    valid2 = True
    for key, value in passport.items():
        if not valid_value(key, value):
            valid2 = False

    for req in required:
        if req not in passport:
            return False, valid2
    return True, valid2


def passports(file_name):
    passport = {}
    for line in open(file_name):
        if line.strip() == "":
            yield passport
            passport = {}
        else:
            for a in line.strip().split(" "):
                passport[a.split(":")[0]] = a.split(":")[1]
    yield passport


if __name__ == "__main__":

    file_name = "test_04.txt"
    file_name = "input_04.txt"

    passport = []
    valid, valid2 = 0, 0
    for passport in passports(file_name):
        v1, v2 = valid_passport(passport)
        if v1:
            valid += 1
            if v2:
                valid2 += 1

    print(valid, valid2)  # 254 184
