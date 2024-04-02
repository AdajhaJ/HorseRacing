import random
import time

A_B_C_D = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e"]
horses = [
    "Smurda",
    "Nitro",
    "Cyclone",
    "Titan",
    "Comet"
]
money = 0
wager = 0
chosen = ""
response = ""

def clear():
    print("\033[H\033[J")

def animation(text, new_line=True):
    animated_text = ""
    for char in text:
        animated_text += char
        print(char, end='', flush=True)
        time.sleep(0.05)  # typing speed
    if new_line:
        print()  # Print a newline at the end if new_line is True
    return animated_text

def winner_announcement(new_line=False):
    message = "The winner is "
    animated_message = animation(message, new_line=new_line)
    loading_dots = ["", ".", ".", "."] 
    for dot in loading_dots:
        print(dot, end="", flush=True)  # Print the dots without newline
        time.sleep(0.5) 



# Start
clear()
animation("Hello! Welcome to the Gambling Den!")
animation("What is your name? ")

#requires them to input a name
while True:
    name = input()
    if name == "":
        animation("Please input a name.")
    else: 
        break

name = name.capitalize()
animation("Welcome, " + name + "!")
time.sleep(0.75)
clear()
animation("This game is about horse racing. You will be able to bet on which horse you think will win.")
time.sleep(0.75)
animation("If the horse you choose loses, you will lose money and vice versa.")
animation("I will give you 20 bucks to start. Best of luck!")
money = 20
time.sleep(0.75)
clear()

#Game
def game_loop():
    global money, response
    
    balence_setup = (name + "'s money: $" + str(money))
    balence = balence_setup.center(50, "-")
    print(balence)

    #Wager Screen
    animation("How much money do you wish to wager?")
    print("A) $1\nB) $5\nC) $" + str(money//2) + "\nD) $" + str(money))
    response =""
    while response not in A_B_C_D:
        response = input("")
        if response == "A" or response == "a":
            wager = 1
        elif response == "B" or response == "b":
            wager = 5
        elif response == "C" or response == "c":
            wager = money//2
        elif response == "D" or response == "d":
            wager = money
        else: 
            animation("Please select a valid response.")
    clear()

    #Horse Selection
    animation("Now pick one of our trusty horses to gamble on.")
    print("A) Smurda\nB) Nitro\nC) Cyclone\nD) Titan\nE) Comet")
    response = ""
    while response not in A_B_C_D:
        response = input("")
        if response == "A" or response == "a":
            chosen = "Smurda"
        elif response == "B" or response == "b":
            chosen = "Nitro"
        elif response == "C" or response == "c":
            chosen = "Cyclone"
        elif response == "D" or response == "d":
            chosen = "Titan"
        elif response == "E" or response == "e":
            chosen = "Comet"
        else: 
            animation("Please select a valid response.")
    clear()

    #Winner Horse
    animation("Let the race begin!")
    time.sleep(0.75)
    winner_announcement()
    winner = random.choice(horses)
    animation(winner)
    time.sleep(0.75)

    #Money Addition/Revoke
    if winner == chosen:
        animation("Congratulations! Your wager will be added to you account.")
        money += wager
    else:
        animation("Tough luck. You are sure to get them next time!")
        animation("However, I am going to have to take your money.")
        money -= wager
    time.sleep(0.75)
    clear()

    #Game continuation
    if money > 0:
        game_loop()
    else:
        animation("You have no more money to spend.")
        animation("This is where I must say goodbye. Thanks for playing!")
        quit()

game_loop()