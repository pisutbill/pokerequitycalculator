import re

rank_dict = {"a": 14, "k": 13, "q": 12, "j": 11, "t": 10}
suit_dict = {"c": 1, "d": 2, "h": 3, "s": 4}
inv_rank = {v: k for k, v in rank_dict.items()}
inv_suit = {v: k for k, v in suit_dict.items()}
hand_str_dict = {0: "high card", 1: "one pair", 2: "two pair", 3: "three of a kind", 4: "straight", 5: "flush", 6: "full house", 7: "four of a kind", 8: "straight flush"}
### need to re sort the all the pairs
class Hand:

    def __init__(self, hand_string):
        self.card_list = []
        self.read_handstring(hand_string)
        self.hand_strength = -1  # 8 for SF 1 is highcard
        self.assign_hand_strength()

    def read_handstring(self, hand_string):
        suit_pattern = r"[cdhs]"
        non_transformed = [item for item in re.split(suit_pattern, hand_string) if item]
        rank_list = []
        for char in non_transformed:
            if char in rank_dict:
                rank_list.append(rank_dict[char])
            else:
                rank_list.append(int(char)) #put the number rank in, transform a,k,q,j to number

        if len(rank_list) != 5:
                raise ValueError("Wrong number of card rank")
        for rank in rank_list:
            if rank < 2 or rank > 14:
                raise ValueError("Invalid card rank " + str(rank))

        suit_list = []
        for char in hand_string:
            if char in ["c", "d", "h", "s"]:
                suit_list.append(suit_dict[char])
        if len(suit_list) != 5:
            raise ValueError("Invalid number of card suits")

        self.card_list = list(zip(rank_list, suit_list))
    

        self.card_list.sort(key=lambda x: (x[0], x[1])) #change to sort by rank as well

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
        return first_four_rank == [2, 3, 4, 5] and self.card_list[4][0] == 14

    def check_straight_flush(self):
        return self.check_flush() and self.check_straight()

    def check_four_of_kind(self):
        rank_count = self.get_rank_counts()

        for rank,count in rank_count.items():
            if count == 4:
                return True
        return False

    def check_full_house(self):
        rank_counts = {}  # Dictionary to count occurrences of each rank

        # Count occurrences of each rank
        for card in self.card_list:
            rank = card[0]
            rank_counts[rank] = rank_counts.get(rank, 0) + 1

        three_kind = False
        pair = False

        # Identify three of a kind and pair
        for rank, count in rank_counts.items():
            if count == 3:
                three_kind = True
            elif count == 2:
                pair = True

        # Check if both three of a kind and a pair are found
        if three_kind and pair:
            return True

        return False

    def check_three_of_kind(self):
        rank_count = self.get_rank_counts()

        for rank,count in rank_count.items():
            if count == 3:
                return True
        return False

    def check_two_pair(self):
        rank_count = self.get_rank_counts()
        pair_count = 0

        for rank,count in rank_count.items():
            if count == 2:
                pair_count += 1
        if pair_count == 2:
            return True
        return False


    def check_one_pair(self):
        rank_count = self.get_rank_counts()

        for rank,count in rank_count.items():
            if count == 2:
                return True
        return False

    def compare_one_pair(self, another):
        pass

    def get_rank_counts(self):
        rank_counts = {}  # Dictionary to count occurrences of each rank

        # Count occurrences of each rank
        for card in self.card_list:
            rank = card[0]
            rank_counts[rank] = rank_counts.get(rank, 0) + 1
        return rank_counts

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



hand = Hand("2h3d5sac4s")
