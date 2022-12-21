"""BlackJack Game Main module

   More descriptions to follow 
"""

suits = ["spades", "clubs", "hearts", "diamonds"]
suit = suits[2]
rank = "K"
value = 10

print("Your card is: " + rank + " of " + suit)

suits.append("snakes")


for suit in suits:
    print(suit)

