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

if __name__ == '__main__':
    unittest.main()