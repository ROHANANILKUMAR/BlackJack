class Human():
    def __init__(self,Name):
        self.garbage=False
        self.bust=False
        self.black_jack=False
        self.money=100
        self.bet=0
        self.special_card=False
        self.cards=[]
        self.name=Name

    def assign_card(self,card):
        self.cards.append(card)

    def reset(self):
        self.cards=[]
        self.special_card=False
        self.bust=False
        self.black_jack=False

class Player(Human):

    def lose_bet(self):
        if(self.bet<0):
            self.bet=0
        else:
            return "Err"

    def set_bet(self,value):
        if value<=self.money:
            self.bet=value
            self.money-=value
            return True
        else:
            return False

    def win_bet_BlackJack(self):
        try:
            self.won_money=(self.bet)/2+self.bet
            self.money+=self.won_money
            bet=0
        except:
            self.won_money=0
            bet=0
        return self.won_money

    def win_double_money(self):
        self.money+=self.bet*2
        self.bet=0

class Dealer(Human):
    pass
    