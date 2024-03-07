label introduction:

    "You are a space explorer named Astrid, and you have unfortunally crashed onto a asteroid in the asteroid belt."

    "And out of all the asteroids you could have landed on, you managed to land on THE quantum asteroid."

    "The quantum asteroid famed for it's unique disregard of the time space contium, with people's personality, 
    inner narration and apperances being known to change."

    "Stumbling out of the darkness of your ship wreck, you take in your surroundings"

    scene moonbackground

    "it seems that you're in the middle of bucktown nowhere, with no immedient way off of the asteroid."

    "Explorer protocal states that crashedlanded pilots should either repair their broken ship, or get help from the locals."

    "Turning around and seeing the total destruction of your spaceship, alongside a severe lack of supplies, knocks the repair option
    of the life. Which leaves getting help as your only valid option."

    "But what is the best of to get help? Should you go searching for people to help you, or should you wait for help to arrive?"

    menu:
        "Search for help":

            "You have to find a way off this asteroid, and the best way to do that lies in getting outside help."

            "Walking away from the wreckage of your ship, you begin your search."

            jump searchForHelp
        
        "Stay at the ship":

            "Honestly why shouldn't you stay in the ship?"

            "People surely saw you ship crash onto the astraoid, and leaving the ship just means 
            forsaking their soon to be help."

            "But even as minutes turn to hours, and the hours turn to days, you start to wonder if help is truly going to arrive."

            menu:
                "search for help":

                    "If people were going to come, they would have been here by now."

                    "You decide that the only way off this asteroid is to get help, so you bid your ship goodbye and start your search."

                    jump searchForHelp
                
                "The ship leads to salvation":
                    "You and the ship have been partners for as long as you can remember, and if there's anything that can get you off this asteroid, it's
                    the ship's presence."

                    "Don't you remember when you assisted the ship with the dismantlement of the Jupiter Cartel? Or that time t "

                    "History has shown that the ship has always had a magnetic personality, and if anything is going to draw help towards you, it's the ship's
                    famous charm."

                    "Yet as the days start to roll by, you begin to wonder why the ship hasn't attrated people."

                    "It is then that you realize that the ship's charm must have been broken during the crash."

                    "With that realization in mind, you hurry off towards the wastes, looking for ship beauty supplies."

                    jump aloneEnding

label searchForHelp:
    show moonbackground
    
    "You sweep your gaze across the distance, searching every nook and cranny that you come across"

    "After one of your routine sweeping gazes, you see what seems to be a figure in the distance"

    "This figure could be your way off of this asteroid."

    "However, It doesn't seem like the figure has spotten you yet, so it would still possible to sneak away."

    "After a moment of thinking, you come to a decision"

    menu:
        "Stay away from figure":

            "You still remember that one episode of 'space murderers in space', where somebody stumbled across a lone figure in the distance."
            
            "You can't remember exactly what happened to them but, given the title of the show, it probally wasn't good."

            "Who knows what horrible fate that figure would have imposed upon you if you were spotted?"

            "You decide to wander back into the asteroid wastes, seraching for a preferablly well lit, presentable figure"

            jump aloneEnding

        "Wave the figure over":
            
            "There's no way off this asteroid without gathering help, so you wave your arms and call out to the figure"

            "This seems to have gotten the attention of the figure, as they soon start to approach"

            show neillegstrong

            "When this figure approches, there are some things that quickly become apparent."

            "The man has the strongest pair of legs that you have ever seen on any living creature, and he seems completly
            as ease without a helmet in space"

            "while you study the man, wishing that your scouter was not destroyed in the crash, the man gets close enough to talk"

            n "I'm surpised to find another soul on this desolate asteroid, but I'm always happy to find a 
            new friend."

            n "My name is Neil Legstrong, and I'm happy to make your acquaintance"

            n "What about you and I join together to find a way of this asteroid? I do have a little errand
            to run, but I'm sure it won't be much of a hassle" 

            menu:
                "Go with armstrong":
                    "There is something about Legstrong that excudes trust and confidence, and you
                    get the sense that this man won't lead to astray"

                    "You decide that you should stick with Legstrong for the time being"                

                    #Leads to landing craft repair

                "Don't go with him":
                    "Something about this man immediently sets you at ease. He seems like someone you could instintually trust."

                    "However, paradoxically, the suddenness of trust that you feel towards legstrong immmediently makes you distrust him"

                    "You start to back away from Neil Legstrong"

                    n "Ah... I suppose that means that you don't want to join up with me?"

                    menu:
                        "go with armstrong":
                            "While reluctant to go armstrong, you bregrungingly agree to join forces for the time being"
                            #Leads to landing craft repair

                        "No":
                            n "Well, I guess this is where we part ways, I wish you luck on your search."

                            "You quickly head away from legstrong, and resume your search for help."

                            jump aloneEnding

label aloneEnding:
    scene aloneending
    "Soon after your search begins, a space dust storm pops into being!"

    "Your visibility starts to steadidly decline, but you continue your search for help."

    "You begin to wander around haphazzardly, trying to make sense of where you are."

    "You quickly become lost, with your only companion being the space tumbleweeds."

    "You spend the rest of your days wandering the asteroid, hopelessly trying to find a way of this asteroid."

    "But you never find a way to escape."

    "Lost and Alone Ending"

    return
