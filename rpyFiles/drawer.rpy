label drawer:
    scene drawer with fade:

    show screen map

    python:
        ui.interact()

    show screen torch

    python:
        ui.interact()

    show screen mapIcon

    "You can view the map at anytime with the icon on the top right"

    scene black with fade

    call screen door

    $ renpy.pause(2.0, hard = True)

    stop sound

    return
