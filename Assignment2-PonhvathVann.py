#Name: Ponhvath Vann , Student ID: 1502538
#Assignment 2 for ISCG5420 - Programming Fundamentals

import sys

#Codes for each character

smileyFace = "\u263A"
poop = "\uD83D\uDCA9"
ghost = "\uD83D\uDC7B"
candy = "\uD83C\uDF6C"
wall = "\u2016"
danger = "\u26A0"
skull = "\uD83D\uDC80"
heart = "\u2665"
thumb = "\uD83D\uDC4D"
star = "\u2605"
space = ""


#List of Poop Map

fightScene = """
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒			███████▀▀▀░░░░░░░▀▀▀███████
█████████▒▒▒▒▒▒▒▒▒▒		        █████│░░░░░░░░░░░░░░░░│████						
██████████▒▒▒▒█▄▒▒▒			████└┐░░░░░░░░░░░░░░░┌┘░███
██████████▒▒▒▒██▒▒▒			███░░└┐░░░░░░░░░░░░░░┌┘░░██
███████████▄▄▒██▒▒▒			███░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
█████████▒▒▒▒▒██▒▒▒			██▌░▄██████▄░░░▄██████▄░▐██
█████████▒▒▒▒█████▒			███─┘░░▓▓▓▓░░░░░▓▓▓▓░░└─███
████████▒▒▒▒▒███████			██▀▓▓▓░▓▓▓▓░░░░░▓▓▓▓░▓▓░▀██
█████▒▒▒▒▒▒▒▒██▒███			██▄▓▓▓░▓▓▓▓▄▄▄▄▄▓▓▓▓░▓▓▄███
████████▒▒▒▒▒▒▒████			████▄─┘█████████████└─▄████
██████████▒▒▒▒█████			█████░░▐███████████▌░░█████
███████████▒▒█████▒			██████░░▀█████████▀░░▐█████
████████████████▒▒▒			███████░░░░▓▓▓▓▓░░░░▄██████
████████▒██████▒▒▒▒			████████▄░░░░░░░░░▄████████
████████▒▒███▒▒▒▒▒▒			███████████▓▓▓▓▓███████████
████████▒▒▒▒▒▒▒▒▒▒▒			███████████▓▓▓▓▓███████████
████████▒▒▒▒▒▒▒▒▒▒▒
█████████▒▒▒▒▒▒▒▒▒▒		████╗████████╗██╗███████╗███╗═══███╗████████╗
█████████▒▒▒▒▒▒▒▒▒▒		═██╔╝═══██╔══╝╚█║██╔════╝████╗═████║██╔═════╝
█▄█▄█▄█▄█▒▒▒▒▒▒▒▒▒▒		═██║════██║════╚╝███████╗██╔████╔██║█████╗
███████████▒▒▒▒▒▒▒▒		═██║════██║══════╚════██║██║╚██╔╝██║██╔══╝
█████████████▒▒▒▒▒▒		████╗═══██║══════███████║██║═╚═╝═██║███████╗
▒██████▒███████▒▒▒▒
▒███████▒███████▒▒▒
▒▒████████████▒▒▒▒▒
███████████▒▒▒▒▒▒▒▒
████████▒▒▒▒▒▒▒▒▒▒▒
████████▒▒▒▒▒▒▒▒▒▒▒
█▒██████▒▒▒▒▒▒▒▒▒▒▒
▌▒██████▒▒▒▒▒▒▒▒▒▒▒
▒▒██████▒▒▒▒▒▒▒▒▒▒▒
▒▒█████████▄▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ """

map0 = """\u2016\u263A     \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016***\uD83D\uDC80***\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605"""

map1 = """\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9     \u263A\u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016***\uD83D\uDC80***\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605"""


map2 = """\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016\u263A     \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016***\uD83D\uDC80***\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605"""


map3 = """\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9     \u263A\u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016***\uD83D\uDC80***\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605"""



map4 = """\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016\u263A     \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016***\uD83D\uDC80***\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605"""


map5 = """\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9     \u263A\u2016
\u2016***\uD83D\uDC80***\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605"""

                                 
fightSceneTie = """\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016\u263A Tie \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605"""


fightSceneWin = """\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016\u263A K.O \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605"""

map6 = """\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9     \u263A\u2016
\u2016      \uD83D\uDCA9\u2016
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605"""


