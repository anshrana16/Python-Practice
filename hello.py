import random
x=random.randint(1,100)
attempts=0
while (True):
    num=int(input("Enter any random number between 1 to 100:"))
    attempts=attempts+1
    if x>num:
        print("Target no. is so high")
    elif x<num:
        print("Target no. is so low")
    elif x==num:
        print("CONGRATULATIONS!!!, You guessed the correct no. in",attempts,"th attempt")
        break
