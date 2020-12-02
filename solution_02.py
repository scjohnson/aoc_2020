

def valid_password2(password, low, high, letter):
    if (password[low-1] == letter) ^ (password[high-1] == letter):
        return True
    return False


def valid_password(password, low, high, letter):
    count = 0
    count = sum([c == letter for c in password])
    return count >= low and count <= high


def pass_policy(line):
    policy, password = [l.strip() for l in line.split(":")]
    nums, letter = policy.split(" ")
    low, high = [int(i) for i in nums.split("-")]
    return password, low, high, letter


if __name__ == "__main__":

    file_name = "test_02.txt"
    file_name = "input_02.txt"
    print(sum([valid_password(*(pass_policy(line)))
               for line in open(file_name)]))
    print(sum([valid_password2(*(pass_policy(line)))
               for line in open(file_name)]))
