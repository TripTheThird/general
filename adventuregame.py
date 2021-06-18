
print("After running out of fuel and drifting through space,\n"
      "you suddenly start to get pulled into the field of gravity\n"
      "of a nearby planet. You are frantically running around your small\n"
      "vessel as your crewmates assess the chances of survival as you plummet\n"
      "to the ground below. You start to gain more and more velocity, and due\n"
      "to the number of G’s you’re experiencing, you pass out.")
dec_1 = input("You wake up on the planet, you’re crew dead, and your arm\n"
              "bleeding heavily and quickly. It seems the air on this planet\n"
              "is breathable and has an atmosphere similar to earths, and you\n"
              "seem to be in a jungle environment. As you look around at your\n"
              "situation, you notice your ship is on fire. You look inside and\n"
              "you see two things, the MOBILE COMMUNICATOR you could use to contact\n"
              "other ships, and a MEDKIT you need to patch yourself up. The ship could\n"
              "blow any second, you only have time to run in and grab one item.\n"
              "Which one will you take? : ")

if dec_1.lower() == "mobile communicator":
    mob_com = input("You run inside the burning building, and look around\n"
                    "for the mobile communicator. You see it on the ground\n"
                    "and pick it up, just as an explosion bursts from another\n"
                    "part of the crash-landed ship. \nYou run out as quickly as\n"
                    "you can getting safely to cover, as your ship crumbles to\n"
                    "the ground, with your crew and supplies left inside.\n"
                    "As you’re busy trying to calm yourself down, you hear someone\n"
                    "patch through on the radio. “Holy crap! We saw your ship cr- *static*\n"
                    "if you can he- *static* meet us at the structure north of your\n"
                    "structure and we *static*”. Luckily your space suit has a built\n"
                    "in compass and topographical scanner of the surface, so you can\n"
                    "figure out the direction of the structure pretty easily. As you\n"
                    "start to get up to move towards the structure, you notice a sharp\n"
                    "pain in your arm. Do you choose to move towards the STRUCTURE, or\n"
                    "stay and look for something that could act as a BANDAGE or salve\n"
                    "for your wound? : ")
    
    if mob_com.lower() == "structure":
        mob_com_structure = input("After travelling for a little under thirty minutes,\n"
                                  "you come across the structure you believe they were\n"
                                  "talking about. It looks like a small, abandoned research\n"
                                  "facility, it does not seem like it’s been used in many years.\n"
                                  "It seems those you contacted through the communicator have not\n"
                                  "reached this facility yet. Do you want to WAIT OUTSIDE, EXPLORE\n"
                                  "the facility, or PATROL the surrounding area?")
        
        #death
        if mob_com_structure.lower() == "wait outside":
            print("You decide to wait outside the structure. You\n"
                  "are sitting right next to the door, the building\n"
                  "expands about 15 feet to your right and left and is\n"
                  "pretty much just a square. As you’re waiting outside,\n"
                  "you doze off. You wake up to the sound of footsteps,\n"
                  "and as you open your eyes you realize your surrounded\n"
                  "by several raptor-like creatures. They all rush you at\n"
                  "once and with no weapon to defend yourself, they start\n"
                  "to slash and bite you with their teeth and claws.\n"
                  "You quickly become a mangled pile of flesh as they feast\n"
                  "on you. YOU DIED")
                
            #This is your win condition
        elif mob_com_structure.lower() == "explore":
            mob_com_explore = input("You decide to explore the inside of the structure.\n"
                                    "As you enter the building, you look around. You see\n"
                                    "a research lab, a security office, and a break area \n"
                                    "with hallways leading to each, and stairs that you\n"
                                    "assume lead to the roof. You decide to enter the security office. \n"
                                    "You look around and you notice a large SWORD and a BAT.\n"
                                    "Which do you pick up?")
                
            if mob_com_explore.lower() == "bat":
                print("You run at the raptor creature and swing your\n"
                      "bat as hard as you can as it leaps towards you,\n"
                      "and smack it right in the head stunning it. You\n"
                      "run past it and up the stairs, just as it starts\n"
                      "to recover. You sprint up the stairs as fast as you\n"
                      "can, with it following close behind. You make it to \n"
                      "the roof and trip after bursting through the door, and\n"
                      "as you turn around you see the creature right above you, \n"
                      "about to land on you and tear you to shreds. Just before \n"
                      "it lands, a huge laser pierces through the raptor, \n"
                      "knocking it back and leaving a giant hole in its body. \n"
                      "You turn around and see some of the crew members from the \n"
                      "spaceship holding huge pulse rifles, and you run towards them. \n"
                      "“Close one! We got here just in time looks like” chortles man \n"
                      "who shot the raptor. “Thank you so much, I would’ve been raptor \n"
                      "food without you” you reply. You get onto the ship, and they \n"
                      "start back to earth so you can be at home. CONGRATULATIONS YOU WIN!")
                    
            elif mob_com_explore.lower() == "sword":
                print("You run at the raptor and try to pierce it with\n"
                      "your sword, but it bounces off with a flash of sparks.\n"
                      "The creature must have some sort of armored scales. It\n"
                      "seems unaffected and leaps at you, tearing through your\n"
                      "throat. Maybe something blunt would have been better?\n"
                      "YOU DIED.")
                    
            else:
                print("ERROR")
                    
            
        #death
        elif mob_com_structure.lower() == "patrol":
            print("You start to patrol the area around the structure.\n"
                  "After about an hour of walking around the outskirts\n"
                  "of the structure you hear a rustling in the bushes. \n"
                  "You decide to go investigate the source of the noise, \n"
                  "coming from the bushes around the edge of the clearing \n"
                  "around the structure. As you get closer, a raptor like \n"
                  "creature leaps out of the bushes and sinks its teeth \n"
                  "around your abdomen. You start kicking, and flailing in \n"
                  "pain, but as you lose more and more blood, you get weaker. \n"
                  "It ends up taking a chunk out of your body, and you lose \n"
                  "consciousness. YOU DIED.")
                
        else:
            print("ERROR")
                
    #death
    elif mob_com.lower() == "bandage":
        print("You look around your crash site and you notice a plant\n"
              "that looks a lot like aloe vera, and you decide to use \n"
              "that as a salve to hopefully clean your wound. As you \n"
              "rub it in and try to use some leaves to bandage it, you \n"
              "start to lose feeling on the right half of your body and \n"
              "fall to the ground. You quickly realize you just applied \n"
              "poison to your wound and it has coursed through your body, \n"
              "but you realized to late. You quickly lose function of your\n"
              "organs.\n YOU DIED.")
        
    else:
        print("ERROR")
               
