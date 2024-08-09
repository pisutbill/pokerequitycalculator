import unittest
from engine import Hand


class TestHandMethods(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_wheel(self):
        hand = Hand('ad3c2s5d4h')
        self.assertTrue(hand.check_wheel())
    
    def test_not_wheel(self):
        hand = Hand('ad3c2s7d4h')
        self.assertFalse(hand.check_wheel())

    def test_check_straight(self):
        hand = Hand('7d6h5s4c3d')
        self.assertTrue(hand.check_straight())
        hand2 = Hand('qcjh10s9h8d')
        self.assertTrue(hand2.check_straight())
        hand3 = Hand('ah4d5s3c2h')
        self.assertTrue(hand3.check_straight())
    
    def test_check_straight_flush(self):
        hand = Hand('ad2d3d4d5d')
        self.assertTrue(hand.check_straight_flush())
        
    def test_four_of_kind(self):
        hand = Hand('4s4hjs4c4d')
        self.assertTrue(hand.check_four_of_kind())
        not_four = Hand('ad2d3d4d5d')
        self.assertFalse(not_four.check_four_of_kind())

    def test_full_house(self):
        hand = Hand('2s2c2h5h5d')
        self.assertTrue(hand.check_full_house())
        
    def test_two_pair(self):
        hand = Hand('2c2s5hkhkd')
        self.assertTrue(hand.check_two_pair())
        hand2 = Hand('5sks5dkdqs')
        self.assertTrue(hand.check_two_pair())
        not_hand = Hand('2s5c7s8dkh')
        self.assertFalse(hand.check_two_pair())
    
if __name__ == '__main__':
    unittest.main()