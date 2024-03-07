﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
    jump intro
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    n "Niel I'm niel legstrong"

    s "I'm shák-sper"

    z "I'm alien and I'm here to kill Niel Legstrong"
#     python:
#         for i in range(1, 100):
#             message
#     e "You've created a new Ren'Py game."
#
#     e "Once you add a story, pictures, and music, you can release it to the world!"




    # This ends the game.

    return
