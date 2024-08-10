import re


### need to re sort the all the pairs
class Hand:

    def __init__(self, hand_string):
        self.card_list = []
        self.read_handstring(hand_string)
        self.hand_strength = -1  # 8 for SF 1 is highcard
        self.assign_hand_strength()

    def read_handstring(self, hand_string):
        rank_dict = {"a": 14, "k": 13, "q": 12, "j": 11, "t": 10}
        suit_pattern = r"[cdhs]"
        non_transformed = [item for item in re.split(suit_pattern, hand_string) if item]
        rank_list = []
        for char in non_transformed:
            if char in rank_dict:
                rank_list.append(rank_dict[char])
            else:
                rank_list.append(int(char))

        for rank in rank_list:
            if len(rank_list) != 5:
                raise ValueError("Wrong number of card rank")
            if rank < 2 or rank > 14:
                raise ValueError("Invalid card rank " + str(rank))

        suit_list = []
        for char in hand_string:
            if char in ["c", "d", "h", "s"]:
                suit_list.append(char)
        if len(suit_list) != 5:
            raise ValueError("Invalid number of card suits")

        self.card_list = list(zip(rank_list, suit_list))

        self.card_list.sort(key=lambda x: x[0])

        if any(self.card_list.count(x) > 1 for x in self.card_list):
            raise ValueError("duplicate cards")

    def assign_hand_strength(self):
        hand_checks = [
            (self.check_straight_flush, 8),  # Straight Flush
            (self.check_four_of_kind, 7),  # Four of a Kind
            (self.check_full_house, 6),  # Full House
            (self.check_flush, 5),  # Flush
            (self.check_straight, 4),  # Straight
            (self.check_three_of_kind, 3),  # Three of a Kind
            (self.check_two_pair, 2),  # Two Pair
            (self.check_one_pair, 1),  # One Pair
        ]

        for check_function, strength in hand_checks:
            if check_function():
                self.hand_strength = strength
                return

        self.hand_strength = 0  # High Card if no other hand is matched

    def compare(self, another):
        if not isinstance(another, Hand):
            raise TypeError("Not a Hand cannot be compared")
        if self.hand_strength > another.hand_strength:
            return 1
        elif self.hand_strength < another.hand_strength:
            return -1
        else:
            # compare the rank of each card one by one
            for i in range(5):
                if self.card_list[i][0] > another.card_list[i][0]:
                    return 1
                elif self.card_list[i][0] < another.card_list[i][0]:
                    return -1
        return 0

    def check_flush(self):
        return all(card[1] == self.card_list[0][1] for card in self.card_list)

    def check_straight(self):
        if self.check_wheel():
            return True
        return all(
            self.card_list[i][0] + 1 == self.card_list[i + 1][0]
            for i in range(len(self.card_list) - 1)
        )

    def check_wheel(self):
        first_four = self.card_list[:-1]
        first_four_rank = [t[0] for t in first_four]
        if first_four_rank == [2, 3, 4, 5] and self.card_list[4][0] == 14:
            temp = self.card_list[4:] + first_four
            self.card_list = temp
            return True
        return False

    def check_straight_flush(self):
        return self.check_flush() and self.check_straight()

    def check_four_of_kind(self):
        four_kind = None
        windowed_list = [
            self.card_list[i : i + 4] for i in range(len(self.card_list) - 4 + 1)
        ]
        for window in windowed_list:
            if all([x[0] == window[0][0] for x in window]):
                four_kind = window
        if four_kind:
            temp_list = []
            temp_list += four_kind
            for card in self.card_list:
                if card not in temp_list:
                    temp_list += [card]
            self.card_list = temp_list
            return True
        return False

    def check_full_house(self):
        rank_counts = {}  # Dictionary to count occurrences of each rank

        # Count occurrences of each rank
        for card in self.card_list:
            rank = card[0]
            rank_counts[rank] = rank_counts.get(rank, 0) + 1

        three_kind = None
        pair = None

        # Identify three of a kind and pair
        for rank, count in rank_counts.items():
            if count == 3:
                three_kind = [card for card in self.card_list if card[0] == rank]
            elif count == 2:
                pair = [card for card in self.card_list if card[0] == rank]

        # Check if both three of a kind and a pair are found
        if three_kind and pair:
            self.card_list = three_kind + pair
            return True

        return False

    def check_three_of_kind(self):
        three_kind = None
        windowed_list = [
            self.card_list[i : i + 3] for i in range(len(self.card_list) - 3 + 1)
        ]
        for window in windowed_list:
            if all([x[0] == window[0][0] for x in window]):
                three_kind = window
        if three_kind:
            temp_list = []
            temp_list += three_kind
            for card in self.card_list:
                if card not in temp_list:
                    temp_list += card
            return True
        return False

    def check_two_pair(self):
        first_pair = None
        second_pair = None
        windowed_list = [
            self.card_list[i : i + 2] for i in range(len(self.card_list) - 2 + 1)
        ]
        for window in windowed_list:
            if all([x[0] == window[0][0] for x in window]):
                if not first_pair:
                    first_pair = window
                elif first_pair and not second_pair:
                    second_pair = window
        if first_pair and second_pair:
            temp_list = first_pair + second_pair
            for card in self.card_list:
                if card not in temp_list:
                    temp_list += card
            return True
        return False

    def check_one_pair(self):
        pair = None
        windowed_list = [
            self.card_list[i : i + 2] for i in range(len(self.card_list) - 1)
        ]
        for window in windowed_list:
            if all([x[0] == window[0][0] for x in window]):
                pair = window
        if pair:
            tempList = pair
            for card in self.card_list:
                if card not in tempList:
                    tempList += card
            return True
        return False

    def print(self):
        print("printing")
        print(self.card_list)


hand = Hand("4d4s3s2djh")
