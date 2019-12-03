label bar:

    Jerry "Speaking of alcohol, we should head to a bar and meet up with Franky and Lee. It's been a while since we all got together and had a cold one."

    you "Now that you have mentioned it, it's been a long time since I have seen them. It's a good thing they left this boring job and pursued something else."

    Jerry "Yeah, heard Lee is doing well with his hotdog stand. Not sure what Franky has been up to though."

    you "Last time I spoke to him was when he quit. Said something about working for his brother in a repair shop."

    Jerry "Ahhh that's nice. Kinda miss having them arround to be honest."

    you "Yeah, they made night shifts not suck. Now I am stuck with you."

    Jerry "The feeling is mutual."

    #show static_animation at truecenter

    menu:
        "Agree to go have drinks":
            you "Alright, I will shoot them a text and see when they are available."

            Jerry "Sounds good."

            $ mood += 1

            return

        "Refuse to go have drinks":
            $ mood -= 1

            you "Maybe some other time pal, I got a lot of things on my shoulders now."

            Jerry "Saying no to drinks? Wow, who are you and what have you done with Arthur."

            you "Shut up."

            return
