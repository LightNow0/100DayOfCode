from random import choice
print('''

                              ________
                             //_/==/_/    _   _
              ________      //|     /|   (_)_(_)                 ________
     _________)_______\____//_|____/_|__/_/____/__.-------._____/|_______|
    / _____________________/______________=o|_____               |___.___|
    \_    ________        /                 |  __/              _/>>>_>>>/
   (__)[]/   __   \       \              ___|___/ _________ [_](_____()___)
     \==/  .\  /.  |=GT500=\================|=== / .\  /.  \===_/__[__]__)
      \_\  | () |  |____________________________/  | () |   \_/_()___()/
         \ `/__\'  /. '/                        \  `/__\'  /    /
          `._____.'---'                          '.      .'___.'
                  jro                              ~~~~~~

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n')

if choice1 == "left":
    choice2 = input("You've come to a lake. There is an insland the middle of the lake."
                    'Type "wait" to wait for a boat.'
                    'Type "swim" across.\n').lower()
    if choice2 == "swim":
        choice3 = input("You arrive at the island unharmed."
                        "There is a house with 3 doors."
                        "One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if choice3 == "blue":
            print("You found the treasure! You Win!")
        if choice3 == "yellow":
            print("This a fake door. You Lose!")
        if choice3 == "red":
            print("This a fake door. You Lose!")
    else:
        print("You got attacked by an angry trout. You Lose!")
else:
    print("You fell in to a hole. Game Over")