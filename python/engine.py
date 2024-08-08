class Card:
    
    def __init__(self, rank, suit):
        if not isinstance(rank, int):
            raise TypeError("Rank must be an integer")
        if not isinstance(suit, str) or len(suit) != 1:
            raise TypeError("Suit must be a single character")
        if rank < 2 or rank > 14:
            raise ValueError("Invalid card rank. Rank must be between 2 and 14")
        if suit not in {'c', 'd', 'h', 's'} or not suit.isalpha():
            raise ValueError("Invalid card suit. Suit must be 'c', 'd', 'h', or 's'")
        self.rank = rank
        self.suit = suit
        
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank
        raise TypeError("not a card")
    
    def __lt__(self, other):
        if isinstance(other, Card):
            return self.rank < other.rank
        raise TypeError("not a card")
    
    def __gt__(self, other):
        if isinstance(other, Card):
            return self.rank > other.rank
        raise TypeError("not a card")
    
    
card1 = Card(2, 'c')      
print(card1.suit)
print(card1.rank)
            
class Hand:
    def __init__(self, card_list):
        
        
    