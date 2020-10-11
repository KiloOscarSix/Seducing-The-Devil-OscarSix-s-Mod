
    # Scene 50

    # Dad journey to darkness

$ dad_journey_todark = False


label dadjourneytodark:

    scene episode5 with Dissolve (1.0)

    pause

    scene blackscreen with Dissolve (1.0)

    DA "Why is it so dark here?"

    DA "Where am I?"

    DA "Hello!"

    DA "Anybody there?"

    scene scene_50-1 with Dissolve (1.0)

    DA "Huh?! Whe where am I?"

    scene doorhouse with Dissolve (1.0)

    DA "WHAT THE?! WHAT IS THIS PLACE?!"

    DG "Hello Adam"

    DA "Who's there?! Where are you?"

    DG "My name is Lileva."

    DA "Why can't I see you? Where am I? What is this place?"

    DG "You are in my world Adam. I can see you but you can't see me."

    DA "What? I don't understand."

    DG "You will understand it very soon Adam. Why don't you just go and open the first door from the left."

    DA "Why would I do that?! Where the fuck am I?!"

    DG "Everything will be answered Adam. Just do what I say."

    DA "I don't trust you! I was with Veronica. Then something happened. You are the reason behind it, aren't you?"

    DG "You are testing my patience Adam. Don't be so rude. Just open the door and you'll find out everything."

    DA "....."

    jump doorhouse

    $ door1 = False


    # Door 1

label door1:

    scene scene_50-2 with Dissolve (1.0)

    with vpunch

    DA "WHAT THE FUCK?!!"

    DG "Do you like what you see?"

    DA "Rachel you fucking bitch!!"

    if renpy.loadable("patch.rpy") or patch:

        DG "Your grown up son with your wife. His mother. Taking a bath together. All naked.. mhmmmm hot.."

        scene scene_50-3 with Dissolve (1.0)

        A "[Mom_name] I think we should stop."

        scene scene_50-4 with Dissolve (1.0)

        MO "Huh? What do you mean?"

        A "I'm an adult now. I don't think it is okay to take bath together anymore."

        MO "Why would you say that?"

        A "I mean we are naked right now. Is this even okay to look at your naked mother?"

        A "What if [Dad_name] finds out?"

        scene scene_50-5 with Dissolve (1.0)

        MO "Oh silly.. There's nothing wrong in taking a bath together. I'm your mother. We aren't doing anything funny, are we?

            And your dad doesn't need to know and he won't. Don't worry about it. We can show our skins as long as it's nothing sexual."

        A "Are you sure [Mom_name]?"

        scene scene_50-6 with Dissolve (1.0)

        MO "Absolutely son. We have a special bond. Let's not break it for silly reasons.
            I love you son.."

        A "Love you too mom."



    if not renpy.loadable("patch.rpy"):

        DG "[player_name] with your wife. Taking a bath together. All naked.. mhmmmm hot.."

        scene scene_50-3 with Dissolve (1.0)

        A "Rachel, I think we should stop."

        scene scene_50-4 with Dissolve (1.0)

        MO "Huh? What do you mean?"

        A "I'm an adult now. I don't think it is okay to take bath together anymore."

        MO "Why would you say that?"

        A "I mean we are naked right now. It feels like cheating on Adam."

        A "What if he finds out?"

        scene scene_50-5 with Dissolve (1.0)

        MO "Oh silly.. There's nothing wrong in taking a bath together. We aren't doing anything funny, are we?

            And Adam doesn't need to know and he won't. Don't worry about it. We can show our skins as long as it's nothing sexual."

        A "Are you sure Rachel?"

        scene scene_50-6 with Dissolve (1.0)

        MO "Absolutely. We have a special bond. Let's not break it for silly reasons.
            I love you [player_name].."

        A "Love you too Rachel."

    $ door1 = True

    jump doorhouse


    # Scene 51

    # Door 2

    $ door2 = False

label door2:

    scene scene_51-1 with Dissolve (1.0)

    DA "What is she upto this time?"

    DA "She is wearing that transparent nighty. She is in [player_name]'s room, isn't she?"

    DG "Keep watching."

    scene scene_51-2 with Dissolve (1.0)

    with hpunch

    DA "I fucking knew it! That bitch has been lusting over him. Fucking bitch. I'm gonna kill you!!"

    DG "Shhh don't speak."

    scene scene_51-3 with Dissolve (1.0)

    DG "Just look at how she is staring at him. She wants him so bad. Where have you failed Adam?"

    DA "What the fuck are you talking about?!"

    scene scene_51-4 with Dissolve (1.0)

    DA "OH WOW!! Watching porn. And she is standing there, touching herself. I'm living in a mad house!"

    scene scene_51-5 with Dissolve (1.0)

    DA "FUCK!! Get me out of here! NOW!"

    $ door2 = True

    jump doorhouse2



    # Scene 52

    # Door 3


    $ door3 = False


label door3:

    scene scene_52-1 with Dissolve (1.0)

    DA "Veronica... My darling.."

    DG "You love her a lot, don't you?"

    DA "Yes a lot. She means everything to me."

    DG "Then why did you let her go in the first place?"

    DA "I lost my mind back then. I regret about everything. Veronica.."

    V "Is he still acting up?"

    MO "Yes. It's getting out of hand."

    V "Are you still thinking about that? Or have you changed your mind?"

    scene scene_52-2 with Dissolve (1.0)

    MO "Do you even see another way?"

    MO "How much more can I do? He has no love for me inside him. Everytime I try to get close, he just pushes me away."

    MO "I don't even remember the last time we had sex."

    DA "So they are talking about the divorce. Good thing I've made up my mind.
        And who would fuck such a filthy slut anyway?"


    if renpy.loadable("patch.rpy") or patch:

        DG "**Whishpers** Your son would.."

        DA "What? I didn't hear you clearly."

        scene scene_52-3 with Dissolve (1.0)

        V "Why don't you convince him to go a trip for few days? Maybe a change of weather and environment can help."

        MO "He won't listen to me. He doesn't even listen to [player_name]."

        DA "He is a prick. Why would I listen to a prick?"

        scene scene_52-4 with Dissolve (1.0)

        DA "Oh speak of the devil.."

        A "[Mom_name].. My neck hurts.."

        DA "Yeah serves you right for watching porn all day. Who knows what else you did.."

        scene scene_52-5 with Dissolve (1.0)

        V "[player_name].. Honey.. Come here. Let me take a look at it."

        MO "Yes let her take a look. She is really good at fixing muscle pain."

        A "Aah okay."

        scene scene_52-6 with Dissolve (1.0)

        V "Where do you feel pain [player_name]?"

        V "Did you sleep in a weird position?"

        scene scene_52-7 with Dissolve (1.0)

        A "The lower neck part. No I had to do a college project all night long.
           My finals are right up ahead. I worked all night and then woke up with a pain."

        V "Oh I see."

        DA "Project or porn you fucker?!"

        DA "Why can't they hear me?!"

        DG "SShhh..."

        V "Let's see."

        scene scene_52-8 with Dissolve (1.0)

        V "Hmmm.. I feel a bit of tension there. A bit of massage can help but it totally depends on you [player_name].
           You need to take care of yourself. You can't stay seated for all night long and not expect neck or back pain."

        A "Ahh yeah.."

        DA "She is touching that filthy prick.
            Here I am dying to get her touch."

        DA "Wait! We were about to have sex! Lileva!! What did you do?!"

        scene scene_52-9 with Dissolve (1.0)

        A "*GASP!!*"

        DA "FUCKING ASSHOLE!!! STARING AT MY VERONICA!!! I'LL FUCKING KILL YOU!!"

        DA "DO SOMETHING LILEVA!! HE ALREADY TOOK RACHEL AND NOW GOING AFTER MY VERONICA!!"

        DG "HAHAHAHA!!! SShhh..."

        scene scene_52-10 with Dissolve (1.0)

        V "Are you feeling better honey?"

        A "Yess muuch better."

        V "Haha very funny [player_name].."

        DG "Rachel is jealous."

        DA "I don't care! Let's be done with the other doors!"


    if not renpy.loadable("patch.rpy"):

        DG "**Whishpers** [player_name] would.."

        DA "What? I didn't hear you clearly."

        scene scene_52-3 with Dissolve (1.0)

        V "Why don't you convince him to go a trip for few days? Maybe a change of weather and environment can help."

        MO "He won't listen to me. He doesn't even listen to [player_name]."

        DA "He is a prick. Why would I listen to a prick?"

        scene scene_52-4 with Dissolve (1.0)

        DA "Oh speak of the devil.."

        A "Rachel.. My neck hurts.."

        DA "Yeah serves you right for watching porn all day. Who knows what else you did.."

        scene scene_52-5 with Dissolve (1.0)

        V "[player_name].. Honey.. Come here. Let me take a look at it."

        MO "Yes let her take a look. She is really good at fixing muscle pain."

        A "Aah okay."

        scene scene_52-6 with Dissolve (1.0)

        V "Where do you feel pain [player_name]?"

        V "Did you sleep in a weird position?"

        scene scene_52-7 with Dissolve (1.0)

        A "The lower neck part. No I had to do a college project all night long.
           My finals are right up ahead. I worked all night and then woke up with a pain."

        V "Oh I see."

        DA "Project or porn you fucker?!"

        DA "Why can't they hear me?!"

        DG "SShhh..."

        V "Let's see."

        scene scene_52-8 with Dissolve (1.0)

        V "Hmmm.. I feel a bit of tension there. A bit of massage can help but it totally depends on you [player_name].
           You need to take care of yourself. You can't stay seated for all night long and not expect neck or back pain."

        A "Ahh yeah.."

        DA "She is touching that filthy prick.
            Here I am dying to get her touch."

        DA "Wait! We were about to have sex! Lileva!! What did you do?!"

        scene scene_52-9 with Dissolve (1.0)

        A "*GASP!!*"

        DA "FUCKING ASSHOLE!!! STARING AT MY VERONICA!!! I'LL FUCKING KILL YOU!!"

        DA "DO SOMETHING LILEVA!! HE ALREADY TOOK RACHEL AND NOW GOING AFTER MY VERONICA!!"

        DG "HAHAHAHA!!! SShhh..."

        scene scene_52-10 with Dissolve (1.0)

        V "Are you feeling better honey?"

        A "Yess muuch better."

        V "Haha very funny [player_name].."

        DG "Rachel is jealous."

        DA "I don't care! Let's be done with the other doors!"


    $ door3 = True

    jump doorhouse3



    # Scene 53

    # Door 4

    $ door4 = False


