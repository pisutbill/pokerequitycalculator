#a card is a tuple of rank and suit
#rank goes from 2 to 13 with 13 being Ace
#suit being c d h s (2, 'c')
import re
#pip install more_itertools
class Hand:
    rank_dict = {'a':14, 'k':13, 'q':12, 'j':11}
    handStength = -1 #8 for SF 1 is highcard
        

    def __init__(self, hand_string):
        self.card_list = []
        self.read_handstring(hand_string)
    
    def read_handstring(self, hand_string):
        suit_pattern = r'[cdhs]'
        non_transformed= [item for item in re.split(self.suit_pattern, hand_string) if item]
        rank_list = []
        for char in non_transformed:
            if char in self.rank_dict:
                rank_list.append(self.rank_dict[char])
            else:
                rank_list.append(int(char))
        
        for rank in rank_list:
            if len(rank_list) != 5:
                raise ValueError("Wrong number of card rank")
            if rank < 2 or rank > 14:
                raise ValueError("Invalid card rank " + str(rank))
        #get the suit
        
        suit_list = []
        for char in hand_string:
            if char in ['c', 'd', 'h', 's']:
                suit_list.append(char)
        if len(suit_list) != 5:
            raise ValueError('Invalid number of card suits')
        
        self.card_list = list(zip(rank_list, suit_list))
        
        self.card_list.sort(key=lambda x: x[0])
        
    def check_flush(self):
        # Check if all suits are the same
        suits = [t[1] for t in self.card_list]
        return all(suit == suits[0] for suit in suits)

    def check_straight(self):
        # Check if the hand is a wheel (special case of straight)
        if self.check_wheel():
            return True
        
        # Check if ranks are consecutive
        return all(self.card_list[i][0] + 1 == self.card_list[i + 1][0] for i in range(len(self.card_list) - 1))
    
    def check_wheel(self):
        if self.card_list[4][0] == 14:
            temp = self.card_list[:-1]
            temp_rank = [t[0] for t in temp]
            if temp_rank == [2, 3, 4, 5]:
                ace_card = self.card_list[4]
                self.card_list = temp + [ace_card]
                return True
        return False
    
    def check_straight_flush(self):
        return self.check_flush() and self.check_straight()
    

    
    def check_four_of_kind(self):
        windowed_list = [self.card_list[i:i+4] for i in range(len(self.card_list) - 4 + 1)]
        for window in windowed_list:
            if all([x[0] == window[0][0] for x in window]):
                print(window)
                return True
        print(windowed_list)
        return False
    
    def check_full_house(self):
        first_three = self.card_list[:3]
        last_two = self.card_list[3:]
        return all(x[0] == first_three[0][0] for x in first_three) and all(y[0] == last_two[0][0] for y in last_two)
    
    def check_three_of_kind(self):
        windowed_list = [self.card_list[i:i+3] for i in range(len(self.card_list) - 3 + 1)]
        for window in windowed_list:
            if all([x[0] == window[0][0] for x in window]):
                print(window)
                return True
        print(windowed_list)
        return False

    def check_two_pair(self):
        windowed_list = [self.card_list[i:i+2] for i in range(len(self.card_list)-2+1)]
        pair_count = 0
        for window in windowed_list:
            if all([x[0] == window[0][0] for x in window]):
                pair_count += 1
            if pair_count == 2:
                    return True
        return False
    
    def check_one_pair(self):
        windowed_list = [self.card_list[i:i+1] for i in range(len(self.card_list)-1+1)]
        for window in windowed_list:
            if all([x[0] == window[0][0] for x in window]):
                return True
        return False