map7 = """\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016      \uD83D\uDCA9\u2016
\u2016\uD83D\uDCA9      \u2016
\u2016\u263A     \uD83D\uDCA9\u2016
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605"""


#List of Ghost Map
#v stands for version

mapv0 = """\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016***\uD83D\uDC80***\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016\u263A     \uD83D\uDC7B\u2016
"""

mapv1 = """\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016***\uD83D\uDC80***\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B     \u263A\u2016
\u2016      \uD83D\uDC7B\u2016
"""

mapv2 = """\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016***\uD83D\uDC80***\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016\u263A     \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
"""

mapv3 = """\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016***\uD83D\uDC80***\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B     \u263A\u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
"""

mapv4 = """\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016***\uD83D\uDC80***\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016\u263A     \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
"""


mapv5 = """\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016***\uD83D\uDC80***\u2016
\u2016\uD83D\uDC7B     \u263A\u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
"""


fightSceneTie1 = """\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016\u263A Tie \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
"""


fightSceneWin1 = """\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016\u263A K.O \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
"""


mapv6 = """\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B     \u263A\u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
"""


mapv7 = """\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2605\u2605\u2605\u2605\u2605\u2605
\u2016\u263A     \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
\u2016\uD83D\uDC7B      \u2016
\u2016      \uD83D\uDC7B\u2016
"""



#Intro to the game

print("Welcome to the Escape game!!!!!!\n*********************************\n")
name = input("Please enter your name: ")
while len(name) <= 0 or len(name) <= 3 :
    print("Name must be more than 3 characters.")
    name = input("Please enter your name: ")
else :
    print("\nHey there",name+"!\n*********************************")

#Move to the right for poop map

def moveRight(answer) :
    while answer not in ["0","1"]:
        print("Please enter 0 or 1 to proceed to the stage.")
        answer = input("Enter 0 to go left or Enter 1 to go right: ")
    else :
        if answer == "0" :
            answer == print("Oppps you lose! You stepped on a poop.")
            playAgain()
        elif answer == "1" :
            i = 0
            while i < 10:
                i += 1
    return answer


#Move to the left for poop map
            
def moveLeft(answer) :
    while answer not in ["0","1"]:
        print("Please enter 0 or 1 to proceed to the stage.")
        answer = input("Enter 0 to go left or Enter 1 to go right: ")
    else :
        if answer == "0" :
            i = 0
            while i < 10:
                i += 1 
        elif answer == "1" :
            answer == print("Oppps you lose! You stepped on a poop.")
            playAgain()
    return answer        

#Move to the right for ghost map
#v stands for version

def moveRightv1(answer) :
    while answer not in ["0","1"]:
        print("Please enter 0 or 1 to proceed to the stage.")
        answer = input("Enter 0 to go left or Enter 1 to go right: ")
    else :
        if answer == "0" :
            answer == print("Oppps you lose! You meet the ghost.")
            playAgain()
        elif answer == "1" :
            i = 0
            while i < 10:
                i += 1
    return answer


#Move to the left for ghost map
            
def moveLeftv1(answer) :
    while answer not in ["0","1"]:
        print("Please enter 0 or 1 to proceed to the stage.")
        answer = input("Enter 0 to go left or Enter 1 to go right: ")
    else :
        if answer == "0" :
            i = 0
            while i < 10:
                i += 1 
        elif answer == "1" :
            answer == print("Oppps you lose! You meet the ghost.")
            playAgain()
    return answer

#Reach Goal
def reachGoal(answer):
    while answer not in ["0","1"] :
        answer = input("Enter 0 to go left or Enter 1 to go right: ")
    else:
        if answer == "0" or answer == "1" :
            print("""
_.█████████████████ 
_ ██████████████████ 
████████████████████ 
█████████████████████ 
_█_________▄▄▄▄_ ▄▄▄▄_█ 
_█__█████_▐▓▓▌_▐▓▓▌_█ 
_█__█████_▐▓▓▌_▐▓▓▌_█ 
_█__█████_▐▓▓▌_▐▓▓▌_█ 
_█__█████_▀▀▀▀_ ▀▀▀▀ █✿ ✿ 
_█__█████_____________ █(\\|/) 
_____________██ _____________██ 
_____________█ 
______________█ 
_______________██ 
_________________██ 
___________________██ 
__________________██ 
_________________███ 
______________████ 
___________█████ 
_________██████ 
_______██████
You have reached the goal!\nGreat Job! You Won.\n""")
    return answer






