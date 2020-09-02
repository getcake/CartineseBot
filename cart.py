#!/usr/bin/python3
import random as rd
import sys


ip = ""

cartinese = [" ++** ",      #1
       '* !! *',    #2
       "* Fuc !  *",
       "*+!:)  ❤️  !!",         #3
       " rEd . ",   #4
       " *! +:) ",  #5
       "+*Lit **!++ ! ",    #6
       "💕  +* ",   #7
       " +:) ",     #8
       "🖤& * ",    #9
       ':) xo!',    #10
       "* ok !+ ",  #11
       "💔 ",       #12
       " 🦋",       #13
       " ",         #14
       " ",         #15
       "  "         #16
       " ",         #17
       " ",         #18
       " ",         #19
       " ",         #20
       ]


def translate(ip):
    op = str(ip.split(' '))
    z = ''
    with open('test.txt', 'w') as test:
        for word in op:

            x = word.replace(' ', str(rd.choices(cartinese,
                                                weights=[4, 5, 2, 2, 3, 3, 2, 4, 5, 3, 3, 4, 5, 5, 8, 7, 5,10,12,6

                                                        ])))

            x = x.replace(']', '').replace('[', '').replace(
                "'", '').replace(',', '').replace('  ', '')
            print(x, end="", file=test)



translate(ip)
