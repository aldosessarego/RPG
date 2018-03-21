import sys

print "                          -Instructions-\n    This is a text based RPG. In order to play, you only need to read the options and type the letter that corresponds to the choice you wish to make just as it is (uncapitalized).  However, on certain occasions, you'll be asked to type. Simply write the answer then press enter. Enjoy the game."


def main():
    print "\n             -Welcome to [Insert Title Here]-"
    print "a) New Game\nb) Load Game\nc) Options\nd) Exit"
    Answer = raw_input(">>")
    if Answer == "a":
        characterSelection()
    elif Answer == "b":
        Loads()
    elif Answer == "c":
        Options()
    elif Answer == "d":
        print "Okay, bye!"
        sys.exit
    elif Answer == "A" or Answer == "B" or Answer == "C" or Answer == "D":
        print "What did I say about capitalizing the choices? It's a No-No. Lowercase, okay? Good. Let's try that again."
        main()
    else:
        print "Ummm what? Only four options here... dont try anything funny."
        main()

def Loads():
    print ("this loads the game")
    main()

def inventory():
    print "This will show you your items, weapons and potions"

def Party():
    print "this will show you your party memebers"


def Options():
    print "It's a text based game... what did you expect to find here? Audio, Video and control options? Nah, keep playing."
    main()


def standby():
    print("\na) Attack \nb) Items \nc) Party")
    Answer = raw_input(">>")
    if Answer == "a":
        attack()
    elif Answer == "b":
        inventory()
    elif Answer == "c":
        Party()
    else:
        print "Please write one of the choices provided uncapitalized."
        standby()


def tutorial():
    print("\n [" + str(
        PlayerName) + " faces a small Ogre! (lv.1) ] \n\nYou see? This here is one of the many monster you'll encounter along your journey and it'll be my duty to teach you how to survive an attack.")
    global Ogre
    Ogre = Enemies()
    Ogre.Elevel = int(1)
    Ogre.EHealth = int(50 + (15 * Ogre.Elevel))
    Ogre.ESpeed = int(6)
    Ogre.EAttack = int(10 + (5 * Ogre.Elevel))
    standby()


class Enemies:
    global Elevel
    global EHealth
    global ESpeed
    global EAttack


def attack():
    print("Which attack will you use?")
    att = raw_input(">>")
    damage = int(attacks[att] * PlayerAttack)
    print ("\n[" + str(PlayerName) + " deals " + str(damage) + " damage]")
    Ogre.EHealth = (Ogre.EHealth-damage)
    if Ogre.EHealth>0:
      print ("[" + str(Ogre.EHealth) + " Hp left]")
      standby()
    else:
        print "[Enemies defeated.]"


def characterSelection():
    global PlayerName
    PlayerName = raw_input("\nWhat's is your name?\n>>")
    print("\nYou said your name was " + str(PlayerName) + "?\na)Yes\nb)No")
    Answer = raw_input(">>")
    if Answer == "a":
        print"Good."
    elif Answer == "b":
        print"Okay. Let's try that again."
        characterSelection()
    else:
        print"Someone didn'really pay attention to the Instructions. Let's try that again."
        characterSelection()

    def classselection():
        global PlayerClass
        global PlayerHealth
        global MaxHealth
        global PlayerAttack
        global PlayerSpeed
        global attacks
        print"\nOkay. So, which are you?\na) Witch\nb) Vampire\nc) Hunter"
        Answer = raw_input(">>")
        if Answer == "a":
            PlayerClass = "Witches"
            MaxHealth = int(150)
            PlayerHealth = int(150)
            PlayerAttack = int(15)
            PlayerSpeed = int(4)
            attacks = {'Fireball': 1}

        elif Answer == "b":
            PlayerClass = "Vampires"
            MaxHealth = int(100)
            PlayerHealth = int(100)
            PlayerAttack = int(25)
            PlayerSpeed = int(12)
            attacks = {'Scratch': 1}
        elif Answer == "c":
            PlayerClass = "Hunters"
            MaxHealth = int(125)
            PlayerHealth = int(125)
            PlayerAttack = int(20)
            PlayerSpeed = int(8)
            attacks = {'Regular Arrow': 1}
        else:
            print"Try again.\n"
            classselection()

    classselection()
    print "\n[You can now use " + str(
        attacks.keys()) + "] \n\nOh Good. Then you're one of ours. You don't have to worry about anything here. " + str(
        PlayerClass) + " look after each other. Still, I'm going to have to train you to fight. There's a war out there, as soon as you walk out of those doors, you'll be caught in the crossfire."
    global PlayerLevel
    global Playerxp
    global LevelUp
    PlayerLevel = int(1)
    Playerxp = int(0)
    LevelUp = (PlayerLevel ** 2)
    if Playerxp >= LevelUp:
        PlayerLevel += 1
        PlayerHealth += 5
        MaxHealth += 5
        PlayerAttack += 2
        print "Congratulations! You're now level " + int(PlayerLevel) + "!"
    tutorial()


main()