#Fight Scene
heartForPlayer = [heart,heart,heart,heart,heart,heart]
heartForEnemy = [heart,heart,heart,heart,heart,heart,heart,heart]
def fightScene():
    print("This is your faith. All in or nothing.")
    print("""
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒			███████▀▀▀░░░░░░░▀▀▀███████
█████████▒▒▒▒▒▒▒▒▒▒		        █████│░░░░░░░░░░░░░░░░│████
██████████▒▒▒▒█▄▒▒▒			████└┐░░░░░░░░░░░░░░░┌┘░███
██████████▒▒▒▒██▒▒▒			███░░└┐░░░░░░░░░░░░░░┌┘░░██
███████████▄▄▒██▒▒▒			███░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
█████████▒▒▒▒▒██▒▒▒			██▌░▄██████▄░░░▄██████▄░▐██
█████████▒▒▒▒█████▒			███─┘░░▓▓▓▓░░░░░▓▓▓▓░░└─███
████████▒▒▒▒▒███████			██▀▓▓▓░▓▓▓▓░░░░░▓▓▓▓░▓▓░▀██
█████▒▒▒▒▒▒▒▒██▒███			██▄▓▓▓░▓▓▓▓▄▄▄▄▄▓▓▓▓░▓▓▄███
████████▒▒▒▒▒▒▒████			████▄─┘█████████████└─▄████
██████████▒▒▒▒█████			█████░░▐███████████▌░░█████
███████████▒▒█████▒			██████░░▀█████████▀░░▐█████
████████████████▒▒▒			███████░░░░▓▓▓▓▓░░░░▄██████
████████▒██████▒▒▒▒			████████▄░░░░░░░░░▄████████
████████▒▒███▒▒▒▒▒▒			███████████▓▓▓▓▓███████████
████████▒▒▒▒▒▒▒▒▒▒▒			███████████▓▓▓▓▓███████████
████████▒▒▒▒▒▒▒▒▒▒▒
█████████▒▒▒▒▒▒▒▒▒▒		████╗████████╗██╗███████╗███╗═══███╗████████╗
█████████▒▒▒▒▒▒▒▒▒▒		═██╔╝═══██╔══╝╚█║██╔════╝████╗═████║██╔═════╝
█▄█▄█▄█▄█▒▒▒▒▒▒▒▒▒▒		═██║════██║════╚╝███████╗██╔████╔██║█████╗
███████████▒▒▒▒▒▒▒▒		═██║════██║══════╚════██║██║╚██╔╝██║██╔══╝
█████████████▒▒▒▒▒▒		████╗═══██║══════███████║██║═╚═╝═██║███████╗
▒██████▒███████▒▒▒▒
▒███████▒███████▒▒▒
▒▒████████████▒▒▒▒▒
███████████▒▒▒▒▒▒▒▒
████████▒▒▒▒▒▒▒▒▒▒▒
████████▒▒▒▒▒▒▒▒▒▒▒
█▒██████▒▒▒▒▒▒▒▒▒▒▒""")
    print("Player HP =",*heartForPlayer,"        ","Enemy HP =",*heartForEnemy)

