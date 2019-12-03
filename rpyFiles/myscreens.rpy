screen myLeftEarphone():

    imagebutton:
        xalign 0.3
        yalign 0.5
        auto "images/whiteleft_%s.png" action [Hide("myLeftEarphone"), Return()]

    imagebutton:
        xalign 0.7
        yalign 0.5
        auto "images/whiteright_%s.png" action [Hide("myLeftEarphone"), Return()]



screen playMusic():
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "images/mp3.jpg"
        action [Hide("playMusic"), Play("backgroundSound","myWay.mp3") ,Return()]

screen donut():
    imagebutton:
        xalign 0.3
        yalign 0.5
        idle "images/donut.png"
        action [Hide("coffee"),Play("backgroundSound","munching.mp3"), Return()]

screen coffee():
    imagebutton:
        xalign 0.7
        yalign 0.5
        idle "images/coffee.jpg"
        action [Hide("donut"), Play("backgroundSound","slurping.wav"), SetVariable("donutOrNot", False), Return()]

screen walkieTalkie():
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "images/walkietalkie.jpg"
        action [Play("backgroundSound", "walkie.mp3"), Return()]

screen torch():
    imagebutton:
        xalign 0.8
        yalign 0.3
        idle "torchy"
        hover "yellowTorch"
        action [ Hide("torch"), Call('hitTorch'), Return()]

screen map():
    imagebutton:
        xalign 0.1
        yalign 0.3
        idle "paperMap"
        hover "yellowPaperMap"
        action [Hide("map"), Call("readMap"), Return()]

screen MapScreen():
    frame:
        xalign -0.3
        yalign -0.3
        xsize 1920
        ysize 1000
        background "school-layout.png"
        button:
            xpos 700
            ypos 500
            text "home"
            action Hide("MapScreen")

screen mapIcon():
    imagebutton:
        xalign 0.9
        yalign 1.0
        idle "mapIcon"
        action [Show('MapScreen')]


screen door():
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "doorOpen"
        hover "doorClosed"
        action [Hide("door"), Play("sound", "doorOpening.mp3", True),Return()]

screen lockerOrForward():
        add "hallway3"
        imagebutton idle "images/justlocker.jpg" hover "images/lockerHighlight.jpg" xpos 294 ypos 209 action [Hide("lockerOrForward"), Jump("insideLocker")]
        imagebutton idle "images/wayOut.png" hover "images/highlightedWayOut.png" xpos 1178 ypos 238 action [Hide("lockerOrForward")]

screen oneInsideLocker():
    imagebutton:
        xalign 0.5
        yalign 0.9
        idle "images/lolipopWithWrapper.jpg"
        hover "images/HlolipopWithWrapper.jpg"
        action [ SetVariable("allSeenInLocker", allSeenInLocker + 1), Hide("oneInsideLocker"), Call("lolipop")]


screen twoInsideLocker():
    imagebutton:
        xalign 0.4
        yalign 0.9
        idle "images/bookOnTheFloor.jpg"
        hover "images/HbookOnTheFloor.jpg"
        action [ SetVariable("allSeenInLocker", allSeenInLocker + 1), Hide("twoInsideLocker"), Call("bookOnFloor")]

screen threeInsideLocker():
    imagebutton:
        xalign 0.7
        yalign 0.9
        idle "images/rolledPaper.jpg"
        hover "images/HrolledPaper.jpg"
        action [SetVariable("allSeenInLocker", allSeenInLocker + 1), Hide("threeInsideLocker"), Call("bookOnFloor")]

screen crumpledPaper():
    frame:
        xalign -0.3
        yalign -0.3
        xsize 1920
        ysize 1000
        background "images/crumpledPaper"
        button:
            xpos 700
            ypos 500
            text "back"
            action Hide("images/crumpledPaper")

screen instruLeave():
    imagebutton:
        xalign 0.8
        yalign 0.9
        idle "play.png"
        hover "playH.png"
        action [Hide("instruLeave"), SetVariable("start", True)]
