# This is a sample Python script.
import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


opt = ("rock","paper","sissors")
computer = random.choice(opt)

player = input(" enter your choice 'rock' 'paper' 'sissors'")

while player not in opt:
    print(" enter valid choice")
    exit()
print(f":{player}, {computer}")

if(player =="paper" and computer =="sisssors"or"rock"):
    print(" i win ")
elif(player == "sissors" or "rock" and computer =="paper"):
    print(" u won")
else:
    print(" tie !!!")




