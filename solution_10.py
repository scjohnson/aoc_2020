import numpy


def count_valid(jolts):
    num_valid = 1
    dp = 0

    for i in range(len(jolts)-1):
        if jolts[i] + 1 == jolts[i+1]:
            dp += 1
        else:
            if dp:
                num_valid *= 2**(dp-1) - max(dp-3, 0)
            dp = 0
    return num_valid


if __name__ == "__main__":

    file_name = "test_10.txt"
    file_name = "input_10.txt"

    jolts = [int(line.strip()) for line in open(file_name)]
    jolts.append(0)
    jolts = sorted(jolts)
    jolts.append(jolts[-1]+3)
    diffs = numpy.diff(jolts)

    print(numpy.sum(diffs == 1)*numpy.sum(diffs == 3))
    print(count_valid(jolts))
