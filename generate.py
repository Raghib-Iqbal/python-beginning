from random import choice,randint,shuffle
# coin =choice(['head','tale'])
# number= randint(1,10)
import statistics
print(statistics.mean([100,90]))

cards= ['joker','king','queen']
shuffle(cards)
for card in cards:
    print(card)