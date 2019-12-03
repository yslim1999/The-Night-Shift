# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#renpy documentation
init python:
    def walkie_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("walkietalkie.wav")

        elif event == "slow_done":
            renpy.sound.stop()

define you = Character("You")

define Jerry = Character("Jerry", callback=walkie_sound)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $ donutOrNot = True
    $ spokeTwice = False
    $ start = False
    $ allSeenInLocker = 0
    $ mood = 0
    $ personality = 0

    call instruction

    scene black with fade:

    call preIntro

    call screen myLeftEarphone

    "Now let's see..."

    call screen playMusic

    scene begin with fade:

    $ renpy.pause(4.0, hard = True)

    scene introArthur with fade:

    $ renpy.pause(4.0, hard = True)

    scene timeIntro with fade:

    $ renpy.pause(4.0, hard = True)

    scene 2ndIntro with fade:

    $ renpy.pause(4.0, hard = True)

    scene nightshift with fade:

    $ renpy.pause(5.0, hard = True)

    scene black

    scene cibr with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    call intro

    call bar

    call preDandC

    show screen donut

    call screen coffee

    call donutOrCoffee

    if donutOrNot:
        call postDonut
        $ mood += 1
    else:
        call postCoffee
        $ mood += -1

    call takingATrip

    call lightsOut

    call drawer

    call importantDecision

    # This ends the game.

    return
