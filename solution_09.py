
from itertools import combinations
import numpy


def contiguous_set(data, invalid_number):
    i = 1
    sums = numpy.array(data)
    while len(sums) > 1:
        sums = numpy.add(sums[0:-1], data[i:])
        if invalid_number in sums:
            index = numpy.where(sums == invalid_number)[0][0]
            return data[index:index+i]
        i += 1


def check_data(data, preamble_length):
    for i in range(preamble_length, len(data)):
        if data[i] not in [i+j for (i, j) in combinations(data[i-preamble_length:i], 2)]:
            return data[i]


if __name__ == "__main__":

    file_name = "input_09.txt"
    data = [int(line.strip()) for line in open(file_name)]

    invalid_number = check_data(data, 25)
    print(invalid_number)

    hack_list = contiguous_set(data, invalid_number)
    print(min(hack_list)+max(hack_list))
