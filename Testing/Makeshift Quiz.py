correct = 0

location = input("In which city is Overlake located?\n")
if location.lower() == "redmond":
    print("Correct!\n")
    correct+=1
else:
    print("I'm guessing your mom must drive you to school?\n")

states = int(input("How many states are there in the U.S?\n"))
if states == 50:
    print("Correct!\n")
    correct+=1
else:
    print("Wrong! You should've counted the number of stars on the flag!\n")

name = input("What is my name?\n")
if name.lower() == "ashley":
    print("Glad you know me!\n")
    correct+=1
else:
    print("Wow...My feelings are a bit hurt :(\n")

language = input("What coding language are we learning in this class?\n")
if language.lower() == "python":
    print("You've been paying attention in class!\n")
    correct+=1
else:
    print("Incorrect...What have you been doing all of this time?\n")

question = input("How many questions have I asked so far (including this one)?\n")
if question == "5":
    print("Nice! You're finished!")
    correct+=1
    print("You've gotten", correct, "correct.")
else:
    print("Wrong. You've gotten", correct, "correct.")