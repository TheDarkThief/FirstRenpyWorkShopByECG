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

label blowup_moon:
    play audio "audio/explosion.mp3"
    scene black
    show moon-exploding1
    pause 0.25
    show moon-exploding2
    pause 0.25
    show moon-exploding3
    pause 0.25
    show moon-exploding4
    pause 0.25
    show moon-exploding5
    pause 0.25
    show moon-exploding6
    pause 0.25
    show moon-exploding7
    pause 0.25
    show moon-exploding8
    pause 0.25
    show moon-exploding9
    pause 0.25
    show moon-exploding10
    pause 0.25
    show moon-exploding11
    pause 0.25
    scene moon-explosion-ending
    pause 30
