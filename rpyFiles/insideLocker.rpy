label insideLocker:
    $ temp = True

    scene insideTheLocker with fade

    show screen oneInsideLocker

    show screen twoInsideLocker

    show screen threeInsideLocker

    #renpy has no break statements
    while temp:
        if allSeenInLocker >= 3:
            $ temp = False
        else:
            $ renpy.pause(1.0, hard = True)
        $ print allSeenInLocker


    return
