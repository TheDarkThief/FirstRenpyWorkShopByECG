#Lyra's Section - help legstrong -> stop aliens plan -> turn on machine anyways
label helpingLegstrong:
     show neillegstrong

     n "Thanks for helping me, every battle should be fought with a soldier like you."
     n "Now that I'm healed, thanks to you, I want YOU to join me in the journey to stopping the alies from blowing up the moon."
     n "They must be stopped, and with you on my side, we sure can. What do you say?"
    #  menu:
        # "No":
        #     n "No?! What you mean we're a dream team. The bad guys must be stopped and you're THE person for that"

<<<<<<< HEAD
        # "Yes":
        #     n "You're a win, lets beat them sarge. For the world it is!"
        #     n "Now, you can either join me on my space agency, or turn on the machine"
        #     menu:
        #         "Join Legstrong":
        #         n "Wonderful! "
=======
     menu:
        "No":
            n "No?! What you mean we're a dream team. The bad guys must be stopped and you're THE person for that. \
            You have NO choice but to join me."
            jump stop_alien

        "Yes":
            n "You're a win, lets beat them sarge. For the world it is!"
            n "Now, you can either join me on my space agency, or turn on the machine"
            menu:
                "Join Legstrong":
                    n "Wonderful! Lets go"
                    jump stop_alien
                "Turn on the machine":
                    jump machine_on

label stop_alien:
    show legstrong
    n "I'm so happy you helped me stop the alien. You're a real one."
    jump legstrong_job_offer

label machine_on:
   show legstrong
   n "You turned on the machine anyways. Hm. You're an interesting person"
   jump blowup_moon.
>>>>>>> ad79b59e9e870a3535e415f8c770f61c637dbb43

