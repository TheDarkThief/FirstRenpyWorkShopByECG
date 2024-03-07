#Caeden's section - Introduction area/setup
label intro:

    "You are a space explorer named Astrid, a brave astronaut epxloring the galaxy for adventure!"
    
    "Unfortunatly, your brave exploring has to be put on hold, as you seen to have crashed onto a asteroid."

    "And out of all the asteroids you could have crashed onto, you managed to land on THE quantum asteroid."

    "The quantum asteroid is famed throughout the galaxy for it's unique disregard of the time space contium."
    
    "Reports have stated that people who landed on this asteroid have had their personality, 
    inner narration, and apperances changed."

    'You figure that this phenomonon surely will surely have no impact on you whatsoever.'

    "Right?"

    "A intense need to leave your crashed vessel fills your body, so you start looking around for the emergency escape exit."

    "After a period of frantic scrambling, you stumble out of the darkness of your ship wreck, taking in your surroundings."

    scene moon-background

    "it seems that you're in the middle of bucktown nowhere, with no immediently convinent way off of this asteroid."

    "Explorer protocal clearly states that crashedlanded pilots should either repair their broken ship, or get help from the locals."

    "Turning around and seeing the total destruction of your spaceship, alongside a severe lack of supplies, seems to knock the repair option
    off the list."
    
    "Which leaves getting help as your only true, valid option."

    "But what is the best way to get help?"

    "Should you go searching for people, hoping to find someone who could provide you with supplies and information?"

    "Or should you stay put at your ship, in the hopes that the bright, burning flare that is your ship attracts help."

    menu:
        "Search for help":

            "You have to find a way off this asteroid, and the best way to do that lies in getting outside help."

            "Walking away from the wreckage of your ship, you begin your search."

            jump searchForHelp
        
        "Stay at the ship":

            "Honestly why shouldn't you stay in the ship?"

            "People surely saw you ship crash onto the astraoid, and leaving the ship just means 
            forsaking their soon to be help."

            "But as the hours tick by, you start to wonder if help is truly going to arrive."

            "Maybe you should leave the ship to find help?"

            "The ship is a kind soul, it will understand."

            menu:
                "Search for help":

                    "It's been several hours and there is still no sign of help."

                    "If people were going to come, they surely would have come by now."

                    "You decide that the only way off this asteroid is to get help, so you bid your ship a tearful goodbye and walk off to start your search."

                    jump searchForHelp
                
                "The ship leads to salvation":

                    "You and the ship have been partners for as long as you can remember, and if there's anything that can get you off this asteroid, it's
                    the ship's presence."

                    "Don't you remember when you assisted the ship with the dismantlement of the Jupiter Cartel? Or that time that the ship started a revolution against
                    the tyrannical King Louis XXVI?"

                    "History has shown that the ship has always had a magnetic personality, and if anything is going to draw help towards you, it's the ship's
                    famous charm."

                    "Yet as the days start to roll by, you begin to wonder why the ship hasn't attrated people."

                    "It is then that you realize that the ship's charm must have been broken during the crash."

                    "With that realization in mind, you hurry off towards the wastes, looking for ship beauty supplies."

                    jump aloneEnding

label searchForHelp:
    scene moon-background
    
    "You sweep your gaze across the distance, searching every nook and cranny that you come across."

    "After one of your routine sweeping gazes, you see what appears to be a figure in the distance."

    "This figure could be your way off of this asteroid."

    "However, It doesn't seem like the figure has spotten you yet, so it would still possible to sneak away."

    "After a moment of thinking, you come to a decision."

    menu:
        "Stay away from figure":

            "You still remember that one episode of 'space murderers in space', where somebody stumbled across a lone figure in the distance."
            
            "You can't remember exactly what happened to them but, given the title of the show, it probally wasn't good."

            "Who knows what horrible fate that figure would have imposed upon you if you were spotted?"

            "You decide to wander back into the asteroid wastes, seraching for a preferablly well lit, presentable figure"

            jump aloneEnding

        "Wave the figure over":
            
            "There's no way off this asteroid without gathering help, so you wave your arms and call out to the figure."

            "This seems to have gotten the attention of the figure, as they soon start to approach."

            show neil-legstrong

            "When this figure approches, there are some things that quickly become apparent."

            "The man has the strongest pair of legs that you have ever seen on any living creature, and he seems completly
            as ease without a helmet in space."

            "You suddenly wish that you grabbed your scouter before leaving the ship. The man's power level must be at least
            9000."

            "During the time that you spent pondering the man's power level, the man seems to have gotten close enough to talk to you."

            n "I'm surpised to find another soul on this desolate asteroid, but I'm always happy to find a 
            new friend."

            n "My name is Neil Legstrong, and I'm happy to make your acquaintance."

            n "What about you and I join together to find a way of this asteroid? I do have a little errand
            to run, but I'm sure it won't be much of a hassle." 

            menu:
                "Go with armstrong":

                    "There is something about Legstrong that excudes trust and confidence."
                    
                    "You are given the sense that this man would never lead to astray."

                    "With these thoughts in the back of your head, you decide that you should stick with Legstrong for the time being."                

                    jump goWithArmstrong

                "Don't go with him":

                    "Something about this man immediently sets you at ease. He seems like someone you could instintually trust."

                    "However, paradoxically, the suddenness of trust that you feel towards legstrong immmediently makes you distrust him"

                    "You start to back away from Neil Legstrong."

                    n "Ah... I suppose that means that you don't want to join up with me?"

                    menu:
                        "Go with armstrong":
                            "While reluctant to go armstrong, you bregrungingly agree to join forces for the time being."

                            jump goWithArmstrong

                        "No":
                            n "Well, I guess this is where we part ways, I wish you luck on your search."

                            hide neil-legstrong

                            "You start to walk away from armstrong, resuming your search for an another source of help"

                            "Maybe this time you'll find someone a little less trustworthy."


                            jump aloneEnding

label aloneEnding:
    scene alone-ending
    "Soon after your search begins, a space dust storm pops into being!"

    "Your visibility starts to steadidly decline, but you continue your search for help."

    "You begin to wander around haphazzardly, trying to make sense of where you are."

    "You quickly become lost, with your only companion being the space tumbleweeds."

    "You spend the rest of your days wandering the asteroid, hopelessly trying to find a way of this asteroid."

    "But you never find a way to escape."

    "Lost and Alone Ending"

    return

label goWithArmstrong:
    scene moonbackground

    "You and armstrong wander into the wastes, and with legstrong's guidance, find a wrecked toyota brand landing craft"

    scene landingcraftbackground
    
    "Armstrong is a master mechanic! He quickly repairs the the landing craft, and you guys continue on your merry way!"

    "You and armstrong speed past your surroundings, going towards the errand that Armstrong wants to carry out"

    "You confront the alien"

    menu:
        "Join the Alien":

            "The Alien made a pretty convincing argument"

            "Why shouldn't the moon be blown up?"

            "Aside from being solely responsible for the earth's waves, what has the moon done for humanity?"

            "You and the alien quickly beat up legstrong, and legstrong is quickly defeated"

            jump alienteamup
        "Join Armstrong":

            "You and legstrong have been through so much together."

            "Even if you only met the man a half hour ago, the bond that you have formed in that time is unbreakable."

            "You and armstrong easily beat up the alien with your combined might."

            jump helpingLegstrong
