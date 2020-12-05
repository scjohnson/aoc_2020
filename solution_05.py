import numpy


def seat_id(rc):
    return rc[0]*8+rc[1]


def row_column(boarding_pass):
    rows = numpy.array(range(0, 128))
    cols = numpy.array(range(0, 8))
    for c in boarding_pass:
        if c == 'F':
            rows = numpy.split(rows, 2)[0]
        elif c == 'B':
            rows = numpy.split(rows, 2)[1]
        elif c == 'L':
            cols = numpy.split(cols, 2)[0]
        elif c == 'R':
            cols = numpy.split(cols, 2)[1]
    return rows[0], cols[0]


def boarding_passes(file_name):
    for line in open(file_name):
        yield line.strip()


if __name__ == "__main__":

    file_name = "test_05.txt"
    file_name = "input_05.txt"

    seat_ids = [seat_id(row_column(boarding_pass))
                for boarding_pass in boarding_passes(file_name)]
    print(max(seat_ids))  # 996
    seat_ids = numpy.sort(seat_ids)
    diffs = numpy.diff(seat_ids)
    print(seat_ids[numpy.where(diffs == max(diffs))] + 1)
