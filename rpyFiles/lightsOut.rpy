init:
    $ flash = Fade(.25, 0, .75, color="#fff")

label lightsOut:

    scene blackOut with flash

    you "WHAT THE??"

    "*Must have been a trip again. When is this school going to fix this."

    show static_animation

    "*Even the security screen went static"

    you "Jerry, there might have been a trip again. A few cameras ain't showing up."

    play sound "walkie.mp3"

    $ renpy.pause(4.0, hard = True)

    "......"

    call screen walkieTalkie

    you "Jerry? you there?"

    you "Jerry can you hear me?"

    stop backgroundSound

    you "Guess I have to go this time. Let me grab my torch in the drawer."

    return
