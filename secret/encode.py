# this is the part that will take the text to be cyphered

import re
import secret.not_for_you as hidden # sec, fullname

def encode(text):
    coded = 0;
    for c in text:
        d = match(c)
        coded = (coded * 1000) + d
    return coded

def match(t):
    aNum = 0
    for aA in hidden.sec:
        bNum = 0
        for bA in aA:
            cNum = 0
            for cA in bA:
                if cA == t:
                    return (aNum + 1) * 100 + (bNum + 1) * 10 + cNum + 1
                cNum+=1
            bNum+=1
        aNum+=1
    return 0

def secretCheck(guess):
    if guess == hidden.fullname:
        return True
    return False

def getSecret():
    return str(encode(hidden.fullname))