elif dec_1.lower() == "medkit" or dec_1.lower() == "med kit":
    medkit1 = input("You run inside the burning ship and look around for\n"
                    "the med kit. You see it hanging up on the wall, and\n"
                    "quickly grab it just as an explosion bursts from another\n"
                    "part of the crash-landed ship. You run out as quickly as\n"
                    "you can getting safely to the ground, with your crew and\n"
                    "supplies left inside. As you’re busy trying to calm yourself\n"
                    "down, you notice the sharp pain in your arm growing. You take\n"
                    "some supplies out of the med kit, and clean and stitch your\n"
                    "wound. It still hurts but you are no longer losing blood.\n"
                    "You look at the device on the wrist of your suit, which shows\n"
                    "a compass and topographical map of the area. You see a STRUCTURE\n"
                    "to the north of you, and a MOUNTAIN to the south east you could\n"
                    "use to attempt to spot intelligent life on the planet. Which do\n"
                    "you want to move towards? : ")
    if medkit1.lower() == "structure":
        print("After patching yourself up, you make your way towards\n"
              "the structure north. After reaching the structure, you \n"
              "see three raptor like creatures standing at the door way \n"
              "trying to get in, and as you try to sneak away you step \n"
              "on a branch, directing their attention towards you. They\n "
              "all come at you at once, slashing and biting at your \n"
              "torso, legs, and neck. You bleed out very fast. YOU DIED")
    elif medkit1.lower() == "mountain":
        med_mountain = input("After patching yourself up, you make your way\n"
                             "towards the mountain. When you reach it, you \n"
                             "notice when you reach the top of the mountain \n"
                             "you can see nothing but forest. You know there \n"
                             "was a structure somewhere so you know intelligent\n "
                             "life exists, but there doesn’t seem to be any civilization\n"
                             "anywhere. There is a lot of good firewood nearby and a cave \n"
                             "with flint and steel in it nearby. Do you want to SHOUT hoping\n "
                             "somebody nearby hears you, or make a signal FIRE hoping somebody\n" 
                             "from below sees it? : ")
        if med_mountain.lower() == "shout":
            print("After shouting, you wait for a few minutes. You\n"
                  "hear some footsteps from behind, and you see a \n"
                  "mountain lion. You try to run away, but you trip \n"
                  "on the rocky mountain, and it makes you its dinner \n"
                  "this evening. YOU DIED")
        elif med_mountain.lower() == "fire":
            med_fire = input("You grab wood and the flint and steel and\n"
                             "make a signal fire. You bide your time by \n"
                             "upkeeping the fire and collecting more wood. \n"
                             "As you’re sitting by the fire hoping someone \n"
                             "will come soon, you hear footsteps behind you. \n"
                             "You see a mountain lion standing there. Do you \n"
                             "want to RUN away, or grab a piece of wood and use \n"
                             "it as a TORCH against the mountain lion? : ")
            if med_fire.lower() == "run":
                print("You try to run away, but you trip on the rocky\n"
                      "mountain, and the mountain lion makes you its dinner\n"
                      "this evening. YOU DIED")
            elif med_fire.lower() == "torch":
                print("You grab a stick and light it on fire, using it\n"
                      "as a torch. The mountain lion runs at you but as \n"
                      "you wave the torch at it, it stops in it’s tracks \n"
                      "and starts to back away, until you see it turn and \n"
                      "run back into the forest. You breathe a sigh of relief, \n"
                      "just as you hear more footsteps. Panicking you ready your \n"
                      "torch again, just to see it seems to be some of this planets \n"
                      "inhabitants. “What are you doing out here? This forest is dangerous.”\n"
                      "One of them says. You explain the situation, and they take you back to \n"
                      "they’re city, and you can gather the resources to get back to your home \n"
                      "planet. CONGRATULATIONS YOU WIN!")               
        else:
            print("ERROR")
    else:
        print("ERROR")
else:
    print("ERROR")
       