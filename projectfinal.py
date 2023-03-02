inventory = [] #Everything looks great! Just wondering the purpose of this... did you load something in?
def start_game():
    print("")
    print("You're in a KFC, you're really thirsty. The cashier asks what you want.")
    print("\"What's up bossman, what can I get for you?\"")
    print("")
    choice = input("Will you order water, (1) Mt. Dew, (2) or nothing? (3): ")
    print("")
    if choice == "1":
        water()
    elif choice == "2":
        print("The cashier gives a nod of approval.")
        print("\"Excellent choice.\"")
        dew()
    elif choice == "3":
        nothing()
    else:
        print("*Dude, please play along.*")
        print("")
        start_game()
def water():
    print("The cashier gives you a small cup of water.")
    print("\"Will there be anything else?\"")
    inventory.append("water")
    print("What will you say?")
    print("")
    choice = input("Yes, that's all (1) or no, I need more (2): ")
    print("")
    if choice == "1":
        choice1()
    elif choice == "2":
        choice2()
    else:
        print("*Why are you like this? Pick an actual option man.*")
        print("")
        water()

def dew():
    print("They give you a cup of that green goodness.")
    inventory.append("dew")
    print("\"It's on the house.\"")
    print("You leave the KFC with your Mt. Dew.")
    print("")
    outside()
def nothing():
    print("The cashier just looks at you blankly.")
    print("\"Why are you here then? Get out.\"")
    print("You leave the KFC.")
    print("")
    outside()
def choice1():
    print("\"Then get out you little sussy rapscallion!\"")
    print("You leave the KFC.")
    print("")
    outside()
def choice2():
    print("The cashier raises an eyebrow and looks at you.")
    print("\"Well what else do you want?\"")
    print("")
    choice = input("Give me chicken (1) or give me mac and cheese. (2): ")
    print("")
    if choice == "1":
        chicken()
    elif choice == "2":
        mac()
    else:
        print("*Bruuuhhh... make an actual choice. Tell you uwhat, I'll give you another chance.*")
        print("")
        choice2()
def chicken():
    print("The cashier just stares at you slightly confused.")
    print("\"Ok then... that's an extremely vague atatement but I guess I got you.\"")
    print("The cashier gives you an 8 piece bucket of extra crsipy dark meat.")
    print("You pay and then leave the KFC.")
    print("")
    inventory.append("chicken")
    outside()
def mac():
    print("The cashier nods and gives you a container full of that yellow good stuff.")
    print("\"Enjoy the finest mac the Colonel has to offer!\"")
    print("You take the mac and leave the KFC.")
    print("")
    inventory.append("mac")
    outside()
def outside():
    print("You see an old man outside the KFC. He stops you as you walk out.")
    if "dew" in inventory:
        print("The old man notices your Mt. Dew and begins to speak.")
        print("\"It's nice to know there's still some people in the world with fine taste!\"")
        print("You say goodbye to the old man and leave.")
        print("")
        print("CONGRATULATIONS! YOU ACHIEVED THE TRUE ENDING!")
    elif "water" in inventory and "chicken" in inventory:
        print("The old man comes up to you and eyes you up.")
        print("\"Chicken and water? I'm dissapointed about the water but I suppose I can let you slide by as you have chicken.\"")
        print("The old man looks contempt with himself and lets you pass by.")
        print("You leave the man.")
        print("")
        print("YOU ACHIEVED THE NEUTRAL ENDING!")
    elif "water" in inventory and "mac" in inventory:
        print("The old man comes up to you and eyes you up. He begins to speak to you.")
        print("\"Ok, ok, ok... I don't know about the water but that Colonel mac is the GOAT! You have passed my made up test. You may leave now.\"")
        print("You leave the old man.")
        print("")
        print("YOU HAVE ACHIEVED THE OK ENDING!")
    elif "water" in inventory:
        print("The old man looks at your drink and looks dissapointed.")
        print("\"Wow... Water? Really? Not exciting at all. Shame on you random stranger who wanted a drink.\"")
        print("The old man then shoots laser beams from his eyes and you turn to ashes.")
        print("")
        print("YOU ACHIEVED THE BAD ENDING!")
    else:
        print("The old man comes up to you and notices nothing in your hands. He looks at you.")
        print("\"Nothing? You enter a KFC and leave with nothing? I know you didn't eat in so this is frankly unacceptable. You failed my made up test stranger.\"")
        print("The old man begins to levitate and you hear thunder.")
        print("You look up and see a boulder falling from the sky, before you can run away, you are crsuhed.")
        print("")
        print("YOU HAVE ACHIEVED THE WORST ENDING!")
start_game()
