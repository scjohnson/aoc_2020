
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
    priors1 = []
    priors2 = []
    while deck1 and deck2:
        if deck1 in priors1 and deck2 in priors2:
            return deck1, 1
        priors1.append(deck1[:])
        priors2.append(deck2[:])
        if deck1[0] >= len(deck1) or deck2[0] >= len(deck2):
            if deck1[0] > deck2[0]:
                deck1.append(deck1.pop(0))
                deck1.append(deck2.pop(0))
            else:
                deck2.append(deck2.pop(0))
                deck2.append(deck1.pop(0))
        else:
            _, winner = play_recursive(
                deck1[1:deck1[0]+1], deck2[1:deck2[0]+1])
            if winner == 1:
                deck1.append(deck1.pop(0))
                deck1.append(deck2.pop(0))
            else:
                deck2.append(deck2.pop(0))
                deck2.append(deck1.pop(0))
    if deck2:
        return deck2, 2
    return deck1, 1


if __name__ == "__main__":

    file_name = "test_22.txt"
    file_name = "input_22.txt"

    deck1, deck2 = read_decks(file_name)
    winning_deck = play(deck1, deck2)
    winning_deck.reverse()
    # 32033
    print(sum([x*y for x, y in zip(winning_deck, range(1, len(winning_deck)+1))]))

    deck1, deck2 = read_decks(file_name)
    winning_deck, winner = play_recursive(deck1, deck2)
    winning_deck.reverse()
    print(sum([x*y for x, y in zip(winning_deck, range(1, len(winning_deck)+1))]))
    # 34901
