import unittest
from engine import Hand


class TestHandMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_straight_with_low_hand(self):
        hand = Hand("7d6h5s4c3d")
        self.assertEqual(hand.hand_strength, 4)

    def test_straight_with_high_hand(self):
        hand2 = Hand("qcjh10s9h8d")
        self.assertEqual(hand2.hand_strength, 4)

    def test_straight_with_ace_low_hand(self):
        hand3 = Hand("ah4d5s3c2h")
        self.assertEqual(hand3.hand_strength, 4)

    # Straight Flush Test
    def test_straight_flush(self):
        hand = Hand("ad2d3d4d5d")
        self.assertEqual(hand.hand_strength, 8)

    # Four of a Kind Tests
    def test_four_of_a_kind(self):
        hand = Hand("4s4hjs4c4d")
        self.assertEqual(hand.hand_strength, 7)

    def test_not_four_of_a_kind(self):
        not_four = Hand("ad2d3d4d5d")
        self.assertNotEqual(not_four.hand_strength, 7)

    # Full House Test
    def test_full_house(self):
        hand = Hand("2s2c2h5h5d")
        self.assertEqual(hand.hand_strength, 6)

    # Two Pair Tests
    def test_two_pair(self):
        hand = Hand("2c2s5hkhkd")
        self.assertEqual(hand.hand_strength, 2)

    def test_two_pair_with_face_cards(self):
        hand2 = Hand("5sks5dkdqs")
        self.assertEqual(hand2.hand_strength, 2)

    def test_not_two_pair(self):
        not_hand = Hand("2s5c7s8dkh")
        self.assertNotEqual(not_hand.hand_strength, 2)

    # One Pair Test
    def test_one_pair(self):
        hand = Hand("3c3d5d7sad")
        self.assertEqual(hand.hand_strength, 1)

    # Three of a Kind Tests
    def test_three_of_a_kind(self):
        hand = Hand("8s8d8h3c2d")
        self.assertEqual(hand.hand_strength, 3)

    def test_not_three_of_a_kind(self):
        not_hand = Hand("7c7d5h5s2s")
        self.assertNotEqual(not_hand.hand_strength, 3)

    # High Card Tests
    def test_high_card_with_ace(self):
        hand = Hand("ahksqdjc9s")
        self.assertEqual(hand.hand_strength, 0)  # Assuming high card is the lowest rank with strength 0

    def test_high_card_with_low_cards(self):
        hand = Hand("2c4h6s8dkd")
        self.assertEqual(hand.hand_strength, 0)  # Assuming high card is the lowest rank with strength 0
        
    def test_compare_high_card_equal(self):
        hand1 = Hand("ahkdqcjd9s")  # High card: Ace, King, Queen, Jack, 9
        hand2 = Hand("adkhqcjs9d")  # High card: Ace, King, Queen, Jack, 9
        self.assertEqual(hand1.compare(hand2), 0)

    def test_compare_high_card_higher_wins(self):
        hand1 = Hand("ahkdqcjd8s")  # High card: Ace, King, Queen, Jack, 8
        hand2 = Hand("ahkdqcjd9s")  # High card: Ace, King, Queen, Jack, 9
        self.assertEqual(hand1.compare(hand2), -1)

    # One Pair Tests
    def test_compare_one_pair_equal(self):
        hand1 = Hand("3s3d5h7c9d")  # Pair of 3s
        hand2 = Hand("3h3c5d7s9c")  # Pair of 3s
        self.assertEqual(hand1.compare(hand2), 0)

    def test_compare_one_pair_higher_wins(self):
        hand1 = Hand("3s3d5h7c9d")  # Pair of 3s
        hand2 = Hand("4h4c5d7s9c")  # Pair of 4s
        self.assertEqual(hand1.compare(hand2), -1)

    # Two Pair Tests
    def test_compare_two_pair_equal(self):
        hand1 = Hand("3s3d5h5c9d")  # Two pair: 3s and 5s
        hand2 = Hand("3h3c5s5d9c")  # Two pair: 3s and 5s
        self.assertEqual(hand1.compare(hand2), 0)

    def test_compare_two_pair_higher_wins(self):
        hand1 = Hand("3s3d5h5c9d")  # Two pair: 3s and 5s
        hand2 = Hand("4h4c5s5d9c")  # Two pair: 4s and 5s
        self.assertEqual(hand1.compare(hand2), -1)

    # Three of a Kind Tests
    def test_compare_three_of_a_kind_equal(self):
        hand1 = Hand("8s8d8h3c2d")  # Three of a kind: 8s
        hand2 = Hand("8c8h8d4s2c")  # Three of a kind: 8s
        self.assertEqual(hand1.compare(hand2), 0)

    def test_compare_three_of_a_kind_higher_wins(self):
        hand1 = Hand("7s7d7h3c2d")  # Three of a kind: 7s
        hand2 = Hand("8c8h8d4s2c")  # Three of a kind: 8s
        self.assertEqual(hand1.compare(hand2), -1)

    # Straight Tests
    def test_compare_straight_equal(self):
        hand1 = Hand("5s6d7h8c9d")  # 9-high straight
        hand2 = Hand("5h6c7d8s9c")  # 9-high straight
        self.assertEqual(hand1.compare(hand2), 0)

    def test_compare_straight_higher_wins(self):
        hand1 = Hand("5s6d7h8c9d")  # 9-high straight
        hand2 = Hand("6h7c8d9sTc")  # 10-high straight
        self.assertEqual(hand1.compare(hand2), -1)

    # Flush Tests
    def test_compare_flush_equal(self):
        hand1 = Hand("2s4s6s8sTs")  # Flush with Ts high
        hand2 = Hand("2d4d6d8dTd")  # Flush with Ts high
        self.assertEqual(hand1.compare(hand2), 0)

    def test_compare_flush_higher_wins(self):
        hand1 = Hand("2s4s6s8s9s")  # Flush with 9s high
        hand2 = Hand("2d4d6d8dTs")  # Flush with Ts high
        self.assertEqual(hand1.compare(hand2), -1)

    # Full House Tests
    def test_compare_full_house_equal(self):
        hand1 = Hand("3s3c3h5s5d")  # Full House: 3s over 5s
        hand2 = Hand("3d3h3c5d5h")  # Full House: 3s over 5s
        self.assertEqual(hand1.compare(hand2), 0)

    def test_compare_full_house_higher_wins(self):
        hand1 = Hand("3s3c3h5s5d")  # Full House: 3s over 5s
        hand2 = Hand("4d4h4c5d5h")  # Full House: 4s over 5s
        self.assertEqual(hand1.compare(hand2), -1)

    # Four of a Kind Tests
    def test_compare_four_of_a_kind_equal(self):
        hand1 = Hand("4s4hjs4c4d")  # Four of a kind: 4s
        hand2 = Hand("4h4d4c4s7s")  # Four of a kind: 4s
        self.assertEqual(hand1.compare(hand2), 0)

    def test_compare_four_of_a_kind_higher_wins(self):
        hand1 = Hand("3s3h3d3c5h")  # Four of a kind: 3s
        hand2 = Hand("4h4d4c4s7s")  # Four of a kind: 4s
        self.assertEqual(hand1.compare(hand2), -1)

    # Straight Flush Tests
    def test_compare_straight_flush_equal(self):
        hand1 = Hand("5s6s7s8s9s")  # 9-high straight flush
        hand2 = Hand("5h6h7h8h9h")  # 9-high straight flush
        self.assertEqual(hand1.compare(hand2), 0)

    def test_compare_straight_flush_higher_wins(self):
        hand1 = Hand("5s6s7s8s9s")  # 9-high straight flush
        hand2 = Hand("6h7h8h9hTh")  # 10-high straight flush
        self.assertEqual(hand1.compare(hand2), -1)


if __name__ == "__main__":
    unittest.main()
