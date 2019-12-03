label intro:
    #scene black

    you "Of which I'm certain...... I've lived a life that's full...... I've traveled each and every highway....."

    Jerry "Oi Arthur"

    you "much more than this.... I DID IT MY WAYYYYYY"

    Jerry "ARTHURRRRRR"

    stop backgroundSound

    you "What now jezzz that was the best part"

    Jerry "If your gonna sing could you at least turn the goddamn mic off."

    you "Ohhh it was on?"

    Jerry "It was on ever since you got on duty."

    you "Well at least you get to hear some of my amazing singing"

    Jerry "Ohh how I love it when you go out of tune with your husky voice."

    you "Hey believe it or not I used to take lessons."

    Jerry "Funny how that turned out."

    you "You know I never imagined being a security guard for a school would be so tough. As if dealing with those up to no good rascals during semester weren't tiring enough, now I am stuck here midnight working on silly reports."

    Jerry "That's life pal. Should have listened to your parents and stayed in school."

    menu:
        "Agree":
            jump agree

        "Disagree":
            jump disagree

    label agree:
        you "Yeah... Maybe I should have. I'd probably have a nice job, owned a place of my own and not be worried about this racked up debt I have."

        Jerry "Remind me again why you have this massive debt?"

        you "Let's just say I have made some bad choices and decided to do business with cunning people."

        Jerry "So you basically got scammed? Sounds like a very Arthur thing to do not going to lie."

        you "Shut up. At that time they seemed very professional and trustworthy. I knew something was fishy but they brainwashed me somehow. I was too gullible."

        Jerry "It's too late the change the past and things could have been worse. You should be grateful you even got a job."

        you "Yeah... I suppose."

        Jerry "You know what would make you feel better?"

        you "What?"

        Jerry "A nice cold one."

        you "You know me well, Jerry."

        $ personality -= 1

        return

    label disagree:
        $ personality += 1

        you "I don't regret anything though. I had a lot of fun and made a lot memories and I'd take that over reading books and remembering pointless equations any day."

        Jerry "Well then stop complaining."

        you "Ohhh just let me rant a little, it's not like you love this job either."

        Jerry "I mean it's a job and I am grateful for it. Definitely better than being a janitor, gosh that experience was horrible. Not only are you doing the dirty work, people don't give you respect at all."

        you "As if we get much respect as security guards."

        Jerry "hhhh... I could really use a cold beer right about now"

        return
