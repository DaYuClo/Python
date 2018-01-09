import random

print("Here", end=" ")
print("it is...")

print("Henry \'The Great\' the \"Hair Stylist\"")

print("My name is Xing three times\n" * 3)

print("107/4=",107/4)
print("107//4=",107//4)
print("107%4=",107%4)
print("\n")

name = "Xing"
print(name)
print("Hi", name)

name=input("What is your name?: ")
print("Hi", name)


FFX="The best PS2 game ever"

print("\nOriginal quote:")
print(FFX)

print("\nIn Uppercase:")
print(FFX.upper())

print("\nIn Lowercase:")
print(FFX.lower())

print("\nAs a Title:")
print(FFX.title())

print("\nWith a replacement:")
print(FFX.replace("PS2", "Playstation 2"))

# int, float, str=str(10)='10'

GTR = int(input("GTR Cost: "))
Cayenne_Turbo_S = int(input("Cayenne Turbo S Cost: "))
Ferrari_458_Spider = int(input("Ferrari 458 Spider Cost: "))
total=GTR+Cayenne_Turbo_S+Ferrari_458_Spider
print("Total:$",total)
print("\n")
#generate random numbers from 1-9
#method 1 using randint
#method 2 using randrange
#method 1 and method 2 both do the same job, so just pick 1 or both
die1=random.randint(1,9)
die2=random.randrange(10)
total_die=die1+die2
print("Dice One rolled",die1,"\tDice Two rolled",die2,"\tfor total of",total_die)

print("\n")
print("Guess the password")
pw=input("Enter the password:")
if pw == "password":
    print("Access Granted")
elif pw == "please":
    print("Ok, I will be nice today: Access Granted")
else:
    print("Try again")
    
print("\n")

print("Guess the password v2.0")
pw=""
while pw != "pws":
    pw=input("Enter the password:")
print("Access Granted")
print("\n")

#Hero vs Trolls
health=10
trolls=0
damage=3

while health > 0:
    trolls += 1
    health -= damage
    print("Your hero takes", damage, "damges")
    print("Your hero defeated", trolls,"trolls")


#corrupted host
print("\n")
money=float(input("How many dollars do you slip the host?"))
if money>0.01:
    print("This way")
else:
    print("Please wait")


#counting numbers
print("\nPrint numbers from 1-10 but skipping 5 and 9")
count=0
while True:
    count+=1
    if count>10:
        break
    if count==5:
        continue
    if count==9:
        continue
    print(count)

#login into the computer-case sensitive
print("\n")

security = 0
username=""
while not username:
    username=input("Username:")
pw=""
while not pw:
    pw=input("Password:")

if username=="Xing" and pw=="Shi":
    print("Welcome Sreca")
    security=99
elif username=="Juan" and pw=="Mendez":
    print("Welcome Panda")
    security=39
elif username=="Guest" or username=="guest" or username=="GUEST" or pw=="Guest":
    print("Welcome to the network")
    security=1
else:
    print("Login failed")

#Guess The Number
print("\n")
correct_num=random.randint(85,95)
guess=int(input("Take a guess:"))
tries=1
while guess != correct_num:
          if guess > correct_num:
              print("Lower...")
          else:
              print("Higher...")

          guess=int(input("Take a guess:"))
          tries+=1
print("Congrat.  The number was", correct_num)
print("Only took",tries,"tries")

#Demonstrates the for loop with a string
print("")
word=input("Enter a word:")
for letter in word:
    print(letter)


#Demonstrates the range() function
print("")

print("Counting: ")
for i in range(10):
    print(i,end=" ")

print("\n")
for i in range(0,50,5):
    print(i,end=" ")

print("\n")
for i in range(10,0,-1):
    print(i,end=" ")



#Demonstrate the len() function and the in operator
print("\n")

message=input("Enter a message: ")
print("The length of your message is:", len(message))
if "e" in message:
    print("Letter E is in your message")
else:
    print("Letter E is not in your message")
    

#No Vowels
print("\n")
message = input("Enter a message: ")
new_message=""
VOWELS="aeiou"
print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("A new string has been created: ", new_message)


#Demonstrates string indexing
#start = None == start = 0
print("\n")
word="pizza"

print(
"""
0   1   2   3   4   5
+---+---+---+---+---+
| p | i | z | z | a |
+---+---+---+---+---+
-5 -4  -3  -2  -1  
"""
)

print("Enter beginning and ending index: ")
start = None
while start !="":
    start=(input("\nStart: "))

    if start:
        start=int(start)
        finish=int(input("Finish: "))

        print("word[",start, ":", finish, "] is", end=" ")
        print(word[start:finish])


#Demonstrates list methods
print("\n")
scores=[]
choice=None
while choice != "0":
    print(
    """
    0 -  Exit
    1 - Show Scores
    2 - Add a Score
    3 - Delete a Score
    4 - Sort Scores From Highest to Lowest
    5 - Sort Scores From Lowest to Highest
    """
    )

    choice = input("Choice: ")
    print()

    if choice == "0":
        print("Good-bye")
    elif choice == "1":
        for score in scores:
            print(score)
    elif choice == "2":
        score=int(input("What socre did you got?: "))
        scores.append(score)
    elif choice == "3":
        score=int(input("Remove which score?: "))
        if score in scores:
            scores.remove(score)
        else:
            print(score, "isn't in the list")
    elif choice == "4":
        scores.sort(reverse=True)
    elif choice == "5":
        scores.sort()


#Tic-Tac-Toe
print("\n")
print(
"""
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
"""
)

    
input("\nEnter any key to exit...")
