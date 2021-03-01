import random

class Card(object):
    """一张牌"""
    def __init__(self, suite, face):
        self._suite = suite # 花色
        self._face = face # 数字
    
    @property
    def face(self):
        return self._face
    
    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            faceStr =  "A"
        elif self._face == 11:
            faceStr =  "J"
        elif self._face == 12:
            faceStr =  "Q"
        elif self._face == 13:
            faceStr =  "K"
        else:
            faceStr = str(self._face)
        return "%s%s"%(self._suite, faceStr)
    
    def __repr__(self):
        return self.__str__()



class Poker(object):
    """一副牌"""
    def __init__(self):
        self._cards = [Card(suite, face)
                    for suite in "♠♥♣♦"
                    for face in range(1,14)]
        self._current = 0
    
    @property
    def cards(self):
        return self._cards
    
    def shuffle(self): # 洗牌
        self._current = 0
        random.shuffle(self._cards)
    
    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card
    @property
    def has_next(self): # 还有没有牌
        return self._current < len(self._cards)


class Player(object):
    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name
    
    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        """摸牌"""
        self._cards_on_hand.append(card)
    
    def arrange(self, card_key):
        """整理玩家手里的牌"""
        self._cards_on_hand.sort(key=card_key)

def get_key(card):
    return (card.suite,card.face)

def main():
    p = Poker()
    p.shuffle()  # 洗牌
    players = [Player("东邪"), Player("吸毒"), Player("南帝")]
    for _ in range(15):
        for player in players:
            player.get(p.next)
    for player in players:
        print(player.name+":",end = " ")
        player.arrange(get_key)
        print(player.cards_on_hand)

if __name__ == "__main__":
    main()