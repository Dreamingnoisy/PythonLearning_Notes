import random
class Card:

    ''' Represents a standard playing card''' 

    def __init__(self,suit=0,rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],Card.suit_names[self.suit])


    def __lt__(self,other): 
        #lt stands for "less than"
        return  (self.suit,self.rank) < (other.suit,other.rank)

class Deck:
    'A deck of cards'
    def __init__(self):
        self.cards = []
        for i in range(4):
            for j in range(1,14):
                card = Card(i,j)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self,card):
        self.cards.append(card)

    def shuffle(self):
        
        random.shuffle(self.cards)

    def sort(self):

        self.cards = sorted(self.cards)

    def move_cards(self,hand,num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self,num_of_hands,num_of_cards):
        lt_of_hands = []
        for i in range(num_of_hands):
            hand = Hand()
            self.move_cards(hand,num_of_cards)
            lt_of_hands.append(hand)
        return lt_of_hands

class Hand(Deck):
    '''Represents a hand of playing cards'''

    def __init__(self,label=''):
        self.cards = []
        self.label = label



def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide 
    the definition of method_name (as a string) if it is
    invoked on obj.
    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None
if __name__ == "__main__":
    c = Deck()

    lt = c.deal_hands(2,5)
    for hand in lt:
        print(hand)

    print(c)