label door4:

    scene scene_53-1 with Dissolve (1.0)

    DA "That's Rachel. I can already tell. I've fucked her so many times that I will recognize that pussy from miles away."

    MO "aahhh... ahh..mmm...mhmmm..."

    scene scene_53-2 with Dissolve (1.0)

    MO "uuhmmm...mmmm...."

    DA "She has a beautiful body though. Big beautiful tits and that cute bush."

    DG "Changing your mind, are you?"

    DA "Absolutely not!"

    DA "Who is she even thinking about?"

    scene scene_53-3 with Dissolve (1.0)

    DA "OH YES! Why am I not surprised?!"


    if renpy.loadable("patch.rpy") or patch:


        DA "Watching his mother masturbate.. Nice.."

        DG "Are you getting jealous now?"

        DA "She is still my wife! And he is our kid!! This is so wrong!!"

        scene scene_53-4 with Dissolve (1.0)

        DG "Well I see nothing wrong here.. He is getting hard.. Rock hard.. For his mother mmmhmmm..."

        DA "STOP!! GET ME OUT OF HERE!!"

        DG "NA AH AAAH..."

        scene scene_53-5 with Dissolve (1.0)

        DA "Is this really happening right now?!!"

        DA "YOU MOTHERFUCKER!!"

        scene scene_53-6 with Dissolve (1.0)

        MO "[player_name]!!!!! AAAHHHHHH GOODD!!!!"

        DA "She's thinking about him...WOW!!"

        scene scene_53-7 with Dissolve (1.0)

        DA "OH...."

        DG "Almost there..."

        DG "Look at that big dick.. Both of them are going at it..
            No more boundaries.."

        DA "I knew it!! I knew it!!"

        scene scene_53-8 with Dissolve (1.0)

        MO "[player_name]!! I know you are there!! Don't just stand there and watch me suffer!!"

        DA "WHAT THE?!"

        MO "I know that you watch me like this everyday. Please [player_name]!!"

        MO "Don't you see how desperate I am?! [player_name]!!"

        scene scene_53-9 with Dissolve (1.0)

        A "Oh no!"

        DA "Is this really happening?!"

        DA "Are they really going to fuck each other?!!"

        DG "Hehehehe...."

        scene scene_53-10 with Dissolve (1.0)

        pause

        scene scene_53-11 with Dissolve (1.0)

        pause
        scene scene_53-12 with Dissolve (1.0)

        pause



    if not renpy.loadable("patch.rpy"):


        DA "Watching her masturbate.. Nice.."

        DG "Are you getting jealous now?"

        DA "She is still my wife! This is so wrong!!"

        scene scene_53-4 with Dissolve (1.0)

        DG "Well I see nothing wrong here.. He is getting hard.. Rock hard.. For a beautiful woman mmmhmmm..."

        DA "STOP!! GET ME OUT OF HERE!!"

        DG "NA AH AAAH..."

        scene scene_53-5 with Dissolve (1.0)

        DA "Is this really happening right now?!!"

        DA "YOU MOTHERFUCKER!!"

        scene scene_53-6 with Dissolve (1.0)

        MO "[player_name]!!!!! AAAHHHHHH GOODD!!!!"

        DA "She's thinking about him...WOW!!"

        scene scene_53-7 with Dissolve (1.0)

        DA "OH...."

        DG "Almost there..."

        DG "Look at that big dick.. Both of them are going at it..
            No more boundaries.."

        DA "I knew it!! I knew it!!"

        scene scene_53-8 with Dissolve (1.0)

        MO "[player_name]!! I know you are there!! Don't just stand there and watch me suffer!!"

        DA "WHAT THE?!"

        MO "I know that you watch me like this everyday. Please [player_name]!!"

        MO "Don't you see how desperate I am?! [player_name]!!"

        scene scene_53-9 with Dissolve (1.0)

        A "Oh no!"

        DA "Is this really happening?!"

        DA "Are they really going to fuck each other?!!"

        DG "Hehehehe...."

        scene scene_53-10 with Dissolve (1.0)

        pause

        scene scene_53-11 with Dissolve (1.0)

        pause
        scene scene_53-12 with Dissolve (1.0)

        pause


    $ door4 = True

    jump doorhouse4



    # Scene 54

    # Door 5

    $ door5 = False

label door5:

    scene scene_54-1 with Dissolve (1.0)

    DA "That's me! How am I there if I'm here?!"

    scene scene_54-2 with Dissolve (1.0)

    pause

    scene scene_54-3 with Dissolve (1.0)

    DA "WOW! She is leaving in the middle of the night. To her lover she goes.."

    scene scene_54-4 with Dissolve (1.0)

    pause

    scene scene_54-5 with Dissolve (1.0)

    pause

    scene scene_54-6 with Dissolve (1.0)

    pause

    scene scene_54-7 with Dissolve (1.0)

    pause

    scene scene_54-8 with Dissolve (1.0)

    pause

    scene scene_54-9 with Dissolve (1.0)

    DA "...."

    $ door5 = True

    jump doorhouse5



    # Scene 55

    # Door 6


    $ door6 = False

label door6:



    if renpy.loadable("patch.rpy") or patch:

        scene scene_55-1 with Dissolve (1.0)

        DG "ahaha that morning wood.. So sexy.."

        DA "And here we go.."

        DG "Will you just shut up? Let's witness the most beautiful moment between a mother and her son.."

        scene scene_55-2 with Dissolve (1.0)

        MO "Haa...umm...."

        scene scene_55-3 with Dissolve (1.0)

        MO "Uckk...Oh my.."

        MO "(The last time I didn't even look at him properly. I was too shy and horny..mmm)"

        scene scene_55-4 with Dissolve (1.0)

        MO "(So big and so hot.. mmmhmmm... He was so good with it.. mmm)"

        MO "(Let's have a little fun)"

        scene scene_55-5 with Dissolve (1.0)

        MO "eemmm *lick*"

        MO "(He will love it.. Waking up to his mom tasting his big hard cock)"

        scene scene_55-6 with Dissolve (1.0)

        MO "*Lick* *lick*"

        window hide

        scene scene_55-5 with Dissolve (0.5)
        scene scene_55-6 with Dissolve (0.5)
        scene scene_55-5 with Dissolve (0.5)
        scene scene_55-6 with Dissolve (0.5)
        scene scene_55-5 with Dissolve (0.5)
        scene scene_55-6 with Dissolve (0.5)
        scene scene_55-5 with Dissolve (0.5)
        scene scene_55-6 with Dissolve (0.5)

        MO "(He needs to be treated even better. I know what I have to do)"

        scene scene_55-7 with Dissolve (1.0)

        MO "*Ukhh*"

        scene scene_55-8 with Dissolve (1.0)

        MO "ummm...mmhmmm.."

        MO "(I can't even fit the whole thing)"

        window hide

        scene scene_55-7 with Dissolve (0.5)
        scene scene_55-8 with Dissolve (0.5)
        scene scene_55-7 with Dissolve (0.5)
        scene scene_55-8 with Dissolve (0.5)
        scene scene_55-7 with Dissolve (0.5)
        scene scene_55-8 with Dissolve (0.5)
        scene scene_55-7 with Dissolve (0.5)
        scene scene_55-8 with Dissolve (0.5)

        scene scene_55-9 with Dissolve (1.0)

        A "Uhh mom!"

        A "What are you doing?"

        A "Dad's still at home!"

        scene scene_55-10 with Dissolve (1.0)

        MO "Shush son.. Let me take care of you. Adam won't wake up just yet.."

        MO "I want you so bad baby.."

        A "Oh mom..."

        window hide

        scene scene_55-7 with Dissolve (0.5)
        scene scene_55-8 with Dissolve (0.5)
        scene scene_55-7 with Dissolve (0.5)
        scene scene_55-8 with Dissolve (0.5)
        scene scene_55-7 with Dissolve (0.5)
        scene scene_55-8 with Dissolve (0.5)
        scene scene_55-7 with Dissolve (0.5)
        scene scene_55-8 with Dissolve (0.5)

        A "OH FUCK!!!"

        scene scene_55-11 with Dissolve (1.0)

        MO "Do you want to be inside your mommy [player_name]?"

        A "Yes mom...yes.."

        scene scene_55-12 with Dissolve (1.0)

        MO "Uuhh..."

        A "ahhmm.. so warm..."

        scene scene_55-13 with Dissolve (1.0)

        A "You have such beautiful breasts mom.. mmmhmmm.."

        MO "Oh [player_name]..my baby.."

        scene scene_55-14 with Dissolve (1.0)

        MO "You are soooo biggg my boy.."

        A "Mom..."

        scene scene_55-15 with Dissolve (1.0)

        A "Oh yess.. ahhh...mmmm... mom..."

        MO "AAhhh.."

        window hide

        scene scene_55-14 with Dissolve (0.5)
        scene scene_55-15 with Dissolve (0.5)
        scene scene_55-14 with Dissolve (0.5)
        scene scene_55-15 with Dissolve (0.5)
        scene scene_55-14 with Dissolve (0.5)
        scene scene_55-15 with Dissolve (0.5)
        scene scene_55-14 with Dissolve (0.5)
        scene scene_55-15 with Dissolve (0.5)
        scene scene_55-14 with Dissolve (0.5)
        scene scene_55-15 with Dissolve (0.5)

        MO "hhanngg...mmhmmm...ah ah ha..."

        MO "FUCK ME [player_name]!! FUCK ME HARD!! FUCK YOUR MOTHER HARD!!"

        window hide

        scene scene_55-16 with Dissolve (1.0)
        scene scene_55-17 with Dissolve (0.5)
        scene scene_55-16 with Dissolve (0.5)
        scene scene_55-17 with Dissolve (0.5)
        scene scene_55-16 with Dissolve (0.5)
        scene scene_55-17 with Dissolve (0.5)
        scene scene_55-16 with Dissolve (0.5)
        scene scene_55-17 with Dissolve (0.5)
        scene scene_55-16 with Dissolve (0.5)
        scene scene_55-17 with Dissolve (0.5)

        MO "OH GOD!! SO GOOD!! MY SON IS FUCKING ME SOOO GOOD!!"

        scene scene_55-18 with Dissolve (1.0)

        A "MOM!! I'm gonna cum!!"

        MO "Cum inside me baby.. Give me all of your seeds!! mmhmmm"

        A "AAAHHHH...!!!"

        scene scene_55-19 with Dissolve (1.0)

        with vpunch

        A "aahh.."

        with vpunch

        A "Oh gosh!! Ahhhmmm..."

        MO "[player_name]..!!"

        scene scene_55-20 with Dissolve (1.0)

        MO "haahh haaahh..so much cum.."

        A "Mom.. mom.."

        scene scene_55-21 with Dissolve (1.0)

        MO "My son.. It was so good.. You even came inside me.."

        A "You are amazing mom.. This is so taboo but I don't care anymore. I love you and that's all I know.."

        MO "I love you too son.. I love you more than anything.."

        scene scene_55-22 with Dissolve (1.0)

        MO "*mwah*"

        scene scene_55-23 with Dissolve (3.0)

        A "You smell good mom.."

        MO "Hehehe.. I'll stay for few more minutes.. I want to enjoy your embrace.."

        A "You are such a lovey dovey, aren't you?"

        MO "More like crazy for my own son.."

        A "You make it sound more sexy.."

        MO "Honey don't forget to wear your underwear. You forgot to wear it after taking it off last night.."

        A "Wait! How did you....?"

        MO "Hahah I have seen you watching porn so many times.."

        A "Ahh...Mom.."

        MO "It's alright. How about we watch it together tonight?"

        A "Sounds like a plan. I'll download something spicy."

        MO "Can't wait to have fun heheh.."

        A "I better go and put something on.."

        MO "Sure honey.."
        $ renpy.end_replay()
        scene scene_55-24 with Dissolve (3.0)

        DA "WHERE THE FUCK WERE YOU?!"

        DA "FUCKING SOME STREET DOG ALL NIGHT, WERE YOU?!"

        MO "Oh god Adam. Lower your voice. [player_name] is sleeping. He will hear you."

        DA "Let that prick hear. You have been trying to get his dick. Did you think I won't find out?!"

        MO "What are you talking about?!"

        MO "Have you gone mad?!"

        DA "DON'T YOU TRY TO FOOL ME YOU LITTLE BITCH!! I'VE SEEN THE WAY YOU LOOK AT HIM!"

        MO "OH so are we completely going to ignore how you have been trying so hard to get Veronica back?!

            SHE DOESN'T EVEN GIVE A SHIT ABOUT YOU!"

        "*SMACK* *SMACK*"

        MO "OH Nooo...stop... no..."

        "*crying*"

        scene scene_55-25 with Dissolve (3.0)

        MO "*sniff* *sniff*"

        MO "[player_name]..[player_name]..[player_name].."

        A "Uhh [Mom_name] let me sleep!"

        scene blackscreen with Dissolve (1.0)



    if not renpy.loadable("patch.rpy"):

        scene scene_55-1 with Dissolve (1.0)

        DG "ahaha that morning wood.. So sexy.."

        DA "And here we go.."

        DG "Will you just shut up? Let's witness the most beautiful moment between a man and a woman.."

        scene scene_55-2 with Dissolve (1.0)

        MO "Haa...umm...."

        scene scene_55-3 with Dissolve (1.0)

        MO "Uckk...Oh my.."

        MO "(The last time I didn't even look at him properly. I was too shy and horny..mmm)"

        scene scene_55-4 with Dissolve (1.0)

        MO "(So big and so hot.. mmmhmmm... He was so good with it.. mmm)"

        MO "(Let's have a little fun)"

        scene scene_55-5 with Dissolve (1.0)

        MO "eemmm *lick*"

        MO "(He will love it.. Waking up to me tasting his big hard cock)"

        scene scene_55-6 with Dissolve (1.0)

        MO "*Lick* *lick*"

        window hide

        scene scene_55-5 with Dissolve (0.5)
        scene scene_55-6 with Dissolve (0.5)
        scene scene_55-5 with Dissolve (0.5)
        scene scene_55-6 with Dissolve (0.5)
        scene scene_55-5 with Dissolve (0.5)
        scene scene_55-6 with Dissolve (0.5)
        scene scene_55-5 with Dissolve (0.5)
        scene scene_55-6 with Dissolve (0.5)

        MO "(He needs to be treated even better. I know what I have to do)"

        scene scene_55-7 with Dissolve (1.0)

        MO "*Ukhh*"

        scene scene_55-8 with Dissolve (1.0)

        MO "ummm...mmhmmm.."

        MO "(I can't even fit the whole thing)"

        window hide

        scene scene_55-7 with Dissolve (0.5)
        scene scene_55-8 with Dissolve (0.5)
        scene scene_55-7 with Dissolve (0.5)
        scene scene_55-8 with Dissolve (0.5)
        scene scene_55-7 with Dissolve (0.5)
        scene scene_55-8 with Dissolve (0.5)
        scene scene_55-7 with Dissolve (0.5)
        scene scene_55-8 with Dissolve (0.5)

        scene scene_55-9 with Dissolve (1.0)

        A "Uhh Rachel!"

        A "What are you doing?"

        A "Adam's still at home!"

        scene scene_55-10 with Dissolve (1.0)

        MO "Shush.. Let me take care of you. Adam won't wake up just yet.."

        MO "I want you so bad baby.."

        A "Oh Rachel..."

        window hide

        scene scene_55-7 with Dissolve (0.5)
        scene scene_55-8 with Dissolve (0.5)
        scene scene_55-7 with Dissolve (0.5)
        scene scene_55-8 with Dissolve (0.5)
        scene scene_55-7 with Dissolve (0.5)
        scene scene_55-8 with Dissolve (0.5)
        scene scene_55-7 with Dissolve (0.5)
        scene scene_55-8 with Dissolve (0.5)

        A "OH FUCK!!!"

        scene scene_55-11 with Dissolve (1.0)

        MO "Do you want to be inside me [player_name]?"

        A "Yes Rachel...yes.."

        scene scene_55-12 with Dissolve (1.0)

        MO "Uuhh..."

        A "ahhmm.. so warm..."

        scene scene_55-13 with Dissolve (1.0)

        A "You have such beautiful breasts Rachel.. mmmhmmm.."

        MO "Oh [player_name]..my baby.."

        scene scene_55-14 with Dissolve (1.0)

        MO "You are soooo biggg.."

        A "Rachel..."

        scene scene_55-15 with Dissolve (1.0)

        A "Oh yess.. ahhh...mmmm... Rachel..."

        MO "AAhhh.."

        window hide

        scene scene_55-14 with Dissolve (0.5)
        scene scene_55-15 with Dissolve (0.5)
        scene scene_55-14 with Dissolve (0.5)
        scene scene_55-15 with Dissolve (0.5)
        scene scene_55-14 with Dissolve (0.5)
        scene scene_55-15 with Dissolve (0.5)
        scene scene_55-14 with Dissolve (0.5)
        scene scene_55-15 with Dissolve (0.5)
        scene scene_55-14 with Dissolve (0.5)
        scene scene_55-15 with Dissolve (0.5)

        MO "hhanngg...mmhmmm...ah ah ha..."

        MO "FUCK ME [player_name]!! FUCK ME HARD!! FUCK ME SO HARD!!"

        window hide

        scene scene_55-16 with Dissolve (1.0)
        scene scene_55-17 with Dissolve (0.5)
        scene scene_55-16 with Dissolve (0.5)
        scene scene_55-17 with Dissolve (0.5)
        scene scene_55-16 with Dissolve (0.5)
        scene scene_55-17 with Dissolve (0.5)
        scene scene_55-16 with Dissolve (0.5)
        scene scene_55-17 with Dissolve (0.5)
        scene scene_55-16 with Dissolve (0.5)
        scene scene_55-17 with Dissolve (0.5)

        MO "OH GOD!! SO GOOD!! YOU ARE FUCKING ME SOOO GOOD!!"

        scene scene_55-18 with Dissolve (1.0)

        A "RACHEL!! I'm gonna cum!!"

        MO "Cum inside me baby.. Give me all of your seeds!! mmhmmm"

        A "AAAHHHH...!!!"

        scene scene_55-19 with Dissolve (1.0)

        with vpunch

        A "aahh.."

        with vpunch

        A "Oh gosh!! Ahhhmmm..."

        MO "[player_name]..!!"

        scene scene_55-20 with Dissolve (1.0)

        MO "haahh haaahh..so much cum.."

        A "Rachel.. Rachel.."

        scene scene_55-21 with Dissolve (1.0)

        MO "My [player_name].. It was so good.. You even came inside me.."

        A "You are amazing Rachel.. This is so wrong but I don't care anymore. I love you and that's all I know.."

        MO "I love you too [player_name].. I love you more than anything.."

        scene scene_55-22 with Dissolve (1.0)

        MO "*mwah*"

        scene scene_55-23 with Dissolve (3.0)

        A "You smell good Rachel.."

        MO "Hehehe.. I'll stay for few more minutes.. I want to enjoy your embrace.."

        A "You are such a lovey dovey, aren't you?"

        MO "More like crazy for the guy next door.."

        A "You make it sound more sexy.."

        MO "Honey don't forget to wear your underwear. You forgot to wear it after taking it off last night.."

        A "Wait! How did you....?"

        MO "Hahah I have seen you watching porn so many times.."

        A "Ahh...Rachel.."

        MO "It's alright. How about we watch it together tonight?"

        A "Sounds like a plan. I'll download something spicy."

        MO "Can't wait to have fun heheh.."

        A "I better go and put something on.."

        MO "Sure honey.."

        scene scene_55-24 with Dissolve (3.0)

        DA "WHERE THE FUCK WERE YOU?!"

        DA "FUCKING SOME STREET DOG ALL NIGHT, WERE YOU?!"

        MO "Oh god Adam. Lower your voice. [player_name] is sleeping. He will hear you."

        DA "Let that prick hear. You have been trying to get his dick. Did you think I won't find out?!"

        MO "What are you talking about?!"

        MO "Have you gone mad?!"

        DA "DON'T YOU TRY TO FOOL ME YOU LITTLE BITCH!! I'VE SEEN THE WAY YOU LOOK AT HIM!"

        MO "OH so are we completely going to ignore how you have been trying so hard to get Veronica back?!

            SHE DOESN'T EVEN GIVE A SHIT ABOUT YOU!"

        "*SMACK* *SMACK*"

        MO "OH Nooo...stop... no..."

        "*crying*"

        scene scene_55-25 with Dissolve (3.0)

        MO "*sniff* *sniff*"

        MO "[player_name]..[player_name]..[player_name].."

        A "Uhh Rachel, let me sleep!"

        scene blackscreen with Dissolve (1.0)


    $ door6 = True

    jump doorhouse6




    # Scene 56

    # Door 7

    $ door7 = False


