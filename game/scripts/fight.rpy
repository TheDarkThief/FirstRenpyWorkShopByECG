#Astrid Health
astridMaxHp = 100
astridHp = astridMaxHp

#bad alien health
alienMaxHP = 100
alienHp = alienMaxHP

#Random number generator
label diceRoll:
    d4 = renpy.random.randint(1, 4)
    d6 = renpy.random.randint(1, 6)
    d10 = renpy.random.randint(1, 10)
    d20 = renpy.random.randint(1, 20)
    return

label start:

call diceRoll
while astridHp > 0:

#player turn
    menu:
    "Punch":
        if d20 >= 17:        # 15% chance Crit
            astridDamage = (d4 + d4) * 2
            alienHp -= astridDamage
            "Crit!!! [astridDamage] damage!!!"
        elif d20 >= 4 and d20 < 17:  # 60% chance Normal hit (d20 >= 8 covers 8 to 16)
            astridDamage = (d4 + d4)
            alienHp -= astridDamage
            "[astridDamage] damage!"
        else:                # 25% chance to miss (d20 < 8)
            astridDamage = 0
            alienHp -= astridDamage
            "Miss! Be better next time!"

    laserCharges = 5
    "Laser Beam":
        if laserCharges == 0:
            astridDamage = 0
            alienHp -= 0
            "No charges left!"
        elif d20 <= 17:        # 15% chance Crit
            astridDamage = (d6 + d10) * 2
            alienHp -= astridDamage
            laserCharges -= 1
            "Crit!!! [astridDamage] damage!!!"
        elif d20 >= 10 and d20 < 17:  # 35% chance Normal hit
            astridDamage = (d6 + d10)
            alienHp -= astridDamage
            "[astridDamage] damage!"
            laserCharges -= 1
        else:                # 50% chance to miss (d20 < 10)
            astridDamage = 0
            alienHp -= astridDamage
            "Miss! Be better next time!"
            laserCharges -= 1
    "Bandage"
        heal = d6 + d10
        astridHp += heal
        "Health restored by [heal]!"

    kits = 5
    "First Aid Kit"
        if healingCharge == 0:
            "Out of Super First Aids!"
        else:
            heal = 20
            astridHp =+ heal
            "Health restored by [heal]!"
            kits -= 1

#Enemy turn - initial random behavior and then has a "preservation mode"
    call diceRoll
    if alienHp < 50: #alien enters healing mode a second phase of sorts?
        if d10 == 1: # 10% chance to full heal
            alienHp = alienMaxHP
            "The Alien fully regenerates!"
        elif d10 > 1 and d10 < 5: #40 chance to normal heal
            alienHp += d20
            "The alien heals for [d20]!"
        elif d10 >= 5: #50% chance to wild attack
            alienAttack = d20 + d10
            astridHp -= attack
            "The Alien desperately lashes out for [alienAttack] damage!"
    else:
        if  d10 >= 5: #50% chance to normal attack
            alienAttack = d10 + d6
            astridHp -= attack
            "The Alien hits for [alienAttack] damage!"







