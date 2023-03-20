import itertools
import math
import sys

from players import player1
from players import dealer
from colors import colors
from HandRanking import simplify_to_values

class card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        rank_name = ""
        suit_name = ""
        if self.rank == 0:
            rank_name = "2"
        elif self.rank == 1:
            rank_name = "3"
        elif self.rank == 2:
            rank_name = "4"
        elif self.rank == 3:
            rank_name = "5"
        elif self.rank == 4:
            rank_name = "6"
        elif self.rank == 5:
            rank_name = "7"
        elif self.rank == 6:
            rank_name = "8"
        elif self.rank == 7:
            rank_name = "9"
        elif self.rank == 8:
            rank_name = "10"
        elif self.rank == 9:
            rank_name = "J"
        elif self.rank == 10:
            rank_name = "Q"
        elif self.rank == 11:
            rank_name = "K"
        elif self.rank == 12:
            rank_name = "A"
        if self.suit == 0:
            suit_name = f"{colors.red}♥{colors.end_color}"
        elif self.suit == 1:
            suit_name = f"{colors.black}♣{colors.end_color}"
        elif self.suit == 2:
            suit_name = f"{colors.red}♦{colors.end_color}"
        elif self.suit == 3:
            suit_name = f"{colors.black}♠{colors.end_color}"
        return rank_name + suit_name



class StandardDeck(list):
    def __init__(self):
        super().__init__()
        suits = list(range(4))
        ranks = list(range(13))
        for rank in ranks:
            for suit in suits:
                self.append(card(rank,suit))

    def deal(self, location):
        x = 1
        y = 1
        hand_count = 0
        #pop_card = [48,44,8,4,0]
        #pop_card = random.sample(range(51),5)
        #pop_card = sorted(pop_card, reverse=True)
        combinations = itertools.combinations(range(0,52),5)
        for combo in combinations:
            player1.values = []
            player1.cards = []
            hand_count += 1
            combo = combo[::-1]
            location.values.append(combo)
            location.cards.append(combo)
            simplify_to_values(player1)
            x = int(hand_count * 100 / 2598960)
            if x > y:
                y = x
                sys.stdout.write("\r {}% complete".format(y))
                sys.stdout.flush()
        #location.cards.append(pop_card)
        #location.values.append(pop_card)
        #simplify_to_values(player1)



deck = StandardDeck()