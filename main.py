import random

number = random.randint(1,100)
guess = 0

while (guess != number):
     guess = int(input("enter your gugess "))

     if(guess > number ):
         print(" guess lower")
     elif(guess < number):
         print(" guess higher")
     else:
      print("you won")



