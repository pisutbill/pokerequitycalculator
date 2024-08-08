
public class Hand {
    private Card[] cards = new Card[5];
    private Hand_Stength hand_strength;
    private int numStrength;
    enum Hand_Stength {
        STRAIGHT_FLUSH, FOUR_OF_A_KIND, FLUSH, STRAIGHT, THREE_OF_A_KIND, TWO_PAIRS, ONE_PAIR, HIGH_CARD;
    }

    public Hand(Card[] cards) {
        if (cards.length != 5) {
           throw new IllegalArgumentException("Incorrect Number of Cards");
        }
        this.cards = cards;
        determineHandStrength();
    }

    public Hand(Card card1, Card card2, Card card3, Card card4, Card card5) {
        this.cards[0] = card1;
        this.cards[1] = card2;
        this.cards[2] = card3;
        this.cards[3] = card4;
        this.cards[4] = card5;
        determineHandStrength();
    }

    public Hand(String cardsString) {
        int val = 0;
        boolean isValNext = true;
        int cardCount = 0;
        for (int i = 0; i < cardsString.length(); i++) {
            char input = cardsString.charAt(i);
            System.out.println(i + " " +input);
            if (isValNext) {
                if (input == 'a') {
                    val = 14;
                    isValNext = false;
                } else if (input == 'k') {
                    val = 13;
                    isValNext = false;
                } else if (input == 'q') {
                    val = 12;
                    isValNext = false;
                } else if (input == 'j') {
                    val = 11;
                    isValNext = false;
                } else if (Character.isDigit(cardsString.charAt(i+1))) {
                    val = Integer.parseInt(cardsString.substring(i, i+1));
                    i++;
                    isValNext = false;
                } else {
                    if (!Character.isDigit(cardsString.charAt(i))) {
                        throw new IllegalArgumentException("not a digit");
                    } else {
                        val =Character.getNumericValue(cardsString.charAt(i));
                        isValNext = false;
                    }
                }
            } else {
                if (!((input == 'd') || (input == 's') || (input =='h') || (input == 'c'))) {
                    throw new IllegalArgumentException("not valid suit");
                } else {
                    this.cards[cardCount++] = new Card(val, input);
                    isValNext = true;
                }
            }
        }
        determineHandStrength();
    }

    public int compare(Hand another) {
        System.out.println(numStrength);
        System.out.println(another.getNumStrength());
        if (numStrength > another.getNumStrength()) {
            return 1;
        } 
        if (numStrength == another.getNumStrength()) {
            return 0;
        }

        return -1;
    }

    public void determineHandStrength() {
        sort();
        if (isStraightFlush()) {
            hand_strength = Hand_Stength.STRAIGHT_FLUSH;
            numStrength = 8;
        } else if (isFourOfAKind()) {
            hand_strength = Hand_Stength.FOUR_OF_A_KIND;
            numStrength = 7;
        } else if (isFlush()) {
            hand_strength = Hand_Stength.FLUSH;
            numStrength = 6;
        } else if (isStraight()) {
            hand_strength = Hand_Stength.STRAIGHT;
            numStrength = 5;
        } else if (isThreeOfAKind()) {
            hand_strength = Hand_Stength.THREE_OF_A_KIND;
            numStrength = 4;
        } else if (isTwoPair()) {
            hand_strength = Hand_Stength.TWO_PAIRS;
            numStrength = 3;
        } else if (isOnePair()) {
            hand_strength = Hand_Stength.ONE_PAIR;
            numStrength = 2;
        } else {
            hand_strength = Hand_Stength.HIGH_CARD;
            numStrength = 1; //clean later
        }
    }

    public int getNumStrength() {
        return numStrength;
    }


    public void sort() {
        for (int i = 3; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                //System.out.println(j);
                if (this.cards[j].compareTo(this.cards[j+1]) == -1) {
                    Card temp = this.cards[j];
                    this.cards[j] = this.cards[j+1];
                    this.cards[j+1] = temp;
                }
            }
        }
    }

    public Card[] getCards() {
        return this.cards;
    }

    public boolean isStraightFlush() {
        if (isFlush()) {
            if (isStraight()) {
                return true;
            }
        }
        return false;
    }

    public boolean isFourOfAKind() {
        boolean found = false;
        for (int j = 0; j <= 1; j++) {
            int val = cards[j].getValue();
            int count = 0;
            for (int i = j+1; i <= j+3; i++) {
                if (cards[i].getValue() == val) {
                    count++;
                }
            }
            if (count == 3) return true;
        }
        return false;
        
    }


    public boolean isFlush() {
        char checkSuit = this.cards[0].getSuit();
        for (int i = 1; i <= 4; i++) {
            if (checkSuit != cards[i].getSuit()) {
                return false;
            }
        }
        return true;
    }

    public boolean isStraight() {
        if (cards[0].getValue() == 14) {
            return checkWheel();
        }
        return checkStraight(cards);
    }

    public boolean checkWheel() {
        System.out.println("test checkWheel");
        Card[] temp = new Card[5];
        char aceSuit = cards[0].getSuit();
        for (int i = 1; i < 5; i++) {
            temp[i-1] = cards[i];
        }
        temp[4] = new Card(14, aceSuit);
        if (!checkStraight(temp)) return false;
        cards = temp;
        return true;
    }

    public boolean checkStraight(Card[] cardToCheck) {

        for (int i = 0; i < (cardToCheck.length - 2); i++) {
            int thisValue = cardToCheck[i].getValue();
            int nextValue = cardToCheck[i+1].getValue();
            if (thisValue == 2) {
                if (nextValue != 14) {
                    return false;
                } else {
                    return true;
                }
            }
            if (nextValue != (thisValue - 1)) return false;
        }
        return true;
    }

    public boolean isThreeOfAKind() {//to do need to determine new order
        for (int i = 0; i <= 2; i++) {
            int val = cards[i].getValue();
            int count = 0;
            for (int j = i + 1; j <= (i + 2); i++) {
                if (val == cards[j].getValue()) {
                    count++;
                } else {
                    count = -1;
                }
            }
            if (count == 2) return true;
        }
        return false;
    }

    public boolean isTwoPair() {
        boolean foundFirstPair = false;
        int firstPairIndex = 0;
        for (int i = 0; i <= 3; i++) {
            if (cards[i].getValue() == cards[i+1].getValue()) {
                System.out.println("found first pair");
                if (!foundFirstPair) {
                    firstPairIndex = i + 1;
                    foundFirstPair = true;
                }


            }
        }
        if (foundFirstPair) {
            for (int i = firstPairIndex + 1; i <= 3; i++) {
                if (cards[i].getValue() == cards[i+1].getValue()) return true;
            }
        }
        return false;
        
    }

    public boolean isOnePair() {
        for (int i = 0; i <= 3; i++) {
            if (cards[i].getValue() == cards[i+1].getValue()) {
                return true;
            }
        }
        return false;
    }


    public void print() {
        System.out.println("Printing hand");
        for (int i = 0; i < cards.length; i++) {
            int val = cards[i].getValue();
            char suit = cards[i].getSuit();
            switch (val) {
                case 14: {
                    System.out.print('A');
                    break;
                }
                case 11: {
                    System.out.print('J');
                    break;
                }
                case 12: {
                    System.out.print('Q');
                    break;
                }
                case 13: {
                    System.out.print('K');
                    break;
                }
                default:
                    System.out.print(String.valueOf(val));
                
            }
            System.out.print(suit + "\n");
        }
        System.out.println("Hand Strength: " + hand_strength);
        System.out.println("end of hand");
    }

    public int compare() {
        return 0;
    }


    




}
