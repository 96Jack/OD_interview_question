import collections

Card = collections.namedtuple("Card", ['rank', 'suit'])
# print(Card('4', 'read'))

class French:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'hongtao meihua fangkuai heitao'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    # 使对象可迭代且可切片
    def __getitem__(self, position):
        return self._cards[position]
    

deck = French()
#rank    2 3 4 5 ... 14
#color:  0
#        1
#        2
#        3
# 2*4 = 8  最大 8+3 = 11 
# 3*4 = 12 最小 12+0 = 12
suit_values = dict(hongtao=3, meihua=2, fangkuai=1, heitao=0)
def spades_high(card):
    rank_value = French.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)