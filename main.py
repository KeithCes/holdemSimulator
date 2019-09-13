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
import math

deck = []
playerHand = []
opponentHand = []
communityCards = []
straight = False
flush = False
straightFlush = False


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


def checkHand(hand):
    print(hand)
    nums = []
    suits = []
    i = 0
    while i < 7:
        if str(hand[i])[0] == "1":
            nums.append(str(hand[i])[0:2])
            suits.append(str(hand[i])[2])
        else:
            nums.append(str(hand[i])[0])
            suits.append(str(hand[i])[1])
        i += 1
    checkPair(nums)
    checkFlush(suits)
    checkStraight(nums)
    checkStraightFlush()


def checkPair(lst):
    pairs = []
    threeKind = []
    fourKind = []
    fullHouse = False
    twoPair = False
    tempLst = lst
    tempLst.sort()
    tempLst.append("55")
    tempLst.append("56")
    tempLst.append("57")
    tempLst.append("58")
    i = 0
    while i < 7:
        if (tempLst[i] == tempLst[i + 1] and tempLst[i] == tempLst[i + 2] and tempLst[i] == tempLst[i + 3]):
            fourKind.append(tempLst[i])
            tempLst.remove(tempLst[i])
            tempLst.remove(tempLst[i + 1])
            tempLst.remove(tempLst[i + 2])
        elif tempLst[i] == tempLst[i + 1] and tempLst[i] == tempLst[i + 2]:
            threeKind.append(tempLst[i])
            tempLst.remove(tempLst[i])
            tempLst.remove(tempLst[i + 1])
        elif tempLst[i] == tempLst[i + 1]:
            pairs.append(tempLst[i])
            tempLst.remove(tempLst[i])
        i += 1
        if len(pairs) > 2:
            pairs.sort()
            pairs.remove(pairs[0])
        elif len(pairs) > 0 and len(threeKind) > 0:
            fullHouse = True
        elif len(pairs) > 1:
            twoPair = True
    print("Pairs: " + str(pairs))
    print("Two Pair: " + str(twoPair))
    print("Three Piece: " + str(threeKind))
    print("Four Piece: " + str(fourKind))
    print("Full House: " + str(fullHouse))


def checkFlush(lst):
    global flush
    amountS = 0
    amountH = 0
    amountC = 0
    amountD = 0
    i = 0
    while i < 7:
        if lst[i] == "s":
            amountS += 1
        elif lst[i] == "h":
            amountH += 1
        elif lst[i] == "c":
            amountC += 1
        elif lst[i] == "d":
            amountD += 1
        i += 1
    if amountS == 5 or amountH == 5 or amountC == 5 or amountD == 5:
        flush = True
    print("Flush: " + str(flush))


def checkStraight(lst):
    global straight
    q = 0
    while q < 7:
        if lst[q] == "J":
            lst[q] = "11"
        elif lst[q] == "Q":
            lst[q] = "12"
        elif lst[q] == "K":
            lst[q] = "13"
        elif lst[q] == "A":
            lst[q] = "14"
        q += 1
    lst = sorted(lst, key=int)
    straightCount = 1
    i = 0
    while i < 6 and straightCount < 5:
        if int(lst[i]) + 1 == int(lst[i + 1]):
            straightCount += 1
        else:
            straightCount = 1
        i += 1
    if straightCount >= 5:
        straight = True
    while q < 7:
        if lst[q] == "11":
            lst[q] = "J"
        elif lst[q] == "12":
            lst[q] = "Q"
        elif lst[q] == "13":
            lst[q] = "K"
        elif lst[q] == "14":
            lst[q] = "A"
    print("Straight: " + str(straight))


def checkStraightFlush():
    global straight
    global flush
    global straightFlush
    if straight and flush:
        straightFlush = True
    print("Straight Flush: " + str(straightFlush))


def reveal(deck):
    print("Your Hand: " + str(" ".join(playerHand)))
    print("Opponent's Hand: " + str(" ".join(opponentHand)))
    print("Community Cards: " + str(" ".join(communityCards)))
    playerHand.extend(communityCards)
    opponentHand.extend(communityCards)
    checkHand(playerHand)


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
    numberVal = math.ceil(raw / 4) + 1
    suitVal = raw % 4

    # gets suit
    if suitVal == 1:
        suit = "s"
    elif suitVal == 2:
        suit = "c"
    elif suitVal == 3:
        suit = "h"
    elif suitVal == 0:
        suit = "d"

    # gets number value unless card is a face card
    if numberVal == 11:
        number = "J"
    elif numberVal == 12:
        number = "Q"
    elif numberVal == 13:
        number = "K"
    elif numberVal == 14:
        number = "A"
    else:
        number = numberVal

    # appends number and suit, returns them back
    number = str(number)
    number += suit
    return number


playGame()