label door7:

    scene scene_56-1 with Dissolve (1.0)

    DA "Huh..?"

    DA "Rachel...??"

    scene scene_56-2 with Dissolve (1.0)

    DA "What is she doing here? Lileva..!!"

    scene scene_56-3 with Dissolve (1.0)

    DA "Rachel..!!"

    DA "(You little bitch.. Now I understand. Lileva is in my side. She showed me all the truth and wants me take revenge on you)"

    DA "(I'm going to fucking rape you and then kill you like a pig)"

    DA "Rachel.. Honey.."

    scene scene_56-4 with Dissolve (1.0)

    with hpunch

    DA "OH GOD!!"

    scene scene_56-5 with Dissolve (1.0)

    DA "WHAT THE FUCK ARE YOU?!!"

    MO "ADAM!! HELP ME ADAM!! SHE IS GOING TO KILL ME!!"

    DA "WHAT?!"

    DA "LILEVA!! LILEVA!! WHAT'S GOING ON?!!!"

    scene scene_56-6 with Dissolve (2.0)

    DG "So here I am.. Adam.."

    DA "WHAT THE FUCK!!!"

    DA "I WANT TO LEAVE!! GET ME OUT OF HERE!! SOMEBODY HELP!!"

    scene scene_56-7 with Dissolve (1.0)

    DG "YOU ARE IN MY WORLD ADAM!! AND I HAVE SOME WORK FOR YOU!!"

    MO "ADAM.."

    DA "NO NO NO!!"

    DG "AHAHAHA....!!"

    scene blackscreen with Dissolve (1.0)

    $ dad_journey_todark = True

    jump alanveronicabed


    # Scene 57


    # Alan wake up to Veronica scene

label alanveronicabed:

    scene scene_57-1 with Dissolve (3.0)

    A "hahhh... mmmhmm... I slept like a baby."

    A "What a good morning this is!"

    A "Wait! Why am I in [Mom_name]'s room?"

    A "And who is.."

    scene scene_57-2 with Dissolve (1.0)

    with hpunch

    A "Haaah... *gulp*"

    A "Ve... Ve..."

    scene scene_57-3 with Dissolve (1.0)

    A "(WHAT THE FUCK!! WHAT IS SHE DOING HERE! AND NAKED!!)"

    scene scene_57-4 with Dissolve (1.0)

    with vpunch

    A "(WHAT THE!! EVEN I'M NAKED!! WHAT HAPPENED HERE LAST NIGHT??! WHY CAN'T I REMEMBER ANYTHING?!)"

    A "(Veronica....)"

    scene scene_57-5 with Dissolve (1.0):

        subpixel True
        xalign 0.0
        linear 7.0 xalign 1.0

    A "(What a beautiful curvy body! I have never seen such a pretty woman before!)"

    A "(I'm getting hard just by looking at her body!)"

    with vpunch

    A "(What the fuck am I thinking?! This is bad. I need to leave!)"


    scene scene_57-6 with Dissolve (1.0)

    A "(Time to get the fuck out of here)"


    # Scene 58

    # Lilith First scene

    scene scene_58-1 with Dissolve (3.0)

    pause

    scene scene_58-2 with Dissolve (1.0)

    pause

    scene scene_58-3 with Dissolve (1.0)

    pause

    scene scene_58-4 with Dissolve (1.0)

    pause

    scene scene_58-5 with Dissolve (1.0)

    pause

    scene scene_58-6 with Dissolve (1.0)

    pause

    scene scene_58-7 with Dissolve (1.0)

    L "Let's see what they were upto.."

    scene scene_58-8 with Dissolve (1.0)

    L "mmm...hhmmm..mmhmm.."

    M "YES YES YES!!! OH GOD!! SUCK ME GOOD ELLA!!"

    scene scene_58-9 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:

        L "mmmh..ahhh... Mom... Sis... I want to be there with you.. mhmmm..."

    if not renpy.loadable("patch.rpy"):

        L "mmmh..ahhh... Maddy... Ella... I want to be there with you.. mhmmm..."


    scene scene_58-10 with Dissolve (1.0)

    M "I'M CUMMING BABY!!! GOOOD!!!"

    L "Uhhhunngg..."

    scene blackscreen with Dissolve (1.0)

    pause

    scene scene_58-11 with Dissolve (1.0)

    A "(I need to take a shower.. I smell like a sweaty bum..)"

    A "(But did I have sex with Veronica?! Why can't I remember anything?! NONSENSE!!)"

    "*Door bell rings*"

    A "(Is it [Dad_name]? He is supposed to be at work now.)"

    scene alanroomday with dissolve

    call screen alanroom



    # Scene 59

    # Selina Alan kitchen Scene (Write about taking breakfast before shower)


    $ selina_alan_veronica_kitchen = False


