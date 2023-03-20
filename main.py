from cards import deck
from players import player1
from players import dealer
from HandRanking import simplify_to_values
from HandRanking import masterlist
from HandRanking import highcardlist
from colors import colors



deck.deal(player1)
#print(deck)
#stud_draw(player1)
#stud_draw(dealer)
#player1.cards.reverse()
#print("Player's cards are:", player1.cards)
#print("Dealer's cards are:", dealer.cards)
#print(deck)


#print(deck)
#print(masterlist)
print()
print(masterlist.count(0), "High cards")
print(masterlist.count(1), "Pairs")
print(masterlist.count(2), "Two pairs")
print(masterlist.count(3), "4-card straights")
print(masterlist.count(4), "4-card flushes")
print(masterlist.count(5), "3-of-a-kinds")
print(masterlist.count(6), "5-card straights")
print(masterlist.count(7), "5-card flushes")
print(masterlist.count(8), "Full houses")
print(masterlist.count(9), "4-card straight-flushes")
print(masterlist.count(10), "Quads")
print(masterlist.count(11), "4-card royal flushes")
print(masterlist.count(12), "5-card straight-flushes")
print(masterlist.count(13), "5-card royal flushes")
print("(" + str(len(masterlist)) + " total hands)")
print("\nof all the high cards:")
print(highcardlist.count(14), "were ace-high")
print(highcardlist.count(13), "were king-high")
print(highcardlist.count(12), "were queen-high")
print(highcardlist.count(11), "were jack-high")
print(highcardlist.count(10), "were ten-high")
print(highcardlist.count(9), "were nine-high")
print(highcardlist.count(8), "were eight-high")
print(highcardlist.count(7), "were seven-high")
print("(" + str(len(highcardlist)) + " total high card combos)")
