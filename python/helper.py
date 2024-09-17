# hand_evaluator.py

# given two card lists compare them card by card by their rank
def compare_cards(this, other):
    if len(this) != len(other):
        raise ValueError("Different length of list")
    # error not equal length
    for i in range(len(this)):
        if this[i][0] > other[i][0]:
            return 1
        elif this[i][0] < other[i][0]:
            return -1
    return 0

# given two list of ranks


def compare_ranks(this, other):
    if len(this) != len(other):
        raise ValueError("Different length of list")
    # error not equal length
    for i in range(len(this)):
        if this[i] > other[i]:
            return 1
        elif this[i] < other[i]:
            return -1
    return 0


def compare_by_index(this, other, index):
    if len(this) != len(other):
        raise ValueError("Different length of list")
    this_rank = this[index][0]
    other_rank = other[index][0]
    if this_rank > other_rank:
        return 1
    elif this_rank == other_rank:
        return 0
    else:
        return -1

# this function removes cards that has the same rank as filter_rank


def filter_cards(card_list, filter_ranks):
    if not isinstance(card_list, list):
        raise TypeError("not a list")
    return [card[0] for card in card_list if card[0] not in filter_ranks]