label selinaalanveronicakitchen:

    scene scene_59-1 with Dissolve (1.0)

    A "Oh Selina.. Come in."

    scene scene_59-2 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:

        S "Is mom here? She was supposed to come home right after dropping you here.
           I had to stay all alone the whole night."

        A "Uhh ye yes.. She is sleeping I guess."

        S "In your Dad's room?"

        A "Ah yes.."

        S "Is your dad home or has he left for work already?"

        A "No he isn't here."

        S "Oh.. Since mom is sleeping, I'm guessing that you didn't have breakfast yet. You can't even cook."

        A "Uhh.."

    if not renpy.loadable("patch.rpy"):

        S "Is Veronica here? She was supposed to come home right after dropping you here.
           I had to stay all alone the whole night."

        A "Uhh ye yes.. She is sleeping I guess."

        S "In Adam's room?"

        A "Ah yes.."

        S "Is Adam at home or has he left for work already?"

        A "No he isn't here."

        S "Oh.. Since Veronica is sleeping, I'm guessing that you didn't have breakfast yet. You can't even cook."

        A "Uhh.."


    S "Come with me. I need help."

    scene scene_59-3 with Dissolve (1.0)

    A "Wait Selina. You don't have to make anything. I can order some food."

    S "Shut up and help me out."

    A "Uhh.."

    scene scene_59-4 with Dissolve (3.0)

    S "Ahh done. Now where did you put the forks and spoons?"

    A "Selina.. Are you doing okay?"

    scene scene_59-5 with Dissolve (1.0)

    S "huh? What's with such weird question?"

    A "Yesterday.. You know.."


    if alanforceselina == "no":

        S "Yes I'm doing fine [player_name]. I loved how you embraced me.
           It really meant a lot to me. Thank you [player_name]."

        A "Anything for you Selina. You are the closest person to me and I care about you."


    if alanforceselina == "yes":


        if alankisshospital == "yes":

            S "Umm yes [player_name]. I'm doing much better.
               You've surprised me but I'm glad that you did it.
               Quite the fashion to steal my first kiss, huh?"

            A "Uhh..."


            S "Thank you [player_name]."

            A "Anything for you Selina."


        if alankisshospital == "no":

            S "Yes I'm doing okay [player_name]. Don't worry about it.
               We will talk about it later."

            A "Uhh okay Selina."


    V "[player_name].."

    A "(SHIT!!)"

    scene scene_59-6 with Dissolve (1.0)

    A "Ahh yes Veronica.."

    A "Are you alright? You don't look too good.."

    if renpy.loadable("patch.rpy") or patch:

        S "What's wrong mom?"

        scene scene_59-7 with Dissolve (1.0)

        V "[player_name], where is your dad?"

        A "He is at work I guess."

        V "No he isn't. He left his phone here. I've called his workplace. And they've said that he didn't come to work today."

        A "That's strange."

        scene scene_59-6 with Dissolve (1.0)

        V "I feel worried. I have a severe headache and don't remember anything that happened last night."

        S "Mom. This looks serious. We should call a doctor."

        V "No it's alright. I'll go home and take a shower."

        A "You don't have to leave. You can use our bathroom. You'll find spare clothes there as well."

        scene scene_59-7 with Dissolve (1.0)

        V "It's alright. I don't want to be a burden right now. You just got back from hospital.
           The last thing I would want is to add to it."

        A "I insist Veronica. Selina even made breakfast for us. Take a shower and let's have breakfast together."

        A "And don't worry about [Dad_name]. If he isn't at work then he must have went to the park to exercise or something."

        V "I hope you are right [player_name]. I'll be quick.
           Don't want the food to get cold."

        A "Take your time Veronica."

        S "Yes mom."

        scene scene_59-8 with Dissolve (1.0)

        A "(Strange! Where is dad now? Something must have happened last night.
           With all that's going on, I won't even be surprised if something did happen.)"

        S "You didn't take shower as well, did you?"

        S "I can smell from you here."

        A "Uh oh!"

        scene scene_59-9 with Dissolve (1.0)

        S "Seriously [player_name]? I made all of these and you didn't even bother to let me know that you didn't shower yet."

        A "Well you didn't even ask. So.."

        S "I'll have to reheat the food just because of you."

        A "Don't worry. I'll take a quick shower."

        S "You only have one bathroom. Do you plan on taking a shower with mom now?!"

        A "Uhh..."

        A "I'll just go.."

        scene scene_59-10 with Dissolve (1.0)

        S "Be quick!"

        A "All right. All right."



    if not renpy.loadable("patch.rpy"):

        S "What's wrong Veronica?"

        scene scene_59-7 with Dissolve (1.0)

        V "[player_name], where is Adam?"

        A "He is at work I guess."

        V "No he isn't. He left his phone here. I've called his workplace. And they've said that he didn't come to work today."

        A "That's strange."

        scene scene_59-6 with Dissolve (1.0)

        V "I feel worried. I have a severe headache and don't remember anything that happened last night."

        S "Veronica. This looks serious. We should call a doctor."

        V "No it's alright. I'll go home and take a shower."

        A "You don't have to leave. You can use our bathroom. You'll find spare clothes there as well."

        scene scene_59-7 with Dissolve (1.0)

        V "It's alright. I don't want to be a burden right now. You just got back from hospital.
           The last thing I would want is to add to it."

        A "I insist Veronica. Selina even made breakfast for us. Take a shower and let's have breakfast together."

        A "And don't worry about [Dad_name]. If he isn't at work then he must have went to the park to exercise or something."

        V "I hope you are right [player_name]. I'll be quick.
           Don't want the food to get cold."

        A "Take your time Veronica."

        S "Yes Veronica."

        scene scene_59-8 with Dissolve (1.0)

        A "(Strange! Where is Adam now? Something must have happened last night.
           With all that's going on, I won't even be surprised if something did happen.)"

        S "You didn't take shower as well, did you?"

        S "I can smell from you here."

        A "Uh oh!"

        scene scene_59-9 with Dissolve (1.0)

        S "Seriously [player_name]? I made all of these and you didn't even bother to let me know that you didn't shower yet."

        A "Well you didn't even ask. So.."

        S "I'll have to reheat the food just because of you."

        A "Don't worry. I'll take a quick shower."

        S "You only have one bathroom. Do you plan on taking a shower with Veronica now?!"

        A "Uhh..."

        A "I'll just go.."

        scene scene_59-10 with Dissolve (1.0)

        S "Be quick!"

        A "All right. All right."


    scene alanroomday with dissolve

    A "(I wonder if Veronica is done with the shower. This smell is killing me.
       How did I even manage to sweat this much? Yuck)"

    $ selina_alan_veronica_kitchen = True

    call screen alanroom


    # Scene 60

    # Veronica shower scene


    $ veronica_shower_scene_1 = False


label veronicashowerscene1:


    scene scene_60-1 with Dissolve (1.0)

    "*shower on*"

    scene scene_60-2 with Dissolve (1.0)

    pause

    scene scene_60-3 with Dissolve (1.0)

    A "(I don't hear the shower running. I guess she isn't here)"

    "*Door opens slowly*"

    with hpunch

    A "(...!!!)"

    scene scene_60-4 with Dissolve (1.0)

    V "ungghhh...ukk..."

    scene scene_60-5 with Dissolve (1.0)

    A "(WHAT THE FUCK?!!)"

    A "(OH MY GOD!! SHE..SHE..SHE..!!)"

    scene scene_60-6 with Dissolve (1.0)

    V "uumm...mmh...ah..ah..."

    scene scene_60-7 with Dissolve (0.5)
    scene scene_60-6 with Dissolve (0.5)
    scene scene_60-7 with Dissolve (0.5)
    scene scene_60-6 with Dissolve (0.5)
    scene scene_60-7 with Dissolve (0.5)
    scene scene_60-6 with Dissolve (0.5)
    scene scene_60-7 with Dissolve (0.5)
    scene scene_60-6 with Dissolve (0.5)

    V "OH GOD..!!"

    V "[player_name]...!!!!"

    scene scene_60-8

    with vpunch

    V "GOD..!! Ahhhh..."

    scene scene_60-5 with Dissolve (1.0)

    A "(FUCK!! SHE JUST SHOUTED MY NAME!! SHE WAS THINKING ABOUT ME!!
       WHY?!!)"

    A "(Can't stay here anymore. Too risky. Time to leave.)"

    scene scene_60-9 with Dissolve (1.0)

    "*crank*"

    "*Door closes*"

    scene scene_60-10 with Dissolve (1.0)

    V "Huh?!"

    scene blackscreen with dissolve

    pause

    $ veronica_shower_scene_1 = True

    jump ellablackmail

    # Scene 61

    # Ella blackmail freakout scene


label ellablackmail:

    scene scene_61-1 with Dissolve (1.0)

    "*You have recieved a new text message*"

    E "..."

    scene scene_61-2 with Dissolve (1.0)

    E "Uhhhh....!!!"

    with vpunch

    E "NO NO NO NO.....!!!!"

    scene scene_61-3 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:

        E "MOM!!! MOM!! COME HERE RIGHT NOW!! HURRY!!"

    if not renpy.loadable("patch.rpy"):

        E "MADDY!!! MADDY!! COME HERE RIGHT NOW!! HURRY!!"

    scene scene_61-4 with Dissolve (1.0)

    E "NO NO NO NO... OH GOD...!!!"

    scene scene_61-5 with Dissolve (1.0)

    M "What happened? I've been waiting for you in the tub.."

    scene scene_61-6 with Dissolve (1.0)

    E "Take a look.. GOD!!!"

    scene scene_61-7

    with vpunch

    M "HUH?!! WHAT THE??!!"

    scene scene_61-8 with Dissolve (1.0)

    M "WHAT THE FUCK IS THIS?!! SOMEONE SHOT OUR VIDEO??!!"

    if renpy.loadable("patch.rpy") or patch:

        E "MOM..!! THIS IS BAD!!"

        E "Whoever it is, was here. He set a camera there on that desk."

        M "He isn't asking for money. I don't see anything else other than this clip."

        scene scene_61-9 with Dissolve (1.0)

        E "What are we going to do mom?! This is going to ruin us!"

        M "Ella... Baby.."

        E "What if he publishes everything on the internet?!
           What if everyone finds out everything that we have done?!!"

        E "MOM!!"


        scene scene_61-10 with Dissolve (1.0)

        M "Baby don't worry. Mom will fix everything.
           No one will ruin us."

        scene scene_61-11 with Dissolve (1.0)

        E "What if he sends this to [player_name]?!
           [player_name] will hate me for cheating on him. OH GOD!!
           NO!! NO!!"

        scene scene_61-12 with Dissolve (1.0)

        M "Baby don't worry. Look.. Mom is here with you. Nothing will get released."

        E "How mom?"

        M "If I'm not wrong, few days ago you had a carpenter fix your sofa."

        E "OH GOD! YES!"

        M "Well then we have a lead.. Don't worry. I'll have my men look into this."

        E "Mom.."

        scene scene_61-13 with Dissolve (1.0)

        M "*mwah*"

        scene scene_61-14 with Dissolve (1.0)

        M "I won't let anyone harm my baby.."

        E "Mom you are the best.."

        M "Sure I am."

        M "Now let's go take a bath together."

        E "Okay mom.."

        scene blackscreen with dissolve

        pause


    if not renpy.loadable("patch.rpy"):

        E "MADDY..!! THIS IS BAD!!"

        E "Whoever it is, was here. He set a camera there on that desk."

        M "He isn't asking for money. I don't see anything else other than this clip."

        scene scene_61-9 with Dissolve (1.0)

        E "What are we going to do Maddy?! This is going to ruin us!"

        M "Ella... Baby.."

        E "What if he publishes everything on the internet?!
           What if everyone finds out everything that we have done?!!"

        E "MADDY!!"


        scene scene_61-10 with Dissolve (1.0)

        M "Baby don't worry. I will fix everything.
           No one will ruin us."

        scene scene_61-11 with Dissolve (1.0)

        E "What if he sends this to [player_name]?!
           [player_name] will hate me for cheating on him. OH GOD!!
           NO!! NO!!"

        scene scene_61-12 with Dissolve (1.0)

        M "Baby don't worry. Look.. I'm here with you. Nothing will get released."

        E "How Madison?"

        M "If I'm not wrong, few days ago you had a carpenter fix your sofa."

        E "OH GOD! YES!"

        M "Well then we have a lead.. Don't worry. I'll have my men look into this."

        E "Maddy.."

        scene scene_61-13 with Dissolve (1.0)

        M "*mwah*"

        scene scene_61-14 with Dissolve (1.0)

        M "I won't let anyone harm my baby.."

        E "Maddy you are the best.."

        M "Sure I am."

        M "Now let's go take a bath together."

        E "Okay Maddy.."

        scene blackscreen with dissolve

        pause


    jump madisonlilithscene1



    # Scene 62

    # Madison Lilith Scene


