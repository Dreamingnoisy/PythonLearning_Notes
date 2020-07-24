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
        
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.if_histed()

        for val in self.suits.values():
            if val >= 5:
                return True
        return False

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
        print(rank_list)
        if len(rank_list) < n:
            return False


        for i in range(len(rank_list)-n):
            if abs(rank_list[i]-rank_list[i+(n-1)]) == (n-1):
                return True

        if rank_list[-1] == 13 and abs(rank_list[-(n-1)]-rank_list[-1]) == n-2 and rank_list[0] == 1:
            return True


        return False
        

if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(3):
        hand = PokerHand()
        deck.move_cards(hand, 15)
        hand.sort()
        
        print(hand.has_straight(6))
        #print(hand)
        
        print('')


    
