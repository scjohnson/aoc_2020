

def valid_password2(password, policy):
    nums, letter = policy.split(" ")
    low, high = [int(i) for i in nums.split("-")]
    if (password[low-1] == letter) ^ (password[high-1] == letter):
        return True
    return False


def valid_password(password, policy):
    nums, letter = policy.split(" ")
    low, high = [int(i) for i in nums.split("-")]
    count = 0
    for c in password:
        if c == letter:
            count += 1
    return count >= low and count <= high


if __name__ == "__main__":

    file_name = "test_02.txt"
    file_name = "input_02.txt"
    valid = 0
    valid2 = 0
    for line in open(file_name):
        policy, password = [l.strip() for l in line.split(":")]
        if valid_password(password, policy):
            valid += 1
        if valid_password2(password, policy):
            valid2 += 1
    print(valid, valid2)