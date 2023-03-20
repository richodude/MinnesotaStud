import math
from colors import colors
from players import player1
from players import dealer
from statistics import mode
from statistics import mean
from collections import Counter

masterlist = []
highcardlist = []

def simplify_to_values(self):
    temp_rank = []
    temp_suit = []
    pair_list = []
    connector_list = []
    suit_list = []
    has_ace_two = False
    self.values = self.values[0]
    for i in range(5):
        temp_rank.append(2 + math.floor(player1.values[i]/4))
    for i in range(5):
        temp_suit.append(1 + math.floor(player1.values[i]%4))
    for i in range(4):
        if temp_rank[i] == temp_rank[1+i]:
            pair_list.append(1)
        else:
            pair_list.append(0)
    for i in range(4):
        if temp_rank[i] - temp_rank[1+i] == 1:
            connector_list.append(1)
        else:
            connector_list.append(0)
    if temp_rank[0] == 14 and temp_rank[4] == 2:
        has_ace_two = True
    for i in range(4):
        if temp_suit[i] == temp_suit[1+i]:
            suit_list.append(1)
        else:
            suit_list.append(0)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    is_pair = False
    is_twopair = False
    is_trips = False
    is_fullhouse = False
    is_quads = False
    is_4straight = False
    is_5straight = False
    is_4flush = False
    is_5flush = False
    is_4sflush = False
    is_5sflush = False
    is_4rflush = False
    is_5rflush = False
    is_acehigh = False
    is_kinghigh = False
    is_queenhigh = False
    is_jackhigh = False
    is_tenhigh = False
    is_ninehigh = False
    is_eighthigh = False
    is_sevenhigh = False
    if pair_list == [1, 0, 0, 0] or pair_list == [0, 1, 0, 0] or pair_list == [0, 0, 1, 0] or pair_list == [0, 0, 0, 1]:
        is_pair = True
        #if mode(temp_rank) == 11:
            #print("contains a pair of Jacks")
        #elif mode(temp_rank) == 12:
            #print("contains a pair of Queens")
        #elif mode(temp_rank) == 13:
            #print("contains a pair of Kings")
        #elif mode(temp_rank) == 14:
            #print("contains a pair of Aces")
        #else:
            #print("contains a pair of {}s".format(mode(temp_rank)))
    if pair_list == [1, 0, 1, 0] or pair_list == [0, 1, 0, 1] or pair_list == [1, 0, 0, 1]:
        is_twopair = True
        #print("contains a pair of " + str(temp_rank[1]) + "s and " + str(temp_rank[3]) + "s")
    if pair_list == [1, 1, 0, 0] or pair_list == [0, 1, 1, 0] or pair_list == [0, 0, 1, 1]:
        is_trips = True
        #print("contains a three-of-a-kind of {}s".format(mode(temp_rank)))
    if pair_list == [1, 1, 0, 1] or pair_list == [1, 0, 1, 1]:
        is_fullhouse = True
        #if mean(temp_rank) > mode(temp_rank):
            #print("contains a full house of " + str(mode(temp_rank)) + "s over " + str(temp_rank[0]) + "s")
        #elif mean(temp_rank) < mode(temp_rank):
            #print("contains a full house of " + str(mode(temp_rank)) + "s over " + str(temp_rank[4]) + "s")
    if pair_list == [1, 1, 1, 0] or pair_list == [0, 1, 1, 1]:
        is_quads = True
        #print("contains a 4-of-a-kind of {}s".format(mode(temp_rank)))
    if connector_list == [1, 1, 1, 1] or connector_list == [0, 1, 1, 1] and has_ace_two == True:
        is_5straight = True
        #if has_ace_two == False:
            #print("contains a {} high 5-card straight".format(temp_rank[0]))
        #elif has_ace_two == True:
            #print("contains a {} high 5-card straight".format(temp_rank[1]))
    if suit_list == [1, 1, 1, 1]:
        is_5flush = True
        #print("contains a {} high 5-card flush".format(temp_rank[0]))
    if connector_list == [1, 1, 1, 0] or connector_list == [0, 1, 1, 1] or connector_list == [1, 0, 1, 1] and pair_list == [0, 1, 0, 0] or connector_list == [1, 1, 0, 1] and pair_list == [0, 0, 1, 0] or connector_list == [0, 1, 0, 1] and pair_list == [0, 0, 1, 0] and has_ace_two == True or connector_list == [0, 0, 1, 1] and has_ace_two == True or connector_list == [0, 1, 1, 0] and pair_list == [0, 0, 0, 1] and has_ace_two == True or connector_list == [0, 0, 1, 1] and pair_list == [1, 0, 0, 0] and has_ace_two == True or connector_list == [1, 0, 1, 1] and has_ace_two == True:
        is_4straight = True
        #if has_ace_two == False:
            #if connector_list[0] == 1:
                #print("contains a {} high 4-card straight".format(temp_rank[0]))
            #elif connector_list[0] == 0:
                #print("contains a {} high 4-card straight".format(temp_rank[1]))
        #elif has_ace_two == True:
            #if is_pair == False:
                #print("contains a {} high 4-card straight".format(temp_rank[2]))
            #elif is_pair == False:
                #print("contains a {} high 4-card straight".format(temp_rank[1]))
    if temp_suit.count(1) == 4 or temp_suit.count(2) == 4 or temp_suit.count(3) == 4 or temp_suit.count(4) == 4:
        is_4flush = True
        #if suit_list == [0, 1, 1, 1]:
            #print("Contains a {} high 4-card flush".format(temp_rank[1]))
        #else:
            #print("Contains a {} high 4-card flush".format(temp_rank[0]))
    if is_4flush == True or is_5flush == True:
        if is_4straight or is_5straight == True:
            if is_4flush == True:
                counter = Counter(temp_suit)
                least_common = counter.most_common()[-1][0]
                suit_index = temp_suit.index(least_common)
                temp_temp_rank = temp_rank
                del temp_temp_rank[suit_index]
                temp_temp_list = []
                for i in range(3):
                    if temp_temp_rank[i] - temp_temp_rank[i+1] == 1:
                        temp_temp_list.append(1)
                    else:
                        temp_temp_list.append(0)
                if temp_temp_list == [1, 1, 1]:
                    is_4sflush = True
                    if temp_temp_rank == [14, 13, 12, 11]:
                        is_4rflush = True
                elif temp_temp_rank == [14, 4, 3, 2]:
                    is_4sflush = True
            else:
                if is_4straight == True:
                    is_4sflush = True
                    if temp_rank[3] == 11:
                        is_4rflush = True
    if is_5straight == True and is_5flush == True:
        is_5sflush = True
        #if has_ace_two == False:
            #print("contains a {} high 5-card straight-flush".format(temp_rank[0]))
        #elif has_ace_two == True:
            #print("contains a {} high 5-card straight-flush".format(temp_rank[1]))
    if is_5sflush == True and temp_rank == [14, 13, 12, 11, 10]:
        is_5rflush = True
        #print("contains a royal flush")
    if is_pair == False and is_twopair == False and is_trips == False and is_fullhouse == False and is_quads == False and is_4straight == False and is_5straight == False and is_4flush == False and is_5flush == False and is_4sflush == False and is_5sflush == False and is_4rflush == False and is_5rflush == False:
        if temp_rank[0] == 14:
            is_acehigh = True
        elif temp_rank[0] == 13:
            is_kinghigh = True
        elif temp_rank[0] == 12:
            is_queenhigh = True
        elif temp_rank[0] == 11:
            is_jackhigh = True
        elif temp_rank[0] == 10:
            is_tenhigh = True
        elif temp_rank[0] == 9:
            is_ninehigh = True
        elif temp_rank[0] == 8:
            is_eighthigh = True
        elif temp_rank[0] == 7:
            is_sevenhigh = True
        #print("hand is", self.cards[4], "high")
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #print(temp_rank)
    #print(temp_suit)
    if is_5rflush is True:
        return masterlist.append(13)
    if is_5sflush is True:
        return masterlist.append(12)
    if is_4rflush is True:
        return masterlist.append(11)
    if is_quads is True:
        return masterlist.append(10)
    if is_4sflush is True:
        return masterlist.append(9)
    if is_fullhouse is True:
        return masterlist.append(8)
    if is_5flush is True:
        return masterlist.append(7)
    if is_5straight is True:
        return masterlist.append(6)
    if is_trips is True:
        return masterlist.append(5)
    if is_4flush is True:
        return masterlist.append(4)
    if is_4straight is True:
        return masterlist.append(3)
    if is_twopair is True:
        return masterlist.append(2)
    if is_pair is True:
        return masterlist.append(1)
    else:
        if is_acehigh == True:
            highcardlist.append(14)
        elif is_kinghigh == True:
            highcardlist.append(13)
        elif is_queenhigh == True:
            highcardlist.append(12)
        elif is_jackhigh == True:
            highcardlist.append(11)
        elif is_tenhigh == True:
            highcardlist.append(10)
        elif is_ninehigh == True:
            highcardlist.append(9)
        elif is_eighthigh == True:
            highcardlist.append(8)
        elif is_sevenhigh == True:
            highcardlist.append(7)
        return masterlist.append(0)

    #print(temp_rank)
    #print(temp_suit)
    #print(pair_list)
    #print(connector_list)
    #print(has_ace_two)
    #print(suit_list)