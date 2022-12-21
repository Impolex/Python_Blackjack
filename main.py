import random


def newdeck():
    numbers = [('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('Jack', 10),
               ('Queen', 10), ('King', 10), ('Ace', 0)]
    classes = ['of Spades', 'of Hearts', 'of Clubs', 'of Diamonds']
    return [(i[0] + ' ' + j, i[1]) for i in numbers for j in classes]


def replay():
    while True:
        print('Do you want to play again? (y/n)')
        n = input()
        if n == 'y' or n == 'n':
            return n == 'y'
        else:
            print('Please input "y" or "n"')


def dealplayercard(ls, playerval):
    if len(ls) == 0:
        print('There are no more cards in the deck')
    else:
        card = random.choice(ls)
        deck.remove(card)
        print('Player has been delt a', card[0], )
        if card[1] == 0:
            while True:
                print('Should the Ace be counted as "1" or "11"?')
                acechoice = input()
                if acechoice == '1':
                    playerval = playerval + 1
                    break
                elif acechoice == '11':
                    playerval = playerval + 11
                    break
                else:
                    print('Please input "1" or "11"')
        playerval = playerval + card[1]
        print('Player:', playerval)
    return ls, playerval


def dealdealercard(ls, dealerval, dealercard):
    if len(ls) == 0:
        print('There are no more cards in the deck')
    else:
        card = random.choice(ls)
        deck.remove(card)
        dealercard = card[0]
        print('Dealer has been delt a card face-down')
        if card[1] == 0:
            if dealerval + 11 > 21:
                dealerval = dealerval + 1
            else:
                dealerval = dealerval + 11
        else:
            dealerval = dealerval + card[1]
    return ls, dealerval, dealercard


def dealdealercardup(ls, dealerval, dealercard2):
    if len(ls) == 0:
        print('There are no more cards in the deck')
    else:
        card = random.choice(ls)
        deck.remove(card)
        print('Dealer has been delt a', card[0])
        dealercard2 = card[0]
        if card[1] == 0:
            if dealerval + 11 > 21:
                dealerval = dealerval + 1
                print('Dealer counts the Ace as "1"')
            else:
                dealerval = dealerval + 11
                print('Dealer counts the Ace as "11"')
        else:
            dealerval = dealerval + card[1]
    return ls, dealerval, dealercard2


def playerhit(playerval, dealerval, ls, dealercard1, dealercard2, dealervalvis):
    while True:
        print('The Dealer has a', dealercard2, 'and a face-down card in their hand(', dealervalvis, ')')
        print('Current player hand:', playerval)
        print('Do you want to hit? (y/n)')
        a = input()
        print('|-----------------------------------------------------------------------------------------------------|')

        if a == 'y' or a == 'n':
            if a == 'n':
                print('Dealer turns their first card up. It´s a', dealercard1)
                ls, dealerval = dealer17(ls, dealerval)
                if dealerval > 21:
                    playerval = checkbust('Dealer', dealerval)
                    return ls, playerval
                else:
                    playerval = compare(playerval, dealerval)
                    return ls, playerval
            else:
                ls, playerval = dealplayercard(deck, playerval)
        else:
            print('Please input "y" or "n"')

        return ls, playerval


def dealer17(ls, dealerval):
    while True:
        if dealerval < 17:
            ls, dealerval, x = dealdealercardup(ls, dealerval, 0)

        else:
            return ls, dealerval


def check21(n):
    print(n, 'has exactly 21 points, and has therefore won. Game over')
    return 'gameover'


def checkbust(n, val):
    print(n, 'has gone bust.(', val, ') Game over')
    return 'gameover'


def winner(playerval, dealerval, n):
    print(n, 'has a higher hand, and therefore wins(', playerval, 'vs', dealerval, '). Game over')


def tie(playerval):
    print('Player and dealer tied.(', playerval, ') Game over')


def compare(playerval, dealerval):
    if playerval > dealerval:
        winner(playerval, dealerval, 'Player')
    elif playerval < dealerval:
        winner(playerval, dealerval, 'Dealer')
    else:
        tie(playerval)
    return 'gameover'


def initial21(playerval):
    if playerval == 21:
        check21('Player')
        return True


while True:
    print('The game begins')
    print('The deck is shuffled')

    deck = newdeck()
    playervalue = 0
    dealervalue = 0
    dealerfirstcard = None
    dealersecondcard = None

    deck, playervalue = dealplayercard(deck, playervalue)
    deck, dealervalue, dealerfirstcard = dealdealercard(deck, dealervalue, dealerfirstcard)
    dealervalue1 = dealervalue

    deck, playervalue = dealplayercard(deck, playervalue)

    deck, dealervalue, dealersecondcard = dealdealercardup(deck, dealervalue, dealersecondcard)
    visdealval = dealervalue - dealervalue1

    if not initial21(playervalue):
        while True:
            deck, playervalue = playerhit(playervalue, dealervalue, deck, dealerfirstcard, dealersecondcard, visdealval)

            if playervalue == 'gameover':
                break

            if playervalue == 21:
                check21('Player')
                break

            elif playervalue > 21:
                checkbust('Player', playervalue)
                break

    if not replay():
        break
