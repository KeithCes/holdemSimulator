"""Copyright (c) 2017 * Keith Cestaro
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


from random import shuffle

deck = []
playerHand = []
opponentHand = []
communityCards = []


def addCards():
    i = 1
    while i <= 52:
        deck.append(i)
        i += 1


def deal(deck):
    addCards()
    shuffle(deck)
    translateCard(playerHand, 0)
    translateCard(playerHand, 1)
    translateCard(opponentHand, 0)
    translateCard(opponentHand, 1)
    displayCards()
    input()


def flop(deck):
    translateCard(communityCards, 0)
    translateCard(communityCards, 1)
    translateCard(communityCards, 2)
    displayCards()
    input()


def turn(deck):
    translateCard(communityCards, 3)
    displayCards()
    input()


def river(deck):
    translateCard(communityCards, 4)
    displayCards()
    input()


def reveal(deck):
    print("Your Hand: " + str(" ".join(playerHand)))
    print("Your Hand: " + str(" ".join(opponentHand)))
    print("Community Cards: " + str(" ".join(communityCards)))
    input()


def translateCard(loc, num):
    moveCard(deck, loc)
    loc[num] = convertCard(loc[num])


def displayCards():
    print("Your Hand: " + str(" ".join(playerHand)))
    print("Opponent's Hand: X X")
    print("Community Cards: " + str(" ".join(communityCards)))


def moveCard(x, y):
    temp = x[0]
    y.append(x[0])
    x.remove(temp)


def playGame():
    deal(deck)
    flop(deck)
    turn(deck)
    river(deck)
    reveal(deck)


def convertCard(raw):
    if raw == 1:
        return "2s"
    elif raw == 2:
        return "2c"
    elif raw == 3:
        return "2h"
    elif raw == 4:
        return "2d"
    elif raw == 5:
        return "3s"
    elif raw == 6:
        return "3c"
    elif raw == 7:
        return "3h"
    elif raw == 8:
        return "3d"
    elif raw == 9:
        return "4s"
    elif raw == 10:
        return "4c"
    elif raw == 11:
        return "4h"
    elif raw == 12:
        return "4d"
    elif raw == 13:
        return "5s"
    elif raw == 14:
        return "5c"
    elif raw == 15:
        return "5h"
    elif raw == 16:
        return "5d"
    elif raw == 17:
        return "6s"
    elif raw == 18:
        return "6c"
    elif raw == 19:
        return "6h"
    elif raw == 20:
        return "6d"
    elif raw == 21:
        return "7s"
    elif raw == 22:
        return "7c"
    elif raw == 23:
        return "7h"
    elif raw == 24:
        return "7d"
    elif raw == 25:
        return "8s"
    elif raw == 26:
        return "8c"
    elif raw == 27:
        return "8h"
    elif raw == 28:
        return "8d"
    elif raw == 29:
        return "9s"
    elif raw == 30:
        return "9c"
    elif raw == 31:
        return "9h"
    elif raw == 32:
        return "9d"
    elif raw == 33:
        return "10s"
    elif raw == 34:
        return "10c"
    elif raw == 35:
        return "10h"
    elif raw == 36:
        return "10d"
    elif raw == 37:
        return "Js"
    elif raw == 38:
        return "Jc"
    elif raw == 39:
        return "Jh"
    elif raw == 40:
        return "Jd"
    elif raw == 41:
        return "Qs"
    elif raw == 42:
        return "Qc"
    elif raw == 43:
        return "Qh"
    elif raw == 44:
        return "Qd"
    elif raw == 45:
        return "Ks"
    elif raw == 46:
        return "Kc"
    elif raw == 47:
        return "Kh"
    elif raw == 48:
        return "Kd"
    elif raw == 49:
        return "As"
    elif raw == 50:
        return "Ac"
    elif raw == 51:
        return "Ah"
    elif raw == 52:
        return "Ad"
    else:
        return "error"


playGame()
