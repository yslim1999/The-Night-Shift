label takingATrip:
    you "You know I could use some time off from this job. I need a change of scenary. Maybe a trip to the coasts might do the trick."

    Jerry "We don't get many days off Arthur I suggest you use them wisely."

    you "Like I got anything useful for em. I got no other responsibilities unlike you I ain't got no children to worry about. How are ya kids though?"

    Jerry "Ohhh man, they are a handful I tell ya. Especially the oldiest Eddie. But being a father really changes you."

    you "That's sweet. But I bet it hurts the wallet doesn't it."

    Jerry "It's worth it. Anyways, I am in the library. Just gonna give a look see."

    you "Alright."

    call heardAboutNews

    return

label heardAboutNews:
    Jerry "Have you read about the news about that 16 year old boy?"

    you "Sorry I am allergic to newspaper. But What happened?"

    Jerry "The kid got severely injured in a protest. They said he failed to follow instructions and even assulted a police. Or at least they claim."

    you "That sounds very controversial. What kind of protest was it?"

    Jerry "I can't remember but I think it was climate change. But regardless I don't think he should be put into the hospital for protesting."

    menu:
        "Agree with Jerry":
            you "Yeah, nobody should. They promote freedom but put us down for speaking out. A bunch of hypocrites running this country."

            Jerry "No joke. But maybe there was more to the story that the media is trying to cover up."

            you "This is why I am not political. Just stand by the side and have no worries."

            Jerry "Not sure if I agree with that."

            you "Whatever you say pal."

            $ personality += 1

            return

        "Disagree with Jerry":
            you "Not saying he deserved to be put into the hospital but he must have done something wrong to make the police go to such lengths."

            Jerry "Your probably right but then again I don't trust the media so it is hard to justify who's fault it is."

            you "I mean back when I was his age I was pretty stubborn myself so it's no surprise if it was just him trying to act all tough."

            Jerry "Yet nothing has changed since. If anything, your stubborness has grown significantly."

            $ personality += 1


            if donutOrNot:
                you "Yeah forget about the donuts I was talking about earlier."
                Jerry "Hey I was just playing. Come on."
            else:
                you "Go back to work."
                Jerry "Hehehe"

            return