label madisonlilithscene1:

    scene scene_62-1 with Dissolve (1.0)

    "*crank*"

    "*Door opens*"

    scene scene_62-2 with Dissolve (1.0)

    M "Lilly.. Lilly.."

    M "This girl.. Always on her laptop.. Lilly.."

    scene scene_62-3 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:

        L "Mom! How many times do I have to tell you that my name is Lilith?!"

        M "I don't remember giving you such devlish name. And what did you do to that beautiful blond hair of yours?"


    if not renpy.loadable("patch.rpy"):

        L "Madison! How many times do I have to tell you that my name is Lilith?!"

        M "Such a devlish name. What did you do to that beautiful blond hair of yours?"

    L "My name is Lilith. That's it! And I really like my hair. Now. Why are you here?"

    scene scene_62-4 with Dissolve (1.0)

    M "Oh dear lord.. Whatever. I'm going to the mall. Heard the new store has a good collection of designer dresses."

    M "Do you want to come with me?"

    scene scene_62-5 with Dissolve (1.0)

    L "OMG! You should have said this first. I'm on board.
       Give me 5 minutes!"

    M "Be quick honey.."

    scene blackscreen with dissolve

    pause

    scene scene_62-6 with Dissolve (1.0)

    pause

    scene scene_62-7 with Dissolve (1.0)

    M "So do you like your new dresses?
       A bit expensive but really good product."

    scene scene_62-8 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:

        L "I love them!! Thank you so much mom..
           You are the best.."

        M "You don't have to thank me honey. You are my daughter and my daughter deserves the best thing in the world."


    if not renpy.loadable("patch.rpy"):

        L "I love them!! Thank you so much Madison..
           You are the best.."

        M "You don't have to thank me honey. You deserve the best thing in the world."


    scene scene_62-9 with Dissolve (1.0)

    M "So uhh.. Lill.. Lilith.. Do you know the address of the carpenter that came a few days ago?

       I'm planning on getting a new shelf for my room. And he is really good at what he does."

    L "uh... uh.. Yes I know. It's not far from here.."

    scene scene_62-10 with Dissolve (1.0)

    M "Is this the one?"

    L "Yep..!"

    scene scene_62-11 with Dissolve (1.0)

    M "Are you here?"

    M "Yes.. I have parked outside."

    M "Make it loud. I want to hear him scream."

    L "What?"

    M "Don't worry about them. Just don't leave a trace."

    scene scene_62-12 with Dissolve (1.0)

    L "WHAT'S GOING ON?!!"

    scene scene_62-13 with Dissolve (1.0)

    M "You know what honey.. This man did something really really bad.
       He set a camera in Ella's room and recorded something he isn't supposed to."

    L "YOU HAVE JUST ORDERED YOUR MAN TO KILL HIM!!"

    M "Yes I did."

    L "ARE YOU CRAZY?!"

    M "SShhuuushh... Sit and enjoy the show.."

    L "This can't be happening!"

    M "He deserves it honey. Nobody messes with us!"

    L "This is a crime!"

    M "Do you think I care?"

    scene scene_62-14 with Dissolve (1.0)

    L "*sniff* *sniff* Okay okay.. It was me!!"

    M "What do you mean?"

    L "It was me who set the camera. I sent her the message!
       I just wanted to have a little fun."

    M "What?!"


    if renpy.loadable("patch.rpy") or patch:
        L "That man didn't do anything! He is innocent! Please tell your man to stop!!
           MOM!!"

        scene scene_62-15 with Dissolve (1.0)

        M "Oh Lilly Lilly... My silly little girl..
           I know it was you.."

        L "What?!!"


    if not renpy.loadable("patch.rpy"):
        L "That man didn't do anything! He is innocent! Please tell your man to stop!!
           MADDY!!"

        scene scene_62-15 with Dissolve (1.0)

        M "Oh Lilly Lilly... Silly little girl..
           I know it was you.."

        L "What?!!"

    scene scene_62-16 with Dissolve (1.0)

    M "KILL HIM!"

    L "WHAT THE FUCK?!!"

    with hpunch

    "*gunshot*"

    "*Loud scream*"

    with hpunch

    "*gunshot*"

    "*People screaming*"

    M "Well done.. Now leave.."

    scene scene_62-17 with Dissolve (1.0)

    L "WHY WHY WHY?!! WHY DID YOU JUST KILL AN INNOCENT PERSON?!!"

    L "HOW COULD YOU?!!"

    L "I've just told you it was me!"

    if renpy.loadable("patch.rpy") or patch:

        M "He was staring at my Ella's big beautiful butt.
           No one stares at my daughter."

        scene scene_62-18 with Dissolve (1.0)

        L "WHAT?! JUST FOR STARING AT HER?!! YOU ARE A MONSTER!!"

        M "Took you long enough to realise honey.. Don't cry. I won't harm you.
           You are my daughter and I love you as much as I love Ella and Becky.
           If you want a part in our little fun party, you can always join."


    if not renpy.loadable("patch.rpy"):

        M "He was staring at my Ella's big beautiful butt.
           No one stares at her."

        scene scene_62-18 with Dissolve (1.0)

        L "WHAT?! JUST FOR STARING AT HER?!! YOU ARE A MONSTER!!"

        M "Took you long enough to realise honey.. Don't cry. I won't harm you.
           I love you as much as I love Ella and Becky.
           If you want a part in our little fun party, you can always join."

    L "...."


    M "I love you lilith.."

    scene scene_62-19 with Dissolve (1.0)

    M "*mwah*"

    scene blackscreen with dissolve

    pause

    scene alanroomday with dissolve

    A "(I'll take the shower after breakfast. Selina will get mad at me if I don't hurry)"

    call screen alanroom


    $ alan_selina_veronica_breakfast_1 = False


    # Scene 63

    # Alan shower and Selina entry also breakfast scene


label alanselinaveronicabreakfast1:


    scene scene_63-1 with Dissolve (1.0)

    A "(She looks exhausted and tired)"

    scene scene_63-2 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:

        S "Mom, don't be so sad. You are worrying for nothing."

    if not renpy.loadable("patch.rpy"):

        S "Veronica, don't be so sad. You are worrying for nothing."

    A "What's going on?"

    scene scene_63-3 with Dissolve (1.0)

    S "She is worried about Adam."

    A "Don't worry Veronica. I'm sure he is fine."

    V "I have called some of his friends. None of them know where he is."

    A "Ah.."

    V "We've just got back together and he's already gone missing. I just can't wrap my head around it."

    A "Maybe he is stuck in some kind of work. Let's wait a bit Veronica."

    V "Okay [player_name].."

    scene blackscreen with dissolve

    pause

    scene scene_63-4 with Dissolve (1.0)

    V "Thank for letting me stay [player_name]. And thanks for the food Selina.
       You two have really grown up."

    A "Yes thank you Selina. You'll make a really good wife one day."

    scene scene_63-5 with Dissolve (1.0)

    S "Stop pulling my legs you two."

    A "I'll go for now. See you guys later. Need to take a shower.."

    S "...."

    scene blackscreen with dissolve

    pause

    scene scene_63-6 with Dissolve (1.0)

    A "(Again everything is so messed up. Where is [Dad_name]?
       What happened last night? Why was Veronica masturbating while thinking about me?
       GOD!)"

    A "(My head hurts)"

    scene scene_63-7 with Dissolve (1.0)

    pause

    scene scene_63-8 with Dissolve (1.0)

    A "(A nice shower can help)"

    scene scene_63-9 with Dissolve (1.0)

    pause

    scene scene_63-10 with Dissolve (1.0)

    pause

    scene scene_63-11 with Dissolve (1.0)

    pause

    scene scene_63-12 with Dissolve (1.0)

    pause

    scene scene_63-13 with Dissolve (1.0)

    A "(That photo. Police showed me a photo. That girl.. I have seen that girl..
       I...)"

    A "(I..I..I remember...)"

    scene white with dissolve
    $ renpy.pause(0.7, hard = True)

    jump veronicafirstsex




    # Scene 64


    # Veronica first sex scene