#Heal the player and fight the enemy
def fightEnemy(userCommand):

    while userCommand not in ["H","A"] :
        print("Please insert \"H\" to Heal or \"A\" to Attack!")
        userCommand = input("Press \"H\" to heal and \"A\" to attack: ")
    else: 
        if userCommand == "H" :
            #Player Heal
            numOfHeart = 0
            while numOfHeart < 3 :      #This loop will plus 2 hearts to the user each time they heal themself
                heartForPlayer.append(heart)
                numOfHeart += 1
            print("You heal yourself. HP +2")
            
            #Enemy Attack
            heartForPlayer.pop()
            print("Enemy attacked you. -1 HP")
            print("""
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒			███████▀▀▀░░░░░░░▀▀▀███████
█████████▒▒▒▒▒▒▒▒▒▒		        █████│░░░░░░░░░░░░░░░░│████
██████████▒▒▒▒█▄▒▒▒			████└┐░░░░░░░░░░░░░░░┌┘░███
██████████▒▒▒▒██▒▒▒			███░░└┐░░░░░░░░░░░░░░┌┘░░██
███████████▄▄▒██▒▒▒			███░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
█████████▒▒▒▒▒██▒▒▒			██▌░▄██████▄░░░▄██████▄░▐██
█████████▒▒▒▒█████▒			███─┘░░▓▓▓▓░░░░░▓▓▓▓░░└─███
████████▒▒▒▒▒███████			██▀▓▓▓░▓▓▓▓░░░░░▓▓▓▓░▓▓░▀██
█████▒▒▒▒▒▒▒▒██▒███			██▄▓▓▓░▓▓▓▓▄▄▄▄▄▓▓▓▓░▓▓▄███
████████▒▒▒▒▒▒▒████			████▄─┘█████████████└─▄████
██████████▒▒▒▒█████			█████░░▐███████████▌░░█████
███████████▒▒█████▒			██████░░▀█████████▀░░▐█████
████████████████▒▒▒			███████░░░░▓▓▓▓▓░░░░▄██████
████████▒██████▒▒▒▒			████████▄░░░░░░░░░▄████████
████████▒▒███▒▒▒▒▒▒			███████████▓▓▓▓▓███████████
████████▒▒▒▒▒▒▒▒▒▒▒			███████████▓▓▓▓▓███████████
████████▒▒▒▒▒▒▒▒▒▒▒
█████████▒▒▒▒▒▒▒▒▒▒		████╗████████╗██╗███████╗███╗═══███╗████████╗
█████████▒▒▒▒▒▒▒▒▒▒		═██╔╝═══██╔══╝╚█║██╔════╝████╗═████║██╔═════╝
█▄█▄█▄█▄█▒▒▒▒▒▒▒▒▒▒		═██║════██║════╚╝███████╗██╔████╔██║█████╗
███████████▒▒▒▒▒▒▒▒		═██║════██║══════╚════██║██║╚██╔╝██║██╔══╝
█████████████▒▒▒▒▒▒		████╗═══██║══════███████║██║═╚═╝═██║███████╗
▒██████▒███████▒▒▒▒
▒███████▒███████▒▒▒
▒▒████████████▒▒▒▒▒
███████████▒▒▒▒▒▒▒▒
████████▒▒▒▒▒▒▒▒▒▒▒
████████▒▒▒▒▒▒▒▒▒▒▒
█▒██████▒▒▒▒▒▒▒▒▒▒▒""")
            print("Player HP =",*heartForPlayer,"        ","Enemy HP =",*heartForEnemy)
        elif userCommand == "A" :
            heartForEnemy.pop()
            heartForPlayer.pop()
            print("You attacked the enemy. Enemy HP -1!\nEnemy attacked you. -1 HP!")
            print("""
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒			███████▀▀▀░░░░░░░▀▀▀███████
█████████▒▒▒▒▒▒▒▒▒▒		        █████│░░░░░░░░░░░░░░░░│████
██████████▒▒▒▒█▄▒▒▒			████└┐░░░░░░░░░░░░░░░┌┘░███
██████████▒▒▒▒██▒▒▒			███░░└┐░░░░░░░░░░░░░░┌┘░░██
███████████▄▄▒██▒▒▒			███░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
█████████▒▒▒▒▒██▒▒▒			██▌░▄██████▄░░░▄██████▄░▐██
█████████▒▒▒▒█████▒			███─┘░░▓▓▓▓░░░░░▓▓▓▓░░└─███
████████▒▒▒▒▒███████			██▀▓▓▓░▓▓▓▓░░░░░▓▓▓▓░▓▓░▀██
█████▒▒▒▒▒▒▒▒██▒███			██▄▓▓▓░▓▓▓▓▄▄▄▄▄▓▓▓▓░▓▓▄███
████████▒▒▒▒▒▒▒████			████▄─┘█████████████└─▄████
██████████▒▒▒▒█████			█████░░▐███████████▌░░█████
███████████▒▒█████▒			██████░░▀█████████▀░░▐█████
████████████████▒▒▒			███████░░░░▓▓▓▓▓░░░░▄██████
████████▒██████▒▒▒▒			████████▄░░░░░░░░░▄████████
████████▒▒███▒▒▒▒▒▒			███████████▓▓▓▓▓███████████
████████▒▒▒▒▒▒▒▒▒▒▒			███████████▓▓▓▓▓███████████
████████▒▒▒▒▒▒▒▒▒▒▒
█████████▒▒▒▒▒▒▒▒▒▒		████╗████████╗██╗███████╗███╗═══███╗████████╗
█████████▒▒▒▒▒▒▒▒▒▒		═██╔╝═══██╔══╝╚█║██╔════╝████╗═████║██╔═════╝
█▄█▄█▄█▄█▒▒▒▒▒▒▒▒▒▒		═██║════██║════╚╝███████╗██╔████╔██║█████╗
███████████▒▒▒▒▒▒▒▒		═██║════██║══════╚════██║██║╚██╔╝██║██╔══╝
█████████████▒▒▒▒▒▒		████╗═══██║══════███████║██║═╚═╝═██║███████╗
▒██████▒███████▒▒▒▒
▒███████▒███████▒▒▒
▒▒████████████▒▒▒▒▒
███████████▒▒▒▒▒▒▒▒
████████▒▒▒▒▒▒▒▒▒▒▒
████████▒▒▒▒▒▒▒▒▒▒▒
█▒██████▒▒▒▒▒▒▒▒▒▒▒""")
            print("Player HP =",*heartForPlayer,"        ","Enemy HP =",*heartForEnemy)

        
