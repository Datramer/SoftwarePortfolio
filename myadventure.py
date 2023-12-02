alive = True
won = False
room = 1
key1 = False
key2 = False
key3 = False
key4 = False
spear = False
torch = False
Littorch = False
flint = False
ratslain = False
spiderslain = False
keytotal = 0
instruction = "nowhere"
while alive == True and won == False:


    instruction = ""
    #room 1 the starting room
    #also the final room
    if room == 1:
        print("you are in a dimmly lit room, with no discernable light sources.\n to your south lies a wrot iron door with four key holes\n    to your north a large room apears to be foggy\n    to your east a large room which clearly branches off\n which direction would you like to go? (north/east/south)")
        instruction = input("your choice: ")
        instruction = instruction.lower()
        if instruction == "south":
            if key1 == True and key1 == True and key1 == True and key1 == True:
                #wow you won!
                won = True
                print("you slide the four keys into their respective holes, twisting them each as they enter, the door creaks open and you see the light of day again.")
            else:
                "thats very locked!"
        if instruction == "north":
            print("as you walk down the short hallway what once apeared to be fog reveals itself to be thick and fine cobwebs do you procceed (y/n)")
            instruction = input("your choice: ")
            instruction = instruction.lower()
            if instruction == "y":
                if Littorch == False:
                    print("you think to yourself technically cobwebs are abbandoned spider webs; which these are clearly not. A two meter spider pouces on you from the corner. YOU ARE DEAD")
                    alive = False
                else:
                    print("as you approach the room you lift your torch to see better, but it catches on the webs lighting them briliantly")
                    print("you hear pained screeches, and after mere moments the room blaze has run out of fuel")
                    print("you enter and all thats left is a key, you return eager to leave the chared stench behind")
                    keytotal += 1
                    print("you now have " + str(keytotal) + " keys")
                    key4 = True
                    spiderslain == True
            if instruction == "n":
                print("good choice, you hear scurrying behind you as you retreat to the first room")
        if instruction == "east":
            room = 2



    #room 2 is the large centeral room   
    elif room == 2:
        print("You are in a large room there are four branching rooms including the one you just left.(action(a)/changeroom(cr))")
        instruction = input("your choice: ")
        instruction = instruction.lower()
        if instruction == "a":
            print("you look around seeing a terminal, and some markings on the wall.(terminal(t),examine(e),search(s))")
            instruction = input("your choice: ")
            instruction = instruction.lower()
            if instruction == "t":
                print("you approach the terminal to see the following lines on the old green screen")
                while instruction != "fish" or instruction == 'q':
                    print("Alive without breath,\nAs cold as death;\nNever thirsty, ever drinking,\nAll in mail never clinking.")
                    instruction = input("your response (or q to quit): ")
                    instruction = instruction.lower()
                    if instruction == "fish":
                        print("The terminal sounds a triumphant chime and a compartment you hadnt noticed opens giving you a key")
                        keytotal += 1
                        print("you now have " + str(keytotal) + " keys")
                        key1 = True
                    elif instruction == 'q':
                        print("maybe think about it and come back later")
                    else:
                        print("that answer prompted no response from the terminal")
            elif instruction == "e":
                print("You see four numbers scrawled on the wall with a pitch like paint: a green 4 a yellow 4 a red 2 and an orange 7") 
            elif instruction == "s":
                print("your search yields nothing")
        if instruction == "cr":
            print("go to which room? (n/e/s/w)")
            instruction = input("your choice: ")
            instruction = instruction.lower()
        if instruction == "n":
            room = 3
        elif instruction == "e":
            room = 4
        elif instruction == "s":
            room = 5
        elif instruction == "w":
            room = 1


    #room 3 has the final puzzle and the torch
    elif room == 3:
        if spiderslain == True and ratslain == True:
            print("the room has changed since you last entered there is now four large rotatable wheels with numbers on them")
            print("above the wheels is the inscription follow the order of light")
        else:
            print("as you enter the room a voice says 'return when you are the only living being in this dungeon'(search(s)retreat(r))")
        instruction = input("your choice: ")
        instruction = instruction.lower()
        if instruction == "2744":
            print("a secret compartment opens giving you another key")
            key3 = True
            keytotal += 1
            print("you now have " + str(keytotal) + " keys")
            print("this room is clearly empty you leave it.")
            room = 2
        if instruction == "r":
            room = 2
        if instruction == "s":
            print("in a dark corner you find a discarded unlit torch, but nothing else, you take the torch")
            if flint == True:
                print("you pick it up and use the flint found earlier to light it")
                Littorch = True
            torch = True


    #room 4 has the spear and the flint and steel
    elif room == 4:
        print("You are in a small room with the only exit being the way you came(action(a)return(r))")
        instruction = input("your choice: ")
        instruction = instruction.lower()
        if instruction == "r":
            print("you return the way you came")
            room = 2
        if instruction == "a":
            print("you look around noticing an old statue(examine(e)/search(s))")
            instruction = input("your choice: ")
            instruction = instruction.lower()
            if instruction == "s":
                print("in the corner you find a flint and steel")
                if torch == True:
                    print("you pick it up and use it to light the torch you found earlier")
                    Littorch = True
                flint = True
            if instruction == "e":
                print("you aproach the old statue and realize that it has a spear that you can take, you now have a spear")
                spear = True


    #rat and a key
    elif room == 5:
        if spear == True:
            print("a large rat pounces you, by shear luck you lift your spear squering it as it jumps for you, you found a key")
            ratslain == True
            key2 = True
            keytotal += 1
            print("you now have " + str(keytotal) + " keys")
            print("this room is clearly empty you leave it.")

        else:
            print("OH NO! there is a giant rat already pouncing at you before you can even react, you died")
            alive = False
        room = 2
