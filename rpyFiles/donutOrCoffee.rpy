label donutOrCoffee:

    if donutOrNot == False:
        you "Ahhhh... Nothing like a warm coffee."
        $ renpy.pause(4.0, hard = True)
        hide screen coffee
        stop backgroundSound
        return


    if donutOrNot:
        you "This is so good... hmmm..."
        hide screen donut
        $ renpy.pause(2.0, hard = True)
        show eatenDonut
        $ renpy.pause(2.0, hard = True)
        stop backgroundSound
        return




    #*You look to the corner of your desk and see a cup of coffee and a box of donuts.