#Run the Fight for Poop Map
def runFightScene():
    while len(heartForPlayer) != 0 and len(heartForEnemy) != 0 :
        fightEnemy(input("Press \"H\" to heal and \"A\" to attack: "))
    else :
        if len(heartForPlayer) == 0 and len(heartForEnemy) == 0 :
            print("It's a tie. See you next time!")
            print(fightSceneTie)
            
        elif len(heartForPlayer) == 0 :
            print("You lose! Game Over!")
            resetHeart()
            playAgain()
        elif len(heartForEnemy) == 0 :
            print("You win the fight!")
            print(fightSceneWin)

#Run the Fight for Ghost Map
def runFightScene1():
    while len(heartForPlayer) != 0 and len(heartForEnemy) != 0 :
        fightEnemy(input("Press \"H\" to heal and \"A\" to attack: "))
    else :
        if len(heartForPlayer) == 0 and len(heartForEnemy) == 0 :
            print("It's a tie. See you next time!")
            print(fightSceneTie1)
            
        elif len(heartForPlayer) == 0 :
            print("You lose! Game Over!")
            resetHeart()
            playAgain()
        elif len(heartForEnemy) == 0 :
            print("You win the fight!")
            print(fightSceneWin1)



#Reset the list of the heart to the orginal list for the next run round, if the player decide to play again
def resetHeart():
    i = len(heartForPlayer)
    while len(heartForPlayer)<6:
        heartForPlayer.append(heart)
        i += 1
    i = len(heartForEnemy)
    while len(heartForEnemy)<8:
        heartForEnemy.append(heart)
        i +=1

#Instruction
def instruction():
    print("""
 __________________________________
|                                  |
| Instruction:                     |
| 1/ Avoid the obstacle            |
| 2/ Fight the enemy               |
| 3/ Reach the goal to win!!       |
|__________________________________|""")
    goBack = input("Enter \"ok\" to return to the interface: ")
    while goBack != "ok":
        goBack = input("Enter \"ok\" to return to the interface: ")
    else :
        print("""Please choose the follwing options:
     __________________________________
    |                                  |                     
    |             1/ Play              |   
    |          2/ Instruction          |
    |             3/ Exit              |
    |__________________________________|""")

        print("""\nEnter "P" to play\nEnter "I" to read the instruction\nEnter "E" to exit the game""")
        choice = input("Please choose your choice: ")
        while choice not in ["P","I","E"]:
            choice = input("Please choose your choice: ")
        else :
            if choice == "P" :
                runGame()
            elif choice == "I" :
                instruction()
            elif choice == "E" :
                exitGame()


#Quit the game at the beginning
def exitGame():
    exitQuestion = input("Are you sure you want to quit the game? (y/n)")
    while exitQuestion not in ["y","n"] :
        exitQuestion = input("Are you sure you want to quit the game? (y/n)")
    else :
        if exitQuestion == "n":
            print("""Please choose the follwing options:
     __________________________________
    |                                  |                     
    |             1/ Play              |   
    |          2/ Instruction          |
    |             3/ Exit              |
    |__________________________________|""")

            print("""\nEnter "P" to play\nEnter "I" to read the instruction\nEnter "E" to exit the game""")
            choice = input("Please choose your choice: ")
            while choice not in ["P","I","E"]:
                choice = input("Please choose your choice: ")
            else :
                if choice == "P" :
                    runGame()
                elif choice == "I" :
                    instruction()
                elif choice == "E" :
                    exitGame()
        elif exitQuestion == "y":
            sys.exit()

