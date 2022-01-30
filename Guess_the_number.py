import random
r = int(input("Enter Number Range: "))
n = random.randint(1,r)
guesses = 9
g = 1
print("You have ", guesses, " guesses")
while(guesses>0):
    print("Enter your ",g," guess here: ", end="")
    q = int(input())
    if(q == n):
        print("Bravo you have gussed correct that is ",n,"in just ", g, "gusses")
        break
    elif(q != n):
        if(q>n):
            print("The number is smaller than your guess")
        else:
            print("The number is greater than your guess")
    g = g+1
    guesses = guesses - 1
    if(guesses == 0):
        print("You are out of gusses")
        print("Game over")
    else:
        continue