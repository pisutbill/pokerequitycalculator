import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Hand stflush = new Hand("as2s3s4s5s");
        stflush.print();
        Hand fourKind = new Hand("4s4c4h4dkh");
        fourKind.print();
        System.out.println(stflush.compare(fourKind));
    }

    public static void testFourOfAKind() {
        Card ad = new Card(14, 'd');
        Card as = new Card(14, 's');
        Card ah = new Card(14, 'h');
        Card ac = new Card(14, 'c');
        Hand newHand = new Hand(ad, as ,ah, ac, new Card(13, 'd'));
        newHand.print();
        testStraightFlush();
    }

    public static void testLoop() {
        Scanner myScanner = new Scanner(System.in);
        while (true) {
            Card[] cardArray = new Card[5];
            for (int i = 0; i < 5; i++) {
                System.out.println("Card value");
                int val = 0;
                String valInput = myScanner.nextLine();
                if (valInput.equals("a")) {
                    val = 14;
                } else {
                    val = Integer.parseInt(valInput);
                }
                System.out.println("Card suit");
                char suit = myScanner.nextLine().charAt(0);
                cardArray[i] = new Card(val, suit);
            }
            Hand hand = new Hand(cardArray);
            hand.print();
        }
    }

    public static void testStraightFlush() {
        Card one = new Card(14, 'd');
        Card two = new Card(2, 'd');
        Card three = new Card(3, 'd');
        Card four = new Card(4, 'd');
        Card five = new Card(5, 'd');
        Hand hand = new Hand(five, three, one, two, four);
        hand.print();
        System.out.println(hand.isStraight());
        System.out.println(hand.isFlush());
        System.out.println(hand.isStraightFlush());
        hand.print();
    }
}