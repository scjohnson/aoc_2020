
def num_trees(rows, right, down):
    y = 0
    trees = 0
    for row_num, row in enumerate(rows):
        if row_num % down != 0:
            continue
        if row[y] == '#':
            trees += 1
        y = (y+right)%len(row)
    return trees


if __name__ == "__main__":

    file_name = "test_03.txt"
    file_name = "input_03.txt"

    rows = [line.strip() for line in open(file_name)]
    print(num_trees(rows, 3, 1))
    print(num_trees(rows, 1, 1)*num_trees(rows, 3, 1)*num_trees(rows, 5, 1)
          * num_trees(rows, 7, 1)*num_trees(rows, 1, 2))
