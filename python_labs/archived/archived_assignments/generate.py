from random import shuffle

def main():
    # Define a list of possible ranks
    ranks = [
        "Ace",
        "King",
        "Queen",
        "Jack",
        "Ten",
        "Nine",
        "Eight",
        "Seven",
        "Six",
        "Five",
        "Four",
        "Three",
        "Two"
        ]
    
    # Define a list of suits
    suits = [
        "hearts",
        "diamonds",
        "clubs",
        "spades"
    ]

    # Generate a full deck of cards
    full_deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

    # The user's hand is initially empty
    my_hand = []

    # Shuffle the deck with random.shuffle()
    shuffle(full_deck)

    # Draw the first 5 cards, removing from the deck and adding to the user's hand
    for _ in range(5):
        my_hand.append(full_deck.pop())

    # Print the hand
    print("\n".join(my_hand))

if __name__ == "__main__":
    main()