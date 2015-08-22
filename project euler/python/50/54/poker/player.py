# -*- coding: utf-8 -*-

class Player(object):
    def set_hand(self, hand):
        self.hand = hand
        self.values, self.suits = hand_to_vs(hand)
        self.rank = rank(self.values, self.suits)

    def __gt__(self, other):
        return self.rank > other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __str__(self):
        self.hand = vs_to_hand(self.values, self.suits)
        return self.hand

    def __repr__(self):
        self.hand = vs_to_hand(self.values, self.suits)
        return self.hand

# hand <==> values, suits
def hand_to_vs(hand):
    #値は手(hand)を関数で評価した時に返り値として返すのに用いる
    #0(False)は条件を満たさない場合の返り値として使うので、1からはじめる
    card_to_num = {"2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7, "9":8, "T":9, "J":10, "Q":11, "K":12, "A":13}
    values = [card_to_num[i] for i in hand[::3]]
    suits = [i for i in hand[1::3]]
    return values, suits

def vs_to_hand(values, suits):
    num_to_hand = {1:"2", 2:"3", 3:"4", 4:"5", 5:"6", 6:"7", 7:"8", 8:"9", 9:"T", 10:"J", 11:"Q", 12:"K", 13:"A"}
    hand = ""
    for i in range(5):
        hand += num_to_hand[values[i]] + suits[i] + " "
    hand = hand[:-1]
    return hand

# rank
def rank(values, suits):
    v, s = values, suits
    rank = [0]*10
    rank[0] = royal_flush(v, s)
    rank[1] = straight_flush(v, s)
    rank[2] = four_of_a_kind(v)
    rank[3] = full_house(v)
    rank[4] = flush(s)
    rank[5] = straight(v)
    rank[6] = three_of_a_kind(v)
    rank[7] = two_pairs(v)
    rank[8] = one_pair(v)
    rank[9] = high_card(v)
    return rank

# rank-0
def high_card(values):
    return max(values)

# rank-1~3,5
def pair(values, pairs, per_pair):
    dic = {}
    for i in values:
        dic[i] = values.count(i)
    
    count, L = 0, []
    for k, v in dic.items():
        #組あたりper_pair枚
        if v == per_pair:
            count += 1
            L.append(k)
    L.sort(reverse=True)
    #ペアの数がpairs組
    if count >= pairs:
        if pairs == 1:
            return max(L)
        else:
            return L
    else:
        return False

# rank-1
def one_pair(values):
    return pair(values, 1, 2)

# rank-2
def two_pairs(values):
    return pair(values, 2, 2)

# rank-3
def three_of_a_kind(values):
    return pair(values, 1, 3)

# rank-4
def straight(values):
    st = [range(i, i+5) for i in range(1, 9)]
    v = values
    v.sort()
    if v in st:
        return v[0]
    else:
        return False

# rank-5
def flush(suits):
    if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
        return True
    else:
        return False

# rank-6
def full_house(values):
    if three_of_a_kind(values) and one_pair(values):
        return (three_of_a_kind(values), one_pair(values))
    else:
        return False

# rank-7
def four_of_a_kind(values):
    return pair(values, 1, 4)

# rank-8
def straight_flush(values, suits):
    if (not royal_flush(values, suits)) and straight(values) and flush(suits):
        return straight(values)
    else:
        return False

# rank-9
def royal_flush(values, suits):
    v = values
    v.sort()
    if v == [9, 10, 11, 12, 13] and flush(suits):
        return True
    else:
        return False