label veronicafirstsex:


    scene scene_64-1 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:

        A "Da...Daaad...DAD!!!"

        A "NOOOOO!!!"

        scene scene_64-2 with Dissolve (1.0)

        "*Veronica crying*"

        V "Adam...no..no.."

        scene scene_64-3 with Dissolve (1.0)

        D "Why are you crying daddy?"

        D "It's what you wanted. You wanted to kill him. I did that job instead of you."

        D "Your hands are clean. You need those clean hands to touch us both.."

        A "WHAT?!"

        D "Forget him daddy."

        D "Now.. Now.. Let's have sex.. WOHOO!!"

        A "STAY AWAY!!"

        scene scene_64-4 with Dissolve (1.0)

        A "YOU ARE A MONSTER!! JUST LIKE THAT LILEVA!! LEAVE US ALONE!!"

        D "What are you saying daddy? I'm your sweet little girl. I'm not a monster."

        V "What's she saying?!"

        A "Don't listen to her Veronica. She is a monster. They took mom. Now they want us.
           Aunt has warned me."

        D "But I just want your cock. Mommy said you have a really big cock.
           I can't be strong if you don't take my virginity daddy.
           Hurry.. hurry. Let's have sex."

        A "STAY THE FUCK AWAY!!! ONE MORE STEP AND I'LL KILL YOU!!"

        scene scene_64-5 with Dissolve (1.0)

        D "You are so rude daddy. Why are you getting angry at your daughter?"

        scene scene_64-6 with Dissolve (1.0)

        A "You are not my daughter. You are a monster. What did you do to mom?
           Bring her back!!"

        scene scene_64-7 with Dissolve (1.0)

        with vpunch


    if not renpy.loadable("patch.rpy"):

        A "Ad...Adaaam...ADAM!!!"

        A "NOOOOO!!!"

        scene scene_64-2 with Dissolve (1.0)

        "*Veronica crying*"

        V "Adam...no..no.."

        scene scene_64-3 with Dissolve (1.0)

        D "Why are you crying [player_name]?"

        D "It's what you wanted. You wanted to kill him. I did that job instead of you."

        D "Your hands are clean. You need those clean hands to touch us both.."

        A "WHAT?!"

        D "Forget him."

        D "Now.. Now.. Let's have sex.. WOHOO!!"

        A "STAY AWAY!!"

        scene scene_64-4 with Dissolve (1.0)

        A "YOU ARE A MONSTER!! JUST LIKE THAT LILEVA!! LEAVE US ALONE!!"

        D "What are you saying [player_name]? I'm just a sweet little girl. I'm not a monster."

        V "What's she saying?!"

        A "Don't listen to her Veronica. She is a monster. They took Rachel. Now they want us.
           Diana has warned me."

        D "But I just want your cock. Rachel said you have a really big cock.
           I can't be strong if you don't take my virginity.
           Hurry.. hurry. Let's have sex."

        A "STAY THE FUCK AWAY!!! ONE MORE STEP AND I'LL KILL YOU!!"

        scene scene_64-5 with Dissolve (1.0)

        D "You are so rude . Why are you getting angry at me?"

        scene scene_64-6 with Dissolve (1.0)

        A "You are a monster! What did you do to Rachel?!
           Bring her back!!"

        scene scene_64-7 with Dissolve (1.0)

        with vpunch


    D "THAT'S ENOUGH!!!"

    V "[player_name]!!"

    D "You've gone too far!!"

    D "I didn't want to do this but I'm going to show you how it feels to be so vulnerable!!"

    scene scene_64-8 with Dissolve (1.0)

    D "REVERSEUS!!"

    scene white with dissolve
    $ renpy.pause(0.7, hard = True)

    scene scene_64-9 with Dissolve (3.0)

    V "Now it's better. Not too bright, not totally dark.
       Enough light.."

    A "You are so gorgeous Veronica."

    scene scene_64-10 with Dissolve (1.0)

    V "And what do you plan on doing to this gorgeous lady?"

    A "Let's find out together.."

    V "I feel so horny and helpless right now. I can't stop thinking about you.
       The thought of you thrusting me harder and harder just melts my body.."

    A "How much do you want me right now?"

    V "I want you so bad. I've been dying to get your touch [player_name]!"

    V "[player_name].."

    scene scene_64-11 with Dissolve (1.0)

    V "*mwah* mmhmmm.."

    A "mmmhmmm..mmm..."

    scene scene_64-12 with Dissolve (1.0)

    V "*lick* mhmmm... hmphh.."

    A "Veronica....mmhmmmm..."

    scene scene_64-13 with Dissolve (1.0)

    V "You are such a good kisser [player_name].."

    A "You too baby.."

    V "Already down the baby road, huh? Hehehe.."

    V "But the real baby here is already a grown up.."

    scene scene_64-14 with Dissolve (1.0)

    A "mmhmm..."

    V "SO BIG!! You're so big [player_name]..!!"

    A "Do you like him?"

    scene scene_64-15 with Dissolve (1.0)

    V "Are you kidding? I LOVE HIM!"

    V "Now enough of chit chat.. Let's make this night special.."

    scene scene_64-16 with Dissolve (1.0)

    V "Come with me.."

    A "Oh baby.. You have such a beautiful ass.."

    V "Heheh.. Be a good boy and you'll get to do whatever you want.."

    scene scene_64-17 with Dissolve (1.0)

    V "Do you like what you see [player_name]?"

    A "You are killing me Veronica.."

    A "He's just getting harder harder. He will burst if you don't touch him.."

    scene scene_64-18 with Dissolve (1.0)

    V "Now now.. We can't let that happen, can we?"

    A "That's what I'm saying.."

    V "Aahh naughty.."

    scene scene_64-19 with Dissolve (1.0)

    V "GOSH!! I've been waiting for this moment.."

    A "Can't wait to see what you are gonna do.."

    V "Just watch and enjoy hehe.."


    # Veronica blowjob default


    scene scene_64-20 with Dissolve (1.0)

    V "*mwah* mmm.."

    A "uff..."

    scene scene_64-21 with Dissolve (1.0)

    V "*lick* *lick*"

    A "Oh god...!!"

    scene scene_64-22 with Dissolve (1.0)

    V "*lick*"

    V "ahhmmmm hehehe..."


    scene scene_64-21 with Dissolve (1.0)
    scene scene_64-22 with Dissolve (0.5)
    scene scene_64-21 with Dissolve (0.5)
    scene scene_64-22 with Dissolve (0.5)


    scene scene_64-23 with Dissolve (0.5)
    scene scene_64-24 with Dissolve (0.5)
    scene scene_64-23 with Dissolve (0.5)
    scene scene_64-24 with Dissolve (0.5)


    scene scene_64-21 with Dissolve (0.5)
    scene scene_64-22 with Dissolve (0.5)
    scene scene_64-21 with Dissolve (0.5)
    scene scene_64-22 with Dissolve (0.5)

    A "Ahhh....mmmm...Veronica..mhmm.. Stop teasing me.."

    V "Hehehhe..."

    scene scene_64-25 with Dissolve (1.0)

    A "Oh yes baby...uuhmm.."

    scene scene_64-26 with Dissolve (1.0)

    V "*gulp*"

    scene scene_64-25 with Dissolve (1.0)

    V "uhhmmm...ukkhh..."

    A "Keep going baby..."

    scene scene_64-26 with Dissolve (1.0)
    scene scene_64-25 with Dissolve (0.5)
    scene scene_64-26 with Dissolve (0.5)
    scene scene_64-25 with Dissolve (0.5)
    scene scene_64-26 with Dissolve (0.5)
    scene scene_64-25 with Dissolve (0.5)
    scene scene_64-26 with Dissolve (0.5)

    scene scene_64-26 with Dissolve (0.5)
    scene scene_64-25 with Dissolve (0.5)

    scene scene_64-23 with Dissolve (0.5)
    scene scene_64-24 with Dissolve (0.5)
    scene scene_64-23 with Dissolve (0.5)
    scene scene_64-24 with Dissolve (0.5)


    scene scene_64-26 with Dissolve (0.5)
    scene scene_64-25 with Dissolve (0.5)
    scene scene_64-26 with Dissolve (0.5)
    scene scene_64-25 with Dissolve (0.5)


    scene scene_64-21 with Dissolve (0.5)
    scene scene_64-22 with Dissolve (0.5)
    scene scene_64-21 with Dissolve (0.5)
    scene scene_64-22 with Dissolve (0.5)

    scene scene_64-26 with Dissolve (0.5)
    scene scene_64-25 with Dissolve (0.5)
    scene scene_64-26 with Dissolve (0.5)
    scene scene_64-25 with Dissolve (0.5)
    scene scene_64-26 with Dissolve (0.5)
    scene scene_64-25 with Dissolve (0.5)
    scene scene_64-26 with Dissolve (0.5)
    scene scene_64-25 with Dissolve (0.5)


    A "So good...Oh god..huhhhh...mmm...."


    scene scene_64-19 with Dissolve (1.0)

    V "Hehhe now it's your turn.."

    V "What are you going to do to me honey?"


menu:


    "Lick her pussy":

        A "How about a little love for your beautiful pussy."

        V "Uhhmmm yes yes baby.."

        jump veronicapussylickdefault


    "Get a titjob":

        A "Umm will you wrap your big beautiful boobs around me?"

        A "Please?"

        V "Heheh sure honey.."

        jump veronicatitjobdefault


    "Fuck her in missionary":

        A "Let's put you down on the bed..
           I'm gonna make love with you.."

        V "Oh [player_name].."

        jump veronicamissionarydefault


    "Fuck her in doggy":

        A "Be my little bitch.. I'm going to take you from the back.."

        V "Aha naughty and dirty.. But I want to see how you do it.."

        jump veronicadoggydefault


    "Make her your cowgirl":

        A "Get on top of me baby..
           Fuck me like a cowgirl.."

        V "Hahah I'll ride you like a horse.."

        jump veronicacowgirldefault



    # Veronica Titjob


label veronicatitjobdefault:


    scene scene_64-27 with Dissolve (1.0)

    A "They are so big and beautiful Veronica.."

    V "Is that the truth [player_name]?"

    A "Yes baby..  I won't even mind if you smother me with them.."

    scene scene_64-28 with Dissolve (1.0)

    V "Hahah you are so naughty. If you die then who's going to fuck me every day and night.."

    A "God you can be really naughty as well..uuhhmm.."

    V "Hehehe..."

    scene scene_64-29 with Dissolve (1.0)

    V "Uhhh...So hot..."

    A "Oh baby.. GOD!"

    A "Feels so good.."

    jump veronicatitjob1

label veronicatitjob1:

    scene scene_64-30 with Dissolve (1.0)
    scene scene_64-29 with Dissolve (0.5)
    scene scene_64-30 with Dissolve (0.5)
    scene scene_64-29 with Dissolve (0.5)
    scene scene_64-30 with Dissolve (0.5)
    scene scene_64-29 with Dissolve (0.5)
    scene scene_64-30 with Dissolve (0.5)
    scene scene_64-29 with Dissolve (0.5)
    scene scene_64-30 with Dissolve (0.5)

    A "Keep going baby...Keep going...aahh ahhh.."

    scene scene_64-29 with Dissolve (0.5)
    scene scene_64-30 with Dissolve (0.5)
    scene scene_64-29 with Dissolve (0.5)
    scene scene_64-30 with Dissolve (0.5)
    scene scene_64-29 with Dissolve (0.5)
    scene scene_64-30 with Dissolve (0.5)
    scene scene_64-29 with Dissolve (0.5)
    scene scene_64-30 with Dissolve (0.5)

    V "Oh god.. I feel so horny [player_name]..!!"

    scene scene_64-29 with Dissolve (0.5)
    scene scene_64-30 with Dissolve (0.5)
    scene scene_64-29 with Dissolve (0.5)
    scene scene_64-30 with Dissolve (0.5)

    A "Baby.. You are so good at it.."

    scene scene_64-28 with Dissolve (1.0)

    V "Hehehe..."

    V "Now what are we gonna do [player_name]?"



menu veronicafirstsexmenu:

    "Get another blowjob":

        A "Blow me again baby.. Take my big cock in your mouth.."

        V "I love sucking your big cock hehehe.."

        jump veronicablowjob1


    "Lick her pussy":

        A "How about a little love for your beautiful pussy."

        V "Uhhmmm yes yes baby.."

        jump veronicapussylickdefault


    "Get a titjob":

        A "Umm will you fuck me with your tits again?"

        A "Please?"

        V "Heheh sure honey.."

        jump veronicatitjob1


    "Fuck her in missionary":

        A "Let's put you down on the bed..
           I'm gonna make love with you.."

        V "Oh [player_name].."

        jump veronicamissionarydefault


    "Fuck her in doggy":

        A "Be my little bitch.. I'm going to take you from the back.."

        V "Aha naughty and dirty.. But I want to see how you do it.."

        jump veronicadoggydefault


    "Make her your cowgirl":

        A "Get on top of me baby..
           Fuck me like a cowgirl.."

        V "Hahah I'll ride you like a horse.."

        jump veronicacowgirldefault



   # Second blowjob

