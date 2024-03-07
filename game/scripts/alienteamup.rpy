default plannotdiscussed = False

label alienteamup:
    scene alien-lair-scene
    show dr-zorgoloran
    z "Juan Carlos, is that you?"
    menu:
        "Yes":
            jump yourememberourplan
        "No":
            z "Oh, so who are you?"
            menu: # Feel free to add more people
                "Barack Obama":
                    z "We know of your VIP status on earth."
                    z "I'm sorry to waste your time, Mr. President. I will bring you to your house right away."
                    scene whitehouse
                    "Zygaloran returns you to your white house"
                    pause 2
                    "where you live happily ever after with Michelle..."
                    show barackandmichelle
                    pause 2
                    return
                "Niel Legstrong":
                    z "Don't try to fool me, I just killed Niel Legstrong!"
                    jump zygaloranshootsyou
#                     Unfinished ending
#                 "Astrid":
#                     z "I've never heard of you. You must be a human."
                "Juan Carlos":
                    z "Oh. You forgot your name again."
                    $ plannotdiscussed = True
                    jump forgetfuljuancarlos

label yourememberourplan:
    z "Ah, I'm glad you're back! You remember our plan, yes?"
    menu:
        "Yes":
            z "Ah, so remind me what we're doing next"
            menu:
                "Blowing up Alderaan":
                    jump forgottheplan
                "Blowing up Saturn":
                    jump forgottheplan
                "Blowing up the moon":
                    z "Oh yes, that's right. But if you were Juan Carlos, you wouldn't remember that!"
                    jump zygaloranshootsyou
        "No":
            jump forgetfuljuancarlos


label zygaloranshootsyou:
    # TODO: Animation/gif
    "Zap! you die"
    return

label forgottheplan:
    z "No, Juan Carlos, we're blowing up the moon!"
    jump forgetfuljuancarlos

#### Part 2 #####

label forgetfuljuancarlos:
    z "Ah, classic Juan Carlos, never remembers anything. Glad to have you back!"
    # TODO: move on
    if plannotdiscussed:
        z "Let us continue on our plan to blow up the moon."
    z "The plan is finally coming into fruition."
    z "Humanity has hidden earth for its cultural significance for too long!"
    z "Now that we've killed Niel Legstrong, we have the location of the sol system."
    z "Mankind won't oppress the motherland ever again!"
    z "I know you're forgetful, Juan. Tell me if you have any questions."
    jump questions

label questions:
    # TODO: Remove options after they've been selected?
    menu:
        "Why the moon?":
            z "Humanity isn't aware of this, but beneath the thick crust of the moon is a liquid fondue core."
            z "We could mine the moon, but humanity would notice it too fast, like Niel Legstrong did. That's why he needed to be eliminated"
            z "So we have to resort to blowing up the moon, and the succulent material can be gathered afterwards. "
            jump questions
        "How are we blowing up the moon??":
            z "We are using a moon-blower-up-inator, of course. Starry the Pottypuss won't stop us this time!"
            jump fightorflight
        "Let's a go!":
            jump blowupthemoon

label fightorflight:
    menu:
        "Fight":
            "You lunge at Zygaloran!"
            jump zygaloranshootsyou
        "Flight":
            "You run toward the escape hatch!"
            jump zygaloranshootsyou
        "Stay calm":
            jump questions

label blowupthemoon:
    "Zygaloran plugs in earth's coordinates into the navigation console."
    "Autopilot Engaged"
    "56,000 light years from earth"
    "30,000 light years from earth"
    "19,000\n5,000"
    "Decelerating"
    "4,000"
    "2,000"
    "900"
    "500"
    "100"
    "3"
    "2"
    "1"
    "Big flash on screen! Not anticlimactic!!! Animation of moon blowing up"
    # TODO Animation of moon blowing up
    # TODO big flahs on screen
    # TODO implement automatic countdown
    return


