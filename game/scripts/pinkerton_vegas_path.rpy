# QueenInk's Section - space agency or vegas arc

label legstrong_job_offer:
    ## helped legstrong stop the alien's plan, and DIDN't turn on the machine

    #scene fight helped legstrong
    #show legstrong

    n "Thank you for helping me stop the moon from exploding."
    n "You seem like a capable operative."
    n "Would you like to join my organization? We have an important mission."

    # decision structure YES/NO for joining, or "We should celebrate instead"
    menu:
        "I'll join up with you.":
            jump joined_legstrong_organization
        "I'm not looking to join any organizations right now.":
            jump join_legstrong_first_no
        "We should celebrate instead, have you ever been to Space Vegas?":
            n "I can't force you to join, let's celebrate the win."
            jump legstrong_vegas

label join_legstrong_first_no:
        n "Are you sure? We're fighting to rid the galaxy of the Pinkertons, my old employer."
        n "They need to be stopped before they are the next corporate overlords."

        menu:
            "I'd really rather not get involved.":
                n "Then let me take you out as a thank you for saving the moon. I'm quite fond of it."
                n "You'll love space Vegas."
                jump legstrong_vegas
            "I suppose it's a worthy cause, I'll join you.":
                n "I'm glad you reconsidered, your skills will be invaluable"
                jump joined_legstrong_organization

label joined_legstrong_organization:
    # YES = you join a rebel organization trying to overthrow space pinkertons.
    n "Thank you for helping stop the Pinkerton Agency and destroying their influence throughout space."
    # scene pinkerton ending
    return

label legstrong_vegas:
    n "Welcome to Space Vegas! Don't drink too much here, you never know where you'll end up."
    return