label veronicablowjob1:

    scene scene_64-21 with Dissolve (1.0)
    scene scene_64-22 with Dissolve (0.5)
    scene scene_64-21 with Dissolve (0.5)
    scene scene_64-22 with Dissolve (0.5)


    scene scene_64-23 with Dissolve (0.5)
    scene scene_64-24 with Dissolve (0.5)
    scene scene_64-23 with Dissolve (0.5)
    scene scene_64-24 with Dissolve (0.5)


    scene scene_64-21 with Dissolve (0.5)
    scene scene_64-22 with Dissolve (0.5)
    scene scene_64-21 with Dissolve (0.5)
    scene scene_64-22 with Dissolve (0.5)

    A "Ahhh....mmmm...Veronica..mhmm.. Stop teasing me.."

    V "Hehehhe..."

    scene scene_64-25 with Dissolve (1.0)

    A "Oh yes baby...uuhmm.."

    scene scene_64-26 with Dissolve (1.0)

    V "*gulp*"

    scene scene_64-25 with Dissolve (1.0)

    V "uhhmmm...ukkhh..."

    A "Keep going baby..."

    scene scene_64-26 with Dissolve (1.0)
    scene scene_64-25 with Dissolve (0.5)
    scene scene_64-26 with Dissolve (0.5)
    scene scene_64-25 with Dissolve (0.5)
    scene scene_64-26 with Dissolve (0.5)
    scene scene_64-25 with Dissolve (0.5)
    scene scene_64-26 with Dissolve (0.5)

    scene scene_64-26 with Dissolve (0.5)
    scene scene_64-25 with Dissolve (0.5)

    scene scene_64-23 with Dissolve (0.5)
    scene scene_64-24 with Dissolve (0.5)
    scene scene_64-23 with Dissolve (0.5)
    scene scene_64-24 with Dissolve (0.5)


    scene scene_64-26 with Dissolve (0.5)
    scene scene_64-25 with Dissolve (0.5)
    scene scene_64-26 with Dissolve (0.5)
    scene scene_64-25 with Dissolve (0.5)


    scene scene_64-21 with Dissolve (0.5)
    scene scene_64-22 with Dissolve (0.5)
    scene scene_64-21 with Dissolve (0.5)
    scene scene_64-22 with Dissolve (0.5)

    scene scene_64-26 with Dissolve (0.5)
    scene scene_64-25 with Dissolve (0.5)
    scene scene_64-26 with Dissolve (0.5)
    scene scene_64-25 with Dissolve (0.5)
    scene scene_64-26 with Dissolve (0.5)
    scene scene_64-25 with Dissolve (0.5)
    scene scene_64-26 with Dissolve (0.5)
    scene scene_64-25 with Dissolve (0.5)


    A "So good...Oh god..huhhhh...mmm...."


    scene scene_64-19 with Dissolve (1.0)

    V "Hehhe now it's your turn.."

    V "What are you going to do to me honey?"

    #call veronicafirstsexmenu from _call_veronicafirstsexmenu

    jump veronicafirstsexmenu

    # Veronica missionary


label veronicamissionarydefault:


    scene scene_64-31 with Dissolve (1.0)

    A "Your pussy looks so cute between your thick butts.."

    V "Hehehe.. So are you going to put your cock in my cute pussy honey?"

    scene scene_64-32 with Dissolve (1.0)

    A "But is she ready for my cock?"

    V "Maybe you need to prepare her for your big boy.."

    A "I know just the perfect way to do it.."

    scene scene_64-33 with Dissolve (1.0)

    V "Heheh now I know where this is going.."

    scene scene_64-34 with Dissolve (1.0)

    V "unggghh..yess slap that bitch.. just like that.."

    scene scene_64-35 with Dissolve (1.0)

    A "You are already so wet baby.."

    V "It because you are teasing me honey.."

    scene scene_64-34 with Dissolve (0.5)
    scene scene_64-35 with Dissolve (0.5)
    scene scene_64-34 with Dissolve (0.5)
    scene scene_64-35 with Dissolve (0.5)
    scene scene_64-34 with Dissolve (0.5)
    scene scene_64-35 with Dissolve (0.5)
    scene scene_64-34 with Dissolve (0.5)
    scene scene_64-35 with Dissolve (0.5)

    V "[player_name] please! I can't wait anymore. FUCK ME [player_name].. Please..!!"

    scene scene_64-36

    with vpunch

    V "OH GOD YESS!!"

    A "Woah it's so hot inside you baby.. uughh.."

    V "Don't stay so far away honey... Get on top of me..
       Touch my body with yours. Let's become one.."

    A "Oh Veronica.."

    scene scene_64-37 with Dissolve (1.0)

    A "I can't believe how beautiful you are Veronica.."

    V "Oh [player_name].. I'm getting restless.. Fuck me please..!!"

    scene scene_64-38 with Dissolve (0.5)
    scene scene_64-37 with Dissolve (0.5)
    scene scene_64-38 with Dissolve (0.5)
    scene scene_64-37 with Dissolve (0.5)
    scene scene_64-38 with Dissolve (0.5)
    scene scene_64-37 with Dissolve (0.5)
    scene scene_64-38 with Dissolve (0.5)
    scene scene_64-37 with Dissolve (0.5)

    V "Aaahh ahhh ahh...mmhmmmm... yes yes... fuck me just like that honey..."

    A "Ahhh Veronica... baby... hhmmmpphh..."

    scene scene_64-38 with Dissolve (0.5)
    scene scene_64-37 with Dissolve (0.5)
    scene scene_64-38 with Dissolve (0.5)
    scene scene_64-37 with Dissolve (0.5)
    scene scene_64-38 with Dissolve (0.5)
    scene scene_64-37 with Dissolve (0.5)
    scene scene_64-38 with Dissolve (0.5)
    scene scene_64-37 with Dissolve (0.5)

    V "Ohh god.. you're so big..."

    V "Kiss me [player_name].. Kiss me..."

    scene scene_64-39 with Dissolve (1.0)

    V "mmhhmmphh..."

    A "*mmmhhmm..."

    jump veronicamissionary1


label veronicamissionary1:

    scene scene_64-40 with Dissolve (0.5)
    scene scene_64-39 with Dissolve (0.5)
    scene scene_64-40 with Dissolve (0.5)
    scene scene_64-39 with Dissolve (0.5)
    scene scene_64-40 with Dissolve (0.5)
    scene scene_64-39 with Dissolve (0.5)
    scene scene_64-40 with Dissolve (0.5)
    scene scene_64-39 with Dissolve (0.5)

    V "uuhhhh....mmhhhmmmmpph...mmmm..."

    scene scene_64-40 with Dissolve (0.5)
    scene scene_64-39 with Dissolve (0.5)
    scene scene_64-40 with Dissolve (0.5)
    scene scene_64-39 with Dissolve (0.5)
    scene scene_64-40 with Dissolve (0.5)
    scene scene_64-39 with Dissolve (0.5)
    scene scene_64-40 with Dissolve (0.5)
    scene scene_64-39 with Dissolve (0.5)

    scene scene_64-41 with Dissolve (1.0)

    V "Oh my god!! You are so fucking good [player_name]!!!"

    A "Veronica..aahh...huuuhh..."

    V "I can go like this all night long.. My pussy feels so great!!"

menu :

    "Get another blowjob":

        A "Blow me again baby.. Take my big cock in your mouth.."

        V "I love sucking your big cock hehehe.."

        jump veronicablowjob1


    "Lick her pussy":

        A "How about a little love for your beautiful pussy."

        V "Uhhmmm yes yes baby.."

        jump veronicapussylickdefault


    "Get a titjob":

        A "Fuck me with your tits baby."

        A "Please?"

        V "Heheh sure honey.."

        jump veronicatitjobdefault


    "Fuck her in missionary":

        A "I want to stay on top of you and keep fucking you like this.."

        V "Oh [player_name].."

        jump veronicamissionary1


    "Fuck her in doggy":

        A "Be my little bitch.. I'm going to take you from the back.."

        V "Aha naughty and dirty.. But I want to see how you do it.."

        jump veronicadoggydefault


    "Make her your cowgirl":

        A "Get on top of me baby..
           Fuck me like a cowgirl.."

        V "Hahah I'll ride you like a horse.."

        jump veronicacowgirldefault


    "Cum on her [blue]\[Ends Sex Scene\]":

        A "I'm going to cum baby.. I'm almost there..!!"

        V "Wait..!! Let me get down on my knees..."

        A "Baby.."

        V "Come here.."

        jump veronicacumshot1



    # Veronica pussy lick


label veronicapussylickdefault:


    scene scene_64-42 with Dissolve (1.0)

    A "You are soaking wet right now baby.."

    V "Is she beautiful?"

    A "She's so beautiful. I can't believe my eyes."

    scene scene_64-43 with Dissolve (1.0)

    V "Please love her like she is the only thing you have.."

    A "Veronica..."

    scene scene_64-44 with Dissolve (1.0)

    A "*lick*"

    V "ukkh...uumm.."

    A "*sniff* You smell so good Veronica. And the taste of your juicy pussy.. Oh god.."

    V "[player_name]...mmmmhh.."

    jump veronicapussylick1


label veronicapussylick1:


    scene scene_64-45 with Dissolve (0.5)
    scene scene_64-46 with Dissolve (0.5)
    scene scene_64-45 with Dissolve (0.5)
    scene scene_64-46 with Dissolve (0.5)
    scene scene_64-45 with Dissolve (0.5)
    scene scene_64-46 with Dissolve (0.5)
    scene scene_64-45 with Dissolve (0.5)
    scene scene_64-46 with Dissolve (0.5)

    V "OH GOD [player_name]!! It's too much!!"

    A "uummm...*lick* *lick*"

    scene scene_64-45 with Dissolve (0.5)
    scene scene_64-46 with Dissolve (0.5)
    scene scene_64-45 with Dissolve (0.5)
    scene scene_64-46 with Dissolve (0.5)
    scene scene_64-45 with Dissolve (0.5)
    scene scene_64-46 with Dissolve (0.5)
    scene scene_64-45 with Dissolve (0.5)
    scene scene_64-46 with Dissolve (0.5)
    scene scene_64-45 with Dissolve (0.5)
    scene scene_64-46 with Dissolve (0.5)
    scene scene_64-45 with Dissolve (0.5)
    scene scene_64-46 with Dissolve (0.5)


    V "[player_name]...."

    scene scene_64-47 with Dissolve (1.0)

    V "I'm... cumm......"

    with vpunch

    pause (1.0)

    V "hannngg..."

    with vpunch

    V "mming....."

    with vpunch

    scene white with dissolve
    $ renpy.pause(0.7, hard = True)

    scene scene_64-47 with Dissolve (1.0)

    V "Ohhh GOD!!! I came!!! [player_name] I love you!!"

    A "uuhhhmmm...Baby..."



menu :

    "Get another blowjob":

        A "Blow me again baby.. Take my big cock in your mouth.."

        V "I love sucking your big cock hehehe.."

        jump veronicablowjob1


    "Lick her pussy":

        A "I just want to taste your pussy right now."

        V "Uhhmmm yes yes baby.."

        jump veronicapussylick1


    "Get a titjob":

        A "Fuck me with your tits baby."

        A "Please?"

        V "Heheh sure honey.."

        jump veronicatitjobdefault


    "Fuck her in missionary":

        A "Let's put you down on the bed..
           I'm gonna make love with you.."

        V "Oh [player_name].."

        jump veronicamissionarydefault


    "Fuck her in doggy":

        A "Be my little bitch.. I'm going to take you from the back.."

        V "Aha naughty and dirty.. But I want to see how you do it.."

        jump veronicadoggydefault


    "Make her your cowgirl":

        A "Get on top of me baby..
           Fuck me like a cowgirl.."

        V "Hahah I'll ride you like a horse.."

        jump veronicacowgirldefault



    # Veronica cowgirl


