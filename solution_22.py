
def read_decks(file):
    deck1 = []
    deck = []
    for line in open(file):
        if line.strip() == "":
            deck1 = deck
            deck = []
        elif "Player" in line:
            continue
        else:
            deck.append(int(line.strip()))
    return deck1, deck


def play(deck1, deck2):
    while deck1 and deck2:
        if deck1[0] > deck2[0]:
            deck1.append(deck1.pop(0))
            deck1.append(deck2.pop(0))
        else:
            deck2.append(deck2.pop(0))
            deck2.append(deck1.pop(0))
    return deck2 if deck2 else deck1


def play_recursive(deck1, deck2):
    priors = set()
    while deck1 and deck2:

        orientation = hash(tuple(deck1[:] + [-1] + deck2[:]))
        if orientation in priors:
            return deck1, 1
        priors.add(orientation)

        c1 = deck1.pop(0)
        c2 = deck2.pop(0)

        winner = 1
        if c1 > len(deck1) or c2 > len(deck2):
            winner = 1 if c1 > c2 else 2
        else:
            _, winner = play_recursive(deck1[0:c1], deck2[0:c2])

        if winner == 1:
            deck1.append(c1)
            deck1.append(c2)
        else:
            deck2.append(c2)
            deck2.append(c1)

    return (deck2, 2) if deck2 else (deck1, 1)


def score(deck):
    return sum([x*y for x, y in zip(winning_deck, range(len(winning_deck), 0, -1))])


if __name__ == "__main__":

    file_name = "test_22.txt"
    file_name = "input_22.txt"

    deck1, deck2 = read_decks(file_name)
    winning_deck = play(deck1, deck2)
    # 32033
    print(score(winning_deck))

    deck1, deck2 = read_decks(file_name)
    winning_deck, _ = play_recursive(deck1, deck2)
    # 34901
    print(score(winning_deck))
