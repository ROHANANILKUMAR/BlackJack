from Player import Player,Dealer
import os
from random import *
from cards import *
from time import sleep

def player_left():
    result=False
    for i in players.values():
        if not i.black_jack and not i.bust:
            result=True
    return result

def rst_players():
    for i in players.values():
        i.reset()
    sam.reset()

def collect_garbage():
    garbage_players=[]
    for name,value in players.items():
        if value.garbage:
            garbage_players.append(name)
    for i in garbage_players:
        players.pop(i) 

def double_player_money():
    for i in players.values():
        i.win_double_money()

def check_bust(player):
    if read_value(player.cards)>21:
        player.bust==True
        player.lose_bet()
        player.bet=0
        input(f"Oops {player.name} you got busted, try again next time...")
       
def check_black_jack(player):
    try_list=[x for x in player.cards]
    if check_ace(player):
        try_list.remove(find_ace(player))
        try_list.append("11")
    if read_value(try_list)==21:
        print(f"Hey man you got a black jack... Here's your money : ${player.win_bet_BlackJack()}")
        print("See you in the next game...")
        player.black_jack=True

def show_cards(player_list):
    for i in player_list:
        refresh()
        print(f"{i.name}, your cards are shown below...")
        print(merge_graphics([card_grapics(x,"\t\t") for x in i.cards]))
        check_black_jack(i)
        input("Press to continue...")

def place_bet():
    print_money()
    for i in players.values():
        while True:
            bet_value=int(input(f"{i.name}, whats your bet? "))
            if not i.set_bet(bet_value):
                if get_input("Sorry value greater than the money in your wallet... press q to quit {i.name}, or t to try again...","q","t")=="q":
                    print("Bye, i.name")
                    i.garbage=True
                else:
                    continue
            break

def get_input(question,x,y):
    while True:
        choice=input(f"{question}({x} or {y}) : ")
        if choice.lower()==y:
            return y
        elif choice.lower()==x :
            return x
        else:
            print("Invalid input")

def refresh():
        os.system("cls")

def find_ace(p):
    for i in p.cards:
        if "A" in i:
            return i

def check_ace(p):
    for i in p.cards:
        if "A" in i:
            return True
    return False

def hit(p):
    p.cards.append(deck.pop())

def game_interface(dealercard=False):
    refresh()
    data=""
    for i in players.values():
        if not i.black_jack and not i.bust:
            data+=i.name+" money,bet : $"+str(i.money)+", $"+str(i.bet)+"\t"
    data+="\nDealer's cards :\n"
    if not dealercard:
        data+=merge_graphics([card_grapics(sam.cards[0],"\t\t"),closed_card("\t\t")])
    else:
        data+=merge_graphics([card_grapics(x,"\t\t") for x in sam.cards])
    return data

def load_players():
    number=int(input("Enter number of players : "))
    for i in range(number):
        player_name=input("Enter name of player "+str(i+1)+" : ")
        players[player_name]=Player(player_name)

def assign_cards():
    shuffle(deck)
    for i in range(2):
        for m in players.values():
            m.assign_card(deck.pop())
    for i in range(2):
        sam.assign_card(deck.pop())

def dealer_ace():
    if check_ace(sam):
        print("Dealer got an ace card.")
        sleep(choice([1,2,3]))
        sam.cards.remove(find_ace(sam))
        sam.cards.append("1")
        if read_value(sam.cards)<21:
            sam.cards.remove("1")
            sam.cards.append("11")
            print("Dealer chooses it to be 11")
        else:
            print("Dealer chooses it to be 1")

def print_money():
    returnStr=''
    for i in players.values():
        returnStr+=f"{i.name} balance : ${i.money}\n"
    print(returnStr)

def dealer_turn():
    game_interface(dealercard=True)
    dealer_ace()
    sleep(choice([1,2,3]))
    while True:
        if read_value(sam.cards)>max([read_value(x.cards) for x in players.values() if not x.bust and not x.black_jack]):
            game_interface(dealercard=True)
            print(f"Oops dealer won the game with the card value of {read_value(sam.cards)} better luck next time...")
            sleep(3)
            refresh()
            rst_players()
            print_money()
            input("Press any key to continue")
            break
        elif read_value(sam.cards)<=21:
            global deck
            sam.cards.append(deck.pop())
            print("Dealer hits.")
            game_interface(dealercard=True)
            dealer_ace()
            sleep(1)
            if read_value(sam.cards)>21:
                print("Dealer busted... congrats everyone, you recieve the double of your bet money")
                double_player_money()
                rst_players()
                sleep(3)
                refresh()
                print_money()
                break
            else:
                game_interface(dealercard=True)
            sleep(1)
    deck=load_cards()
    play_game()
            
def player_turn(player):
    while True:
        if not player.black_jack and not player.bust:
            choice=get_input("Would you like to hit(Take one card from the deck) or stay(keep your cards and end your turn)","h","s")
            if(choice=="h"):
                hit(player)
                show_cards([player])
            else:
                while True:
                    if check_ace(player):
                        ace_input=get_input("You have an ace card, use it as one or eleven?","o","e")
                        if ace_input=="o":
                            print("Ace taken as one")
                            player.cards.remove(find_ace(player))
                            player.cards.append("1")
                        else:
                            print("Ace taken as eleven")
                            player.cards.remove(find_ace(player))
                            player.cards.append("11")
                    check_black_jack(player)
                    check_bust(player)
                    break
                print(f"{player.name}, your card value : {read_value(player.cards)}")
                break

def play_game():
    place_bet()
    assign_cards()
    show_cards(list(players.values()))
    for player in players.values():
        if not player.black_jack and not player.bust:
            print(game_interface())
            print(f"{player.name}, Your turn. Your cards are shown below. Remember your cards")
            print(merge_graphics([card_grapics(x,"\t\t") for x in player.cards]))
            player_turn(player)
    if player_left():
        dealer_turn()
    else:
        print("No player left... resetting game")
        rst_players()
        sleep(3)
        refresh()
        print_money()
        deck=load_cards()
        play_game()

   
if __name__=="__main__":
    players={}
    sam=Dealer("sam")
    deck=load_cards()
    load_players()
    print("All of you get $100 each")
    play_game()