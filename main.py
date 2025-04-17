#  this is the file you're supposed to run

import secret.encode as encode


def guess():
    guessRight = False
    while guessRight != True:
       print("\nmy full name is encoded as as " + encode.getSecret())
       guess = input("what do you think my full name is?\n")
       guessRight = encode.secretCheck(guess)
       if guessRight != True:
           print("that is incorrect :( try again.")
    print("\nthat's my full name.  congratulations :)")

def enter():
    tbc = input("\nplease provide something to be encoded: ")
    print("\"" + tbc + "\" can be encoded as the following:")
    print(str(encode.encode(tbc)))


if __name__ == "__main__":
    print("hello, welcome to the thing for hw4.")
    print("to enter your own string respond with 1")
    print("to guess my full name respond with 2")
    tick = 2
    escape = False
    while not escape:
        tick = input("what do you want to do: ")
        if (tick == "1") | (tick == "2"):
            escape = True
        else:
            print("that is an invalid input, try again.")
    if tick == "1":
        enter()
    if tick == "2":
        guess()
