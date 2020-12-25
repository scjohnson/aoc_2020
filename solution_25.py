
def handshake(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= subject_number
        value %= 20201227
    return value


def find_loop_size(subject_number, key):
    value = 1
    i = 0
    while value != key:
        i += 1
        value *= subject_number
        value %= 20201227
    return i


if __name__ == "__main__":
    # card_public_key = 5764801
    # door_public_key = 17807724
    card_public_key = 1614360
    door_public_key = 7734663
    card_loop_size = find_loop_size(7, card_public_key)
    door_loop_size = find_loop_size(7, door_public_key)

    encryption_key = handshake(door_public_key, card_loop_size)
    print(encryption_key)
    encryption_key = handshake(card_public_key, door_loop_size)
    print(encryption_key)
