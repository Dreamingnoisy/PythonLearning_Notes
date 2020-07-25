"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from card import Hand, Deck,Card


class PokerHand(Hand):
    """Represents a poker hand."""

    def __init__(self, label='',status=False):
        super().__init__(label)
        self.status = status
        


    def hist(self):
        self.suit_hist()
        self.rank_hist()
        self.status = True

    def get_suit(self,suit):
        hand_suit = PokerHand()
        for card in self.cards:
            if card.suit == suit:
                hand_suit.add_card(card)
        return hand_suit

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
        
       

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
        
        

    def if_histed(self):
        if self.status == False:
            self.hist()              
        


    def has_pair(self):
        self.if_histed()
        for val in self.ranks.values():
            if val == 2 :
                return True
        return False

    
    def has_two_pairs(self):
        self.if_histed()
        count = 0
        for val in self.ranks.values():
            if val == 2 :
                count += 1
        if count == 2 :
            return True
        else :
            return False

    def has_straight(self,n = 5):
        self.cards = sorted(self.cards,key=lambda x : x.rank)
        
        rank_list,suit_list=[],[]
        for card in self.cards:
            if card.rank not in rank_list:
                rank_list.append(card.rank)
                suit_list.append(card.suit)

        if len(rank_list) < n:
            return False

        for i in range(len(rank_list)-(n-1)):
            if abs(rank_list[i]-rank_list[i+(n-1)]) == (n-1):
                return True

        if rank_list[-1] == 13 and abs(rank_list[-(n-1)]-rank_list[-1]) == n-2 and rank_list[0] == 1:
            return True


        return False

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.if_histed()

        for val in self.suits.values():
            if val >= 5:
                return True
        return False
        
    def has_full_house(self):
        self.if_histed()
        for val in self.ranks.values():
            if val == 2:
                for val2 in self.ranks.values():
                    if val2 == 3:
                        return True

        return False

    def has_four_of_a_kind(self):
        self.if_histed()   

        for val in self.ranks.values():
            if val == 4 :
                return True
        return False

    def has_straight_flush(self,n=5):
        self.if_histed()

        for key in self.suits.keys():
            if self.suits[key] >= 5:
                hand_suit = self.get_suit(key)
                return hand_suit.has_straight()    
                
        return False
    def classify(self):

        if self.has_straight_flush():
            self.label = 'straight_flush'
        elif self.has_four_of_a_kind():
            self.label = 'four_of_a_kind'
        elif self.has_flush():
            self.label = 'flush'
        elif self.has_straight():
            self.label = 'straight'
        elif self.has_two_pairs():
            self.label = 'two_pairs'
        elif self.has_pair():
            self.label = 'pair'
        else: self.label = 'Normal'
count = {}
def count_classify(hand):
    global count
    hand.classify()
    count[hand.label] = count.setdefault(hand.label,0) + 1


if __name__ == '__main__':
    # make a deck


    #deal the cards and classify the hands
    for j in range(100000):
        deck = Deck()
        deck.shuffle()
        for i in range(7):
            hand = PokerHand()
            deck.move_cards(hand, 7)
            hand.sort()
            count_classify(hand)      
    print(sorted(count.items(),key=lambda x:x[1],reverse = True))




    
