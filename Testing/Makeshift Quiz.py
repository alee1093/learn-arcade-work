correct = 0


username = input("What is your name?\n")
print("Nice to meet you,", str(username.capitalize()) + "!")


know = input("Do I know you? You seem familiar. Well, you know me right?\n")
if know.lower() == "yes":
    print("Great! Let's see just how well you know me then.\n")
elif know.lower() == "no":
    print("Well, you're in trouble then. I'm about to test you on just that!\n")
else:
    print("That's not yes or no!")


location = input("As you SHOULD know, I go to the Overlake School. In which city is Overlake located?\n")
if location.lower() == "redmond":
    print("Correct!\n")
    correct += 1
else:
    print("How do you get to campus? I'm guessing your mom must drive you to school.\n")


states = int(input("I live in the United States. How many states are there in the U.S?\n"))
if states == 50:
    print("Correct!\n")
    correct += 1
else:
    print("Wrong! You should've counted the number of stars on the flag!\n")


name = input("This is an obvious one! What is my name?\n")
if name.lower() == "ashley":
    if name.lower() == username.lower():
        print("Wow, we have the same name huh?")
    print("Glad you know me!\n")
    correct += 1
else:
    print("Wow...My feelings are a bit hurt :(\n")


language = input("You have to know this, right " + str(name.capitalize()) + "?" + " Which coding language are we learning in this class?\n")
if language.lower() == "python":
    print("You've been paying attention in class!\n")
    correct += 1
else:
    print("Incorrect...What have you been doing all of this time?\n")


question = input("Ok, you definitely have to get this one! How many questions have I asked so far (including this one)?\n")
if question == "7":
    print("Nice! You're finished!")
    correct += 1
    percent = (correct / 5) * 100
    print("You've gotten", str(percent) + "%", "correct.")
else:
    percent = (correct / 5) * 100
    print("Wrong. You've gotten", str(percent) + "%", "correct.")