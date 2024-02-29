# Kristina's Section - space agency or vegas arc

    # helped legstrong
    scene #fight helped legstrong

    show legstrong #mood

    n "Thank you for helping me stop the moon from exploding."
    n "You seem like a capable operative."
    n "Would you like to join my organization? We have an important mission."

    # decision structure YES/NO for joining, or "We should celebrate instead"

    # NO - celebration
        a "We should celebrate instead, have you ever been to Space Vegas?"
        n "I can't force you to join, let's celebrate the win."
        # Space Vegas Ending-----------


    # NO = first NO
        a "I'm not looking to join any organizations right now."

        n "Are you sure? We're fighting to rid the galaxy of the Pinkertons, my old employer."
        n "They need to be stopped before they are the next corporate overlords."

            # YES/NO
            # NO (second no)
                a "I'd really rather not get involved."

                n "Then let me take you out as a thank you for saving the moon. I'm quite fond of it."
                # Space Vegas Ending---------

            # YES
                a "I suppose it's a worthy cause, I'll join you."

                n "I'm glad, your skills will be invaluable"
                # Fight to overthrow their organization, (optional is legstrong actually having you fight the real rebels) \
                # and he's helping the agency, or does he overthrow the agency and take power himself, or just a freedom fighter?) \
                # Whichever it is will be in the ending dialogue
                # Join Legstrong Ending----------


    # YES = you join a rebel organization trying to overthrow space pinkertons.
        a "Thank you for agreeing to help. Our goal is to stop the Pinkerton Agency and their influence throughout space."
        a "Your skills will be quite useful to our cause."
        # Join Legstrong Ending----------
