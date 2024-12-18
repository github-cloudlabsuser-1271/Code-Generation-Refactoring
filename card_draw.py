import itertools
import random

# Create a deck of cards
deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))

# Shuffle the deck
random.shuffle(deck)

# Draw five cards
print("You got:")
for i in range(5):
   print(f"{deck[i][0]} of {deck[i][1]}")
