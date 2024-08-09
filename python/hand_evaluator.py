# hand_evaluator.py


def check_flush(card_list):
    print("flush checked")
    return all(card[1] == card_list[0][1] for card in card_list)


def check_straight(card_list):
    print("striaght checked")
    if check_wheel(card_list):
        return True
    return all(
        card_list[i][0] + 1 == card_list[i + 1][0] for i in range(len(card_list) - 1)
    )


def check_wheel(card_list):
    print("wheel checked")
    first_four = card_list[:-1]
    first_four_rank = [t[0] for t in first_four]
    if first_four_rank == [2, 3, 4, 5] and card_list[4][0] == 14:
        temp = card_list[4:] + first_four
        card_list = temp
        return True
    return False


def check_straight_flush(card_list):
    print("straight flush checked")
    return check_flush(card_list) and check_straight(card_list)


def check_four_of_kind(card_list):
    print("four kind checked")
    four_kind = None
    windowed_list = [card_list[i : i + 4] for i in range(len(card_list) - 4 + 1)]
    for window in windowed_list:
        if all([x[0] == window[0][0] for x in window]):
            four_kind = window
    if four_kind:
        temp_list = []
        temp_list += four_kind
        for card in card_list:
            if card not in temp_list:
                temp_list += [card]
        card_list = temp_list
        print(card_list)
        return True
    return False


def check_full_house(card_list):
    print("check full house")
    three_kind = None
    pair = None
    three_window = [card_list[i : i + 3] for i in range(len(card_list) - 3 + 1)]
    for window in three_window:
        if all([x[0] == window[0][0] for x in window]):
            three_kind = window
            break
    two_window = [card_list[i : i + 3] for i in range(len(card_list) - 3 + 1)]
    for window in two_window:
        if all([x[0] == window[0][0] for x in window]):
            pair = window
            break
    if three_kind and pair:
        card_list = three_kind + pair
        return True
    return False


def check_three_of_kind(card_list):
    print("check three kind")
    three_kind = None
    windowed_list = [card_list[i : i + 3] for i in range(len(card_list) - 3 + 1)]
    for window in windowed_list:
        if all([x[0] == window[0][0] for x in window]):
            three_kind = window
    if three_kind:
        temp_list = []
        temp_list += three_kind
        for card in card_list:
            if card not in temp_list:
                temp_list += card
        return True
    return False


def check_two_pair(card_list):
    print("check two pair")
    first_pair = None
    second_pair = None
    windowed_list = [card_list[i : i + 2] for i in range(len(card_list) - 2 + 1)]
    for window in windowed_list:
        if all([x[0] == window[0][0] for x in window]):
            if not first_pair:
                first_pair = window
            elif first_pair and not second_pair:
                second_pair = window
    if first_pair and second_pair:
        temp_list = first_pair + second_pair
        for card in card_list:
            if card not in temp_list:
                temp_list += card
        return True
    return False


def check_one_pair(card_list):
    print("check one pair")
    pair = None
    windowed_list = [card_list[i : i + 1] for i in range(len(card_list) - 1 + 1)]
    for window in windowed_list:
        if all([x[0] == window[0][0] for x in window]):
            pair = window
    if pair:
        tempList = pair
        for card in card_list:
            if card not in tempList:
                tempList += card
        return True
    return False
