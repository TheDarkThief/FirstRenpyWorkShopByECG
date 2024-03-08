# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")

# The game starts here.
image moon-exploding1 = Image("images/moonexploding/moon-exploding1.png")
image moon-exploding2 = Image("images/moonexploding/moon-exploding2.png")
image moon-exploding3 = Image("images/moonexploding/moon-exploding3.png")
image moon-exploding7 = Image("images/moonexploding/moon-exploding7.png")
image moon-exploding6 = Image("images/moonexploding/moon-exploding6.png")
image moon-exploding4 = Image("images/moonexploding/moon-exploding4.png")
image moon-exploding5 = Image("images/moonexploding/moon-exploding5.png")
image moon-exploding11 = Image("images/moonexploding/moon-exploding11.png")
image moon-exploding10 = Image("images/moonexploding/moon-exploding10.png")
image moon-exploding8 = Image("images/moonexploding/moon-exploding8.png")
image moon-exploding9 = Image("images/moonexploding/moon-exploding9.png")
image moon-explosion-ending = Image("images/scenes/moon-explosion-ending.png")
image moon-background = Image("images/scenes/moon-background.png")
image alien-lair-scene = Image("images/scenes/alien-lair-scene.png")
image alone-ending = Image("images/scenes/alone-ending.png")
image landingcraft-background = Image("images/scenes/landingcraft-background.png")
image self-destruction-ending = Image("images/scenes/self-destruction-ending.png")
image whitehouse = Image("images/scenes/WhiteHouse.png")
image happy-vegas-ending = Image("images/scenes/happy-vegas-ending.png")
image alone-vegas-ending = Image("images/scenes/alone-vegas-ending.png")
image join-legstrong-ending = Image("images/scenes/join-legstrong-ending.png")
image moonbackground = Image("images/scenes/moonbackground.png") 
image astronaut = Image("images/characters/Astronaut.png")
image zygloran = Image("images/characters/Zygloran.png")
image barackandmichelle = Image("images/characters/BarackAndMichelle.png")
image shake-spar = Image("images/characters/shake-spar.png")
image neil-legstrong = Image("images/characters/neil-legstrong.png")
image dr-zorgoloran = Image("images/characters/dr-zorgoloran.png")

label start:
    jump intro
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

#     jump blowup_moon

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

#     show eileen happy

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