#Play Again
def playAgain():
    replayAnswer = input("Do you want to play again (y/n): ")
    while replayAnswer not in ["y","n"]:
        replayAnswer = input("Do you want to play again (y/n): ")
    else :
        if replayAnswer == "n" :
            sys.exit()
        elif replayAnswer == "y" :
            runApplication()


#Poop Map function
def maps():
    i = 0
    while i < 8 :
        if i == 0 :
            print(map0)
            moveRight(input("Enter 0 to go left or Enter 1 to go right: "))
        if i == 1:
            print(map1)
            moveLeft(input("Enter 0 to go left or Enter 1 to go right: "))
        if i == 2:
            print(map2)
            moveRight(input("Enter 0 to go left or Enter 1 to go right: "))
        if i == 3:
            print(map3)
            moveLeft(input("Enter 0 to go left or Enter 1 to go right: "))
        if i == 4:
            print(map4)
            moveRight(input("Enter 0 to go left or Enter 1 to go right: "))
        if i == 5:
            print(map5)
            fightScene()
            fightEnemy(input("Press \"H\" to heal and \"A\" to attack: "))
            runFightScene()
            resetHeart()
            moveRight(input("Enter 0 to go left or Enter 1 to go right: "))
        if i == 6:
            print(map6)
            moveLeft(input("Enter 0 to go left or Enter 1 to go right: "))
        if i == 7:
            print(map7)
            reachGoal(input("Enter 0 to go left or Enter 1 to go right: "))
            playAgain()
        i += 1

#Ghost Map function
def maps1():
    i = 0
    while i < 8 :
        if i == 0 :
            print(mapv0)
            moveRightv1(input("Enter 0 to go left or Enter 1 to go right: "))
        if i == 1:
            print(mapv1)
            moveLeftv1(input("Enter 0 to go left or Enter 1 to go right: "))
        if i == 2:
            print(mapv2)
            moveRightv1(input("Enter 0 to go left or Enter 1 to go right: "))
        if i == 3:
            print(mapv3)
            moveLeftv1(input("Enter 0 to go left or Enter 1 to go right: "))
        if i == 4:
            print(mapv4)
            moveRightv1(input("Enter 0 to go left or Enter 1 to go right: "))
        if i == 5:
            print(mapv5)
            fightScene()
            fightEnemy(input("Press \"H\" to heal and \"A\" to attack: "))
            runFightScene1()
            resetHeart()
            moveRightv1(input("Enter 0 to go left or Enter 1 to go right: "))
        if i == 6:
            print(mapv6)
            moveLeftv1(input("Enter 0 to go left or Enter 1 to go right: "))
        if i == 7:
            print(mapv7)
            reachGoal(input("Enter 0 to go left or Enter 1 to go right: "))
            playAgain()
        i += 1

#Loop for the map

def runGame():
    mapChoice = input("Choose (P) for Poop Map or choose (G) for Ghost Map: ")
    while mapChoice not in ["P","G"] :
        mapChoice = input("Choose (P) for Poop map or choose (G) for ghost map: ")
    else :
        if mapChoice == "P" :
            i = 0
            while i < 8 :
                maps()
                i += 1
        elif mapChoice == "G" :
            i = 0
            while i < 8 :
                maps1()
                i += 1



#Application run

def runApplication():
    print("""Please choose the follwing options:
     __________________________________
    |                                  |                     
    |             1/ Play              |   
    |          2/ Instruction          |
    |             3/ Exit              |
    |__________________________________|""")

    print("""\nEnter "P" to play\nEnter "I" to read the instruction\nEnter "E" to exit the game""")
    choice = input("Please choose your choice: ")
    while choice not in ["P","I","E"]:
        choice = input("Please choose your choice: ")
    else :
        if choice == "P" :
            runGame()
        elif choice == "I" :
            instruction()
        elif choice == "E" :
            exitGame()
            
runApplication()




