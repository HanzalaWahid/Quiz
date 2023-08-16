print("Welcome to my computer Quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets Play :)")
score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer = input("What does GPS stand for? ")
if answer.lower() == "global positioning system":
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer = input("How many types of memory are? ")
if answer.lower() == "two":
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " question correct")
print("You got " + str((score / 4) * 100) + " %")
