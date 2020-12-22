
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
    while len(deck1) != 0 and len(deck2) != 0:
        if deck1[0] > deck2[0]:
            deck1.append(deck1.pop(0))
            deck1.append(deck2.pop(0))
        else:
            deck2.append(deck2.pop(0))
            deck2.append(deck1.pop(0))
    if len(deck2) > 0:
        return deck2
    return deck1


if __name__ == "__main__":

    file_name = "test_22.txt"
    file_name = "input_22.txt"

    deck1, deck2 = read_decks(file_name)
    winning_deck = play(deck1, deck2)
    winning_deck.reverse()
    print(sum([x*y for x, y in zip(winning_deck, range(1, len(winning_deck)+1))]))
