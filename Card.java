public class Card  {
    private int value;
    private char suit;


    public Card(int value, char suit) {
        if ((value < 0) || (value > 14)) {
            throw new IllegalArgumentException("Invalid Card Value");
        }
        if ((suit != 'c') && (suit != 'd') && (suit != 'h') && (suit != 's')) {
            throw new IllegalArgumentException("Invalid Card Suit");
        }
        this.value = value;
        //2-10, 11=J, 12=Q, 13=K
        this.suit = suit;
        //c d h s
    }

    public boolean equals(Card another) {
        return (this.value == another.getValue());
    }

    public int getValue() {
        return this.value;
    }

    public char getSuit() {
        return this.suit;
    }


    public int compareTo(Card another) {
        //just for comparing the value of each card
        int thisValue = this.value;
        int anotherValue = another.getValue();
        if (thisValue == 1) {
            if (anotherValue == 1) {
                return 0;
            } else {
                return 1;
            }
        } else if (anotherValue == 1) {
            if (thisValue == 1) {
                return 0;
            } else {
                return -1;
            }
        } 
        else {
            return ((thisValue < anotherValue) ? -1 : ((thisValue == anotherValue) ? 0 : 1));
        }

    }

    public void print() {
        System.out.println(String.valueOf(this.value));
    }
}