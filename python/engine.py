import re
import helper as h
rank_dict = {"a": 14, "k": 13, "q": 12, "j": 11, "t": 10}
suit_dict = {"c": 1, "d": 2, "h": 3, "s": 4}
inv_rank = {v: k for k, v in rank_dict.items()}
inv_suit = {v: k for k, v in suit_dict.items()}
hand_str_dict = {0: "high card", 1: "one pair", 2: "two pair", 3: "three of a kind",
                 4: "straight", 5: "flush", 6: "full house", 7: "four of a kind", 8: "straight flush"}
# need to re sort the all the pairs


class Hand:

    def __init__(self, hand_string):
        self.card_list = []
        self.rank_counts = None
        self.read_handstring(hand_string)
        self.hand_strength = -1  # 8 for SF 1 is highcard
        self.assign_hand_strength()

    def read_handstring(self, hand_string):
        suit_pattern = r"[cdhs]"
        non_transformed = [item for item in re.split(
            suit_pattern, hand_string) if item]
        rank_list = []
        for char in non_transformed:
            if char in rank_dict:
                rank_list.append(rank_dict[char])
            else:
                # put the number rank in, transform a,k,q,j to number
                rank_list.append(int(char))

        if len(rank_list) != 5:
            raise ValueError("Wrong number of card rank")
        for rank in rank_list:
            if rank < 2 or rank > 14:
                raise ValueError("Invalid card rank " + str(rank))

        suit_list = [

        ]
        for char in hand_string:
            if char in ["c", "d", "h", "s"]:
                suit_list.append(suit_dict[char])
        if len(suit_list) != 5:
            raise ValueError("Invalid number of card suits")

        self.card_list = list(zip(rank_list, suit_list))

        # change to sort by rank as well
        self.card_list.sort(key=lambda x: (x[0], x[1]), reverse=True)

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
            raise TypeError("Cannot compare with a non-Hand object")

        if self.hand_strength > another.hand_strength:
            return 1
        elif self.hand_strength < another.hand_strength:
            return -1
        else:
            compare_funcs_dict = [
                (self.compare_one_pair, 1),
                (self.compare_two_pair, 2),
                (self.compare_sets, 3),
                (self.compare_straight, 4),
                (self.compare_flush, 5),
                (self.compare_four_and_full, 6),
                (self.compare_four_and_full, 7),
                (self.compare_straight, 8)
            ]

            # Compare based on the hand strength and the corresponding function
            for comp_func, hand_strength in compare_funcs_dict:
                if self.hand_strength == hand_strength:
                    return comp_func(another)

            # Fallback comparison for high card
            return h.compare_cards(self.card_list, another.card_list)

# these functions check wheter a hand has a specific hand strength

    def check_flush(self):
        return all(card[1] == self.card_list[0][1] for card in self.card_list)

    def check_straight(self):
        if self.check_wheel():
            return True
        return all(
            self.card_list[i][0] - 1 == self.card_list[i + 1][0]
            for i in range(len(self.card_list) - 1)
        )

    def check_wheel(self):
        return [t[0] for t in self.card_list] == [14, 5, 4, 3, 2]

    def check_straight_flush(self):
        return self.check_flush() and self.check_straight()

    def check_four_of_kind(self):
        self.get_rank_counts()

        for rank, count in self.rank_counts.items():
            if count == 4:
                return True
        return False

    def check_full_house(self):
        self.get_rank_counts()

        three_kind = False
        pair = False

        # Identify three of a kind and pair
        for rank, count in self.rank_counts.items():
            if count == 3:
                three_kind = True
            elif count == 2:
                pair = True

        # Check if both three of a kind and a pair are found
        if three_kind and pair:
            return True

        return False

    def check_three_of_kind(self):
        self.get_rank_counts()

        for rank, count in self.rank_counts.items():
            if count == 3:
                return True
        return False

    def check_two_pair(self):
        self.get_rank_counts()
        pair_count = 0

        for rank, count in self.rank_counts.items():
            if count == 2:
                pair_count += 1
        if pair_count == 2:
            return True
        return False

    def check_one_pair(self):
        self.get_rank_counts()

        for rank, count in self.rank_counts.items():
            if count == 2:
                return True
        return False

# end of check functions

    def compare_one_pair(self, another):
        if not isinstance(another, Hand):
            raise TypeError("Not a Hand cannot be compared")
        self_pair = self.get_pair()[0]
        another_pair = another.get_pair()[0]
        if self_pair > another_pair:
            return 1
        elif self_pair < another_pair:
            return -1
        else:
            return h.compare_ranks(h.filter_cards(self.card_list, [self_pair]), h.filter_cards(another.card_list, [another_pair]))

    def compare_two_pair(self, another):
        if not isinstance(another, Hand):
            raise TypeError("Not a Hand cannot be compared")
        self_pairs = self.get_pair()
        another_pairs = another.get_pair()
        pair_result = h.compare_ranks(self_pairs, another_pairs)
        if pair_result != 0:
            return pair_result
        else:
            # if both two pair are the same compare kicker
            return h.compare_ranks(h.filter_cards(self.card_list, self_pairs), h.filter_cards(another.card_list, self_pairs))

    def compare_sets(self, another):
        if not isinstance(another, Hand):
            raise TypeError("Not a Hand cannot be compared")
        self_set = self.get_set()
        another_set = another.get_set()
        set_compared = h.compare_ranks([self_set], [another_set])
        if set_compared != 0:
            return set_compared
        else:
            return h.compare_ranks(h.filter_cards(self.card_list, [self_set]), h.filter_cards(another.card_list, [self_set]))

    def compare_straight(self, another):
        if not isinstance(another, Hand):
            raise TypeError("Not a Hand cannot be compared")
        if self.card_list[0][0] == 14 or self.card_list[0][0]:
            return h.compare_by_index(self.card_list, another.card_list, 1)
        return h.compare_by_index(self.card_list, another.card_list, 0)

    def compare_flush(self, another):
        if not isinstance(another, Hand):
            raise TypeError("Not a Hand cannot be compared")
        return h.compare_by_index(self.card_list, another.card_list, 0)

    def compare_four_and_full(self, another):
        if not isinstance(another, Hand):
            raise TypeError("Not a Hand cannot be compared")
        four_kind_result = h.compare_by_index(
            self.card_list, another.card_list, 2)
        if four_kind_result != 0:
            return four_kind_result
        first_card_result = h.compare_by_index(
            self.card_list, another.card_list, 0)
        if first_card_result != 0:
            return first_card_result
        return h.compare_by_index(self.card_list, another.card_list, 4)

    def get_rank_counts(self):
        if not self.rank_counts:
            self.rank_counts = {}  # Dictionary to count occurrences of each rank

            # Count occurrences of each rank
            for card in self.card_list:
                rank = card[0]
                self.rank_counts[rank] = self.rank_counts.get(rank, 0) + 1

    # return array of pairs found
    def get_pair(self):
        self.get_rank_counts()
        result = []
        for rank, count in self.rank_counts.items():
            if count == 2:
                result.append(rank)
        if len(result) == 1:
            return result
        elif len(result) > 1:
            result.sort(reverse=True)
            return result
        return None

    def get_set(self):
        self.get_rank_counts()
        for rank, count in self.rank_counts.items():
            if count == 3:
                return rank
        return None

    def print(self):
        printString = ""
        for card in self.card_list:
            rank = card[0]
            suit = card[1]
            if rank not in inv_rank:
                printString += str(rank)
            else:
                printString += inv_rank[rank]
            printString += inv_suit[suit]
            printString = printString + " "

    def print_handStrength(self):
        print(hand_str_dict[self.hand_strength])