label veronicacowgirldefault:


    scene scene_64-48 with Dissolve (1.0)

    A "Slowly and gently baby.. I don't want you to hurt your pussy.."

    V "You are so sweet and naughty at the same time.. hehe"

    V "ukkhhh...so big... I won't be able to put the whole thing in.."

    A "Slowly baby.."

    scene scene_64-49 with Dissolve (1.0)

    A "My god.. You were literally sent from heaven, weren't you?"

    V "hhunng.."

    scene scene_64-50

    with vpunch

    V "OH GOD!! IT'S SO FAT AND BIG!!"

    A "Now now slowly.. Don't rush it.. Slowly move your body.."

    V "ummmm....ahhh.."


    scene scene_64-49 with Dissolve (0.5)
    scene scene_64-50 with Dissolve (0.5)
    scene scene_64-49 with Dissolve (0.5)
    scene scene_64-50 with Dissolve (0.5)
    scene scene_64-49 with Dissolve (0.5)
    scene scene_64-50 with Dissolve (0.5)
    scene scene_64-49 with Dissolve (0.5)
    scene scene_64-50 with Dissolve (0.5)
    scene scene_64-49 with Dissolve (0.5)
    scene scene_64-50 with Dissolve (0.5)


    A "Yes just like that baby.. uhhmm... ahh...ahh.."

    V "[player_name]..!! huunng....ahh ahh ahh...mmm..."

    scene scene_64-49 with Dissolve (0.5)
    scene scene_64-50 with Dissolve (0.5)
    scene scene_64-49 with Dissolve (0.5)
    scene scene_64-50 with Dissolve (0.5)
    scene scene_64-49 with Dissolve (0.5)
    scene scene_64-50 with Dissolve (0.5)
    scene scene_64-49 with Dissolve (0.5)
    scene scene_64-50 with Dissolve (0.5)
    scene scene_64-49 with Dissolve (0.5)
    scene scene_64-50 with Dissolve (0.5)

    A "Come here baby.. Let me help you.."

    scene scene_64-51 with Dissolve (1.0)

    A "uuhhh..mmmmhh..."

    V "Bury your face between by boobs and fuck my pussy!!"

    scene scene_64-52 with Dissolve (1.0)

    V "OH YES!! FUCK MY PUSSY HARD!!"

    jump veronicacowgirl1


label veronicacowgirl1:

    scene scene_64-51 with Dissolve (0.5)
    scene scene_64-52 with Dissolve (0.5)
    scene scene_64-51 with Dissolve (0.5)
    scene scene_64-52 with Dissolve (0.5)
    scene scene_64-51 with Dissolve (0.5)
    scene scene_64-52 with Dissolve (0.5)
    scene scene_64-51 with Dissolve (0.5)
    scene scene_64-52 with Dissolve (0.5)

    V "[player_name] I can't handle this anymore...Oh god!!"

    V "HARDER HARDER HARDER!!! FUCK MY BRAINS OUT!!"

    scene scene_64-51 with Dissolve (0.5)

    scene scene_64-52
    with vpunch
    scene scene_64-51 with Dissolve (0.5)

    scene scene_64-52
    with vpunch
    scene scene_64-51 with Dissolve (0.5)

    scene scene_64-52
    with vpunch

    scene scene_64-51 with Dissolve (0.5)

    scene scene_64-52
    with vpunch
    scene scene_64-51 with Dissolve (0.5)

    scene scene_64-52
    with vpunch
    scene scene_64-51 with Dissolve (0.5)

    scene scene_64-52
    with vpunch


    scene scene_64-53 with Dissolve (1.0)

    V "huuuh.. huhhh..mmmmhmmm...honey..."

    A "Oh Veronica...my love...I can't explain this feeling.."

    V "I love you [player_name].. You made me whole.."




menu :

    "Get another blowjob":

        A "Blow me again baby.. Take my big cock in your mouth.."

        V "I love sucking your big cock hehehe.."

        jump veronicablowjob1


    "Lick her pussy":

        A "How about a little love for your beautiful pussy."

        V "Uhhmmm yes yes baby.."

        jump veronicapussylickdefault


    "Get a titjob":

        A "Fuck me with your tits baby."

        A "Please?"

        V "Heheh sure honey.."

        jump veronicatitjobdefault


    "Fuck her in missionary":

        A "Let's put you down on the bed..
           I'm gonna make love with you.."

        V "Oh [player_name].."

        jump veronicamissionarydefault


    "Fuck her in doggy":

        A "Be my little bitch.. I'm going to take you from the back.."

        V "Aha naughty and dirty.. But I want to see how you do it.."

        jump veronicadoggydefault


    "Make her your cowgirl":

        A "I want you to stay like this while I keep making love with you."

        V "[player_name].."

        jump veronicacowgirl1


    "Cum on her [blue]\[Ends Sex Scene\]":

        A "I'm going to cum baby.. I'm almost there..!!"

        V "Wait..!! Let me get down on my knees..."

        A "Baby.."

        V "Come here.."

        jump veronicacumshot1


    # Veronica Doggy


label veronicadoggydefault:


    scene scene_64-54 with Dissolve (1.0)

    V "Does your bitch look good master?"

    A "Are you kidding me baby?"

    V "Look how your slut is waiting for you big cock heheh.."

    A "You can be really dirty.."

    V "Come here.. Teach your slut a very hot steamy lesson.."

    A "Hahaha.."

    scene scene_64-55 with Dissolve (1.0)

    V "You aren't a good teacher my master.. You need to put your whole cock in..
       You know.. I'm a bit too dirty and naughty. I need the whole thing to learn.."

    A "How about this my filthy little slut?"

    scene scene_64-56

    with vpunch

    V "OH FUCK!!!! YES MASTER!! YES!! JUST LIKE THAT!!"

    A "Hahah now you are learning in a proper manner.."

    V "aahhhh.."

    V "Teach me more master.. With your big fat cock!"

    scene scene_64-57 with Dissolve (0.5)
    scene scene_64-56 with Dissolve (0.5)
    scene scene_64-57 with Dissolve (0.5)
    scene scene_64-56 with Dissolve (0.5)
    scene scene_64-57 with Dissolve (0.5)
    scene scene_64-56 with Dissolve (0.5)
    scene scene_64-57 with Dissolve (0.5)
    scene scene_64-56 with Dissolve (0.5)

    V "aaah ahhh...mmmh... feels so good master.. Don't stop teaching your slut!!"

    scene scene_64-57 with Dissolve (0.5)
    scene scene_64-56 with Dissolve (0.5)
    scene scene_64-57 with Dissolve (0.5)
    scene scene_64-56 with Dissolve (0.5)
    scene scene_64-57 with Dissolve (0.5)
    scene scene_64-56 with Dissolve (0.5)
    scene scene_64-57 with Dissolve (0.5)
    scene scene_64-56 with Dissolve (0.5)

    A "Time to teach my bitch a difficult subject.."

    V "YES YES MASTER!!"

    scene scene_64-58 with Dissolve (1.0)

    V "Haha master that's a very weird position. But it shows that you are really an experienced master.."

    V "Your little bitch is waiting for that difficult lesson master.."

    scene scene_64-60 with Dissolve (1.0)

    scene scene_64-59

    with hpunch

    V "OH SHIT!!! IT HURTS!!!"

    A "OH GOD!! I'M SORRY VERONICA!!"

    V "DON'T PULL IT OUT MASTER!! I NEED TO LEARN!! TEACH ME!! TEACH YOUR LITTLE SLUT!!"

    jump veronicadoggy1


label veronicadoggy1:

    scene scene_64-60 with Dissolve (1.0)

    scene scene_64-59

    with hpunch

    scene scene_64-60 with Dissolve (0.5)

    scene scene_64-59

    with hpunch

    scene scene_64-60 with Dissolve (0.5)

    scene scene_64-59

    with hpunch

    scene scene_64-60 with Dissolve (0.5)

    scene scene_64-59

    with hpunch

    scene scene_64-60 with Dissolve (0.5)

    scene scene_64-59

    with hpunch

    V "So good.. Soo good master.. Keep going.. Don't stop.."

    A "You little slut.. TAKE THIS!!"

    scene scene_64-60 with Dissolve (0.5)

    scene scene_64-59

    with hpunch

    scene scene_64-60 with Dissolve (0.5)

    scene scene_64-59

    with hpunch

    scene scene_64-60 with Dissolve (0.5)

    scene scene_64-59

    with hpunch

    scene scene_64-60 with Dissolve (0.5)

    scene scene_64-59

    with hpunch

    scene scene_64-60 with Dissolve (0.5)

    scene scene_64-59

    with hpunch

    scene scene_64-60 with Dissolve (0.5)

    scene scene_64-59

    with hpunch

    scene scene_64-60 with Dissolve (1.0)

    scene scene_64-58 with Dissolve (1.0)

    V "WOW!! THAT WAS AN AMAZING LESSON MASTER!!"

    A "HAHA YOU ARE SUCH A GOOD FILTHY SLUT."



menu :

    "Get another blowjob":

        A "Blow me again baby.. Take my big cock in your mouth.."

        V "I love eating your big cock hehehe.."

        jump veronicablowjob1


    "Lick her pussy":

        A "How about a little love for your beautiful pussy."

        V "Uhhmmm yes yes baby.."

        jump veronicapussylickdefault


    "Get a titjob":

        A "Fuck me with your tits baby."

        A "Please?"

        V "Heheh sure honey.."

        jump veronicatitjobdefault


    "Fuck her in missionary":

        A "Let's put you down on the bed..
           I'm gonna make love with you.."

        V "Oh [player_name].."

        jump veronicamissionarydefault


    "Fuck her in doggy":

        A "My slut needs more lesson.."

        V "Yes yes teach your slut even more.."

        jump veronicadoggy1


    "Make her your cowgirl":

        A "Get on top of me baby..
           Fuck me like a cowgirl.."

        V "Hahah I'll ride you like a horse.."

        jump veronicacowgirldefault


    "Cum on her [blue]\[Ends Sex Scene\]":

        A "I'm going to cum baby.. I'm almost there..!!"

        V "Wait..!! Let me get down on my knees... Your slut has to down on her knees"

        A "Baby.."

        V "Come here.."

        jump veronicacumshot1


    # Cumshot


label veronicacumshot1:


    scene scene_64-61 with Dissolve (1.0)

    A "I'M ALMOST THERE VERONICA!!!"

    V "SPRAY YOUR CUM ALL OVER ME!!"

    A "AAHAAHHHH...HERE IT COMES!!!"

    scene scene_64-62

    with vpunch

    A "Aaarrgghh.....hhhhuuuhh.....GOD!!!"

    scene white with dissolve
    $ renpy.pause(0.7, hard = True)

    scene scene_64-63 with Dissolve (1.0)

    A "hhuuhh huh huh..ahh..mmmhmm...WOW!!"

    V "mmmmhhh...yummm....mhhh...hehehe..."

    V "I'm covered in your thick cum honey..hehe...mmhmmm.."

    scene scene_64-64 with Dissolve (2.0)

    A "You were amazing Veronica. This can't get any better.."

    V "You missed a part of me though.."

    A "Huh? Which part?"

    V "It's between my buttcheeks heheh.."

    A "Wait! Are you into anal?"

    V "I can be into anything when I'm with you [player_name].."

    A "Wow! You just keep surprising me Veronica.."

    V "Hehe because I love you [player_name].."

    A "I love you too Veronica.."

    V "Now let's get a little bit of sleep.. A big day ahead of us."

    A "Yes it is Veronica.. Good night love.."

    V "Good night honey.."


    # Remember

    scene white with dissolve
    $ renpy.pause(0.7, hard = True)

    scene scene_64-65 with Dissolve (1.0)

    A "OH GOD!! VERONICA!!"

    scene scene_64-66 with Dissolve (1.0)

    S "*gasp*"

    scene scene_64-65 with Dissolve (1.0)

    "[player_name]..."

    A "HUH?"

    scene scene_64-67 with Dissolve (2.0)

    with hpunch
    $ renpy.end_replay()
    jump alandevilbathroomencounter
