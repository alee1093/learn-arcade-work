# import library
import random


def main():
    """main code --> runs game"""
    guards_distance = 20  # records player's distance from gummy guards
    miles_traveled = 0  # records player's total distance traveled
    thirst_level = 0  # record player's thirst levels
    worms_tiredness = 0  # records gummy worm's exhaustion
    koolaid_drinks = 3  # records how many drinks there are in the canteen

    # introduction
    print("> Hey, you're awake!")
    print("> Oops, no time to talk! You're in a bit of a crisis at the moment...")
    print("> What...? You don't remember what you're doing??? Did you hit your head that hard?")
    print("> Fine, I'll explain, but quickly!")
    print("\nPrompt:\nYou've stolen candy from the Gummy Bear Kingdom's imperial treasury!")
    print("Run from the gummy guards in pursuit of you and make sure not to get caught!\n")
    print("> I suppose you did fall pretty badly while tripping over that giant gummy worm...")
    print("> But it did allow us to ride it as compensation, so it's a win!")
    ready = input("> Well, is your mind finally back from the clouds? Yes or no?\n>> ")
    if ready.lower() == "yes":
        print("\n> That's great because you're in trouble now!")
        print("\n----------------------------------------------------------------------------------------------\n")
    else:
        print("> Well, that's too bad because you'd better start running!")
        print("----------------------------------------------------------------------------------------------\n")

    # listing choices
    done = False
    while not done:
        print("Choose from the following:\n")
        print("A. Drink from your Kool-Aid supply")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit")

        # asking user for choice
        choice = input("\nWhat is your choice?\n>>")

        # quitting
        if choice.upper() == "Q":
            confirmation = input("\nAre you sure you'd like to quit?\n>>")
            if confirmation.lower() == "yes":
                print("\n> Aw, that's a shame :(")
                done = True

        # status check
        elif choice.upper() == "E":
            print("\nStatus:")
            print("You have traveled", miles_traveled, "miles.")
            print("You have", koolaid_drinks, "Kool Aid drinks left.")
            print("The guards are", guards_distance, "miles behind you.")
            print("\n----------------------------------------------------------------------------------------------\n")

        # stop for the night
        elif choice.upper() == "D":
            print("\nYou stop to take a rest for the night, deciding that you are far enough ahead of your pursuers.")
            print("\n> This licorice tree looks good to sleep under.\n")
            worms_tiredness = 0
            print("Your gummy worm is happy and got his beauty sleep.")
            guards_distance -= random.randrange(10, 21)  # moving guards up 10 to 12 miles
            print("The guards have gained on you and are now", guards_distance, "miles away.")
            print("\n----------------------------------------------------------------------------------------------\n")

        # ahead full speed
        elif choice.upper() == "C":
            speed_forward = random.randrange(10, 21)  # deciding miles travelled at full speed (10 to 21)
            miles_traveled += speed_forward  # adding to total miles
            guards_distance += speed_forward  # adding to player's distance from guards
            speed_guards = random.randrange(7, 15)  # deciding miles travelled by guards (7 to 15)
            guards_distance -= speed_guards  # moving guards up
            print("\nYou dig your heels into your gummy worm's sides, prompting him to travel", speed_forward, "miles")
            print("in a speedy manner.")
            print("\n> Hey! He's not a horse :(\n")
            thirst_level += 1
            print("Your thirst level is now", str(thirst_level) + ".")
            print("\n> Be careful, his thirst for water may become a thirst for blood...\n")
            worms_tiredness += random.randrange(1, 4)
            print("Your gummy worm's exhaustion level is now", str(worms_tiredness) + ".")
            print("\n> Yeah, he's tired! Tired of your abuse.\n")
            print("Meanwhile, the gummy guards travel", speed_guards, "miles.")
            if speed_forward < speed_guards:
                print("Despite your cruelty, it looks like the gummy guards have out sped your speed.")
            print("The guards are now", guards_distance, "miles behind you.")
            print("\n----------------------------------------------------------------------------------------------\n")

        # ahead at moderate speed
        elif choice.upper() == "B":
            moderate_forward = random.randrange(5, 12)  # deciding miles travelled at moderate speed (5, 12)
            miles_traveled += moderate_forward  # adding to total miles
            guards_distance += moderate_forward  # adding to player's distance from guards
            speed_guards = random.randrange(7, 15)  # deciding miles travelled by guards (7 to 15)
            guards_distance -= speed_guards  # moving guards up
            print("\nYou proceed at moderate speed and travel", moderate_forward, "miles.")
            thirst_level += 1
            print("Your thirst level increases by 1.")
            worms_tiredness += 1
            print("Your gummy worm grows more exhausted. His exhaustion level is now", str(worms_tiredness) + ".")
            print("Meanwhile, the gummy guards travel", speed_guards, "miles.")
            if moderate_forward < speed_guards:
                print("Unfortunately, the guards travelled at full speed and have advanced on you.")
            print("The gummy guards are now", guards_distance, "miles behind you.")
            print("\n----------------------------------------------------------------------------------------------\n")

        # drink from Kool Aid supply
        elif choice.upper() == "A":
            if koolaid_drinks > 0:
                koolaid_drinks -= 1
                print("\nYou feel your throat drying, so you take a gulp of Kool Aid.")
                print("You now have", koolaid_drinks, "Kool Aid drinks left.")
                thirst_level = 0
                print("Your thirst level is now 0.")
                print("\n> I wish you were as considerate to the gummy worm as you are to your own body...\n")
            else:
                print("\nYou have no more drinks left.")
            print("\n----------------------------------------------------------------------------------------------\n")

        # worm warnings
        if worms_tiredness > 8:
            print("Your gummy worm stops in his tracks.")
            print("\n> That's strange... He usually never pauses like this. Hey, Tim, you okay?\n")
            print("You slide down from Tim's back and kneel down. Tim looks at you with his nonexistent eyes")
            print("for a few moments.")
            print("Tim closes his eyes and his head drops. Your friend has died from overexertion.")
            print("\n> NOOOOO! WHAT HAVE YOU DONE TO TIM???\n")
            print("There is no time to grieve.")
            print("Without a proper method of travel, the gummy guards catch up to you in no time.")
            print("They notice their gummy citizen lying lifelessly next to the stolen candy and")
            print("are determined to make you pay. You are thrown into the Gummy Bear Kingdom's prison for eternity.")
            print("\n> Justice for Tim :D")
            done = True
            break
        elif worms_tiredness > 5:
            print("Warning: Your gummy worm is getting tired.")
            print("\n> See! You should treat him better, the poor thing :C\n")

        # thirst warnings
        if thirst_level > 6:
            print("Your mouth has been sandy for days, and you can feel your taste buds scraping against the roof of")
            print("your mouth like bristles. Suddenly, you fall from your gummy worm's back and your vision blurs.")
            print("You can't reach the Kool Aid, much less lift a finger. Everything goes black.")
            print("You died of thirst!")
            print("\n> Mm, maybe pay more attention to your hydration next time :D")
            done = True
            break
        elif thirst_level > 4:
            print("Warning: You are thirsty.")
            print("\n> What are you doing? Drink something!\n")

        # guards warnings
        if guards_distance <= 0:
            print("It seems that the gummy guards have caught up. They surround you and frighten your gummy worm,")
            print("throwing you off and leaving you defenseless. You are thrown into the Gummy Kingdom's jail.")
            print("Game over.")
            print("\n> Better luck next time :P")
            done = True
            break
        elif guards_distance < 15:
            print("Warning: The gummy guards are getting close!")
            print("\nUh oh! Go faster please!\n")

        # victory notifications
        if miles_traveled >= 200:
            print("You have travelled far out of the gummy guards' reach into the Peppermint Kingdom. You won!")
            print("> Woah, I didn't actually think you could do it.")

        # Kool Aid pond chance
        if choice.upper() == "B" or choice.upper() == "C":
            if random.randrange(1, 21) == 0:
                koolaid_drinks = 3
                thirst_level = 0
                worms_tiredness = 0
                print("You have found a Kool Aid pond!")
                print("You refill your Kool Aid supply, quench your thirst, and allow your gummy worm to rest.")
                print("> Jackpot!")


main()
