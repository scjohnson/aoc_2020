if __name__ == "__main__":

    input = [9, 12, 1, 4, 17, 0, 18]

    # final_round = 2020
    final_round = 30000000

    last_round = {}
    for i, j in enumerate(input):
        last_round[j] = i

    last = input[-1]

    for i in range(len(input), final_round):
        last_last = last
        if last_last in last_round:
            last = (i-last_round[last]-1)
        else:
            last = 0
        last_round[last_last] = i-1
    print(last)
