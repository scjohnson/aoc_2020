import itertools
if __name__ == "__main__":

    file_name = "test_01.txt"
    file_name = "input_01.txt"
    
    nums = [int(line) for line in open(file_name)]

    for pair in itertools.product(nums, repeat=2):
        if pair[0]+pair[1] == 2020:
            print(pair[0]*pair[1])
            break

    for pair in itertools.product(nums, repeat=3):
        if pair[0]+pair[1]+pair[2] == 2020:
            print(pair[0]*pair[1]*pair[2])
            break