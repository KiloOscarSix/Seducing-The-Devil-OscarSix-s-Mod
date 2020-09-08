

    # Scene 41

    # Diana Hospital Cafe


label dianahospitalcafe:

    scene episode4 with Dissolve (1.0)

    pause

    scene scene_41-1 with Dissolve (1.0)

    A "(Damn! I'm getting freaked out by anybody now. This needs to stop)"

    scene scene_41-2 with Dissolve (1.0)

    A "(Did that lady do something to [Mom_name]?
       Has she done something to everyone around me so that they don't recognise her anymore?)"

    A "(But wasn't she just a dream?!)"

    A "(FUCK THIS SHIT!!)"

    scene scene_41-3 with Dissolve (1.0)

    UN "[player_name].."

    A "Huh?"

    scene scene_41-4 with hpunch

    A "[Aunt_name]!!"

    DI "[player_name]! My baby.. Come here.."

    A "DI..!! You are here.."

    scene scene_41-5 with Dissolve (1.0)

    DI "I'm so glad you are okay sweetie. I was so worried."

    A "Thank you for coming Di.. Thank you so much.."

    DI "How are you now? Do you feel any pain?"

    scene scene_41-6 with Dissolve (1.0)

    A "I'm okay now. But Jason, Riley and Kylie.. They had it worst."

    DI "I know.."

    A "Things are so messed up Di.. I don't know what's going on.."

    A "Everyone is ignoring me whenever I mention [Mom_name].
       As if they don't even know her."

    A "A day has passed by and we don't know where she is. And now this."

    DI "You need to calm down [player_name]."

    A "But [Mom_name].. She is what matters the most right now."

    DI "Please calm down [player_name]. I'll explain everything.."

    scene scene_41-7 with Dissolve (1.0)

    A "Huh really?!"

    A "Did you find out about her?"

    A "Tell me you did. Please Di.."

    A "You are the only one who can do anything."

    scene scene_41-8 with Dissolve (1.0)

    DI "Yes I did. But we can't talk here."

    A "Why? What's wrong?"

    DI "This is just not the right place. We need a bit of privacy."

    A "Selina is in my cabin. And I can't leave this place either. My doctor won't allow me to go out."

    if renpy.loadable("patch.rpy") or patch:

        DI "Wait. I'll go talk the doctor and explain there's a family matter we need to discuss.
        We will still be in hospital area."

    if not renpy.loadable("patch.rpy"):

        DI "Wait. I'll go talk the doctor and explain there's an important matter we need to discuss.
        We will still be in hospital area."

    A "Uh okay Di.."

    scene blackscreen with Dissolve (1.0)

    "She convinces the doctor to let you go out for a bit"

    scene scene_41-9 with Dissolve (1.0)

    A "What's with that face [Aunt_name]?
       Where's [Mom_name]?
       Tell me what do you know.."

    scene scene_41-10 with Dissolve (1.0)

    DI "Th..There's something you need to know [player_name].."

    A "Yes...What is it? What's wrong? Is [Mom_name] okay?"

    scene scene_41-11 with Dissolve (1.0)

    DI "I'm so sorry [player_name].."

    A "What do you mean? Why are you saying sorry?"

    scene scene_41-12 with Dissolve (1.0)

    DI "It's all our fault.. We did everything.."

    A "Did what?!"

    DI "I know you must be thinking that you had a dream last night. But it's all true. Every bit of it.."

    scene scene_41-13 with Dissolve (1.0)

    A "WHAT??!!!"

    A "But how?! How is that even possible?!"

    A "There was a lady with wings. That can't be real! And I.. I.. NO!! It's impossible..!!"


    if renpy.loadable("patch.rpy") or patch:

        A "I couldn't have made my own mother pregnant. Never!!"

    if not renpy.loadable("patch.rpy"):

        A "I couldn't have made Rachel pregnant. Never!!"

    A "You are lying!!"

    A "Tell me the truth [Aunt_name]! What's going on?!"

    scene scene_41-14 with Dissolve (1.0)

    DI "IT IS THE TRUTH!!
       There's so much to tell [player_name]."

    A "Tell me..Please.."

    DI "**Sigh**"

    DI "Rachel.."

    DI "She.. She sold her soul to the devil.."

    scene scene_41-13 with Dissolve (1.0)

    A "WHAT?! SOLD HER SOUL??!!"

    DI "Yes she became a slave of the devil long time ago..
       We call the devil Goddess Lileva.."

    A "But but why?! Why would she do that?!"

    DI "To change our fate.."

    A "I don't get it.."

    if renpy.loadable("patch.rpy") or patch:

        DI "You know how much she hates her parents, don't you?"

    if not renpy.loadable("patch.rpy"):

        DI "You know how much she hates the people who raised us, don't you?"

    A "Uhh yes yes.. She never liked me mentioning them.."

    DI "It wasn't for just any reason.."

    scene scene_41-11 with Dissolve (1.0)

    DI "We...we were like toys.."

    A "What do you mean?!"

    if renpy.loadable("patch.rpy") or patch:

        DI "Mom and Dad used us as their sex toys. Every night Dad would come and pick one of us.."

        DI "To.. To.. abuse for hours.."

        A "......!!"

        DI "Mom would just enjoy watching us get used by him.. We were young..
            There was just nothing we could do. We were helpless."

    if not renpy.loadable("patch.rpy"):

        DI "They used us as their sex toys. Every night they would come and pick one of us.."

        DI "To.. To.. abuse for hours.."

        A "......!!"

        DI "We were young.. There was just nothing we could do. We were helpless."

    A "[Aunt_name]... [Mom_name]..."

    DI "At one point we got used to it.. We would doll up and wait for them to come..
        That's what they wanted.."

    A "Then..."

    DI "One day she met Lileva. I don't know how but she did. Lileva promised to give us a better life."

    A "How?"

    if renpy.loadable("patch.rpy") or patch:

        DI "Tell me [player_name].. Did you ever meet your grandparents?"

    if not renpy.loadable("patch.rpy"):

        DI "Tell me [player_name].. Did you ever get to meet those people?"

    A "No.. Never.."

    DI "They are dead.. Lileva killed them long time ago.."

    scene scene_41-13 with Dissolve (1.0)

    A "WHAT THE FUCK?!!!"

    DI "That was the first wish of Rachel. Getting rid of them.."

    if renpy.loadable("patch.rpy") or patch:

        DI "Then she met Adam. They got married and you were born."

    if not renpy.loadable("patch.rpy"):

        DI "Then she met Adam. They got married."

    scene scene_41-15 with Dissolve (1.0)

    A "[Mom_name]..How hard it must have been for you both!"

    A "But what about yesterday?!"

    A "Why did she leave and how did all these happen?!"

    if renpy.loadable("patch.rpy") or patch:

        DI "All those years of abuse scarred her life.."

        DI "After you were born.. She started showing similar characteristics.."

        A "What do you mean?!"

        DI "She started feeling attracted to you.. Not in a monstrous way.. She didn't want to become like dad."

        A "WHAT?! Why would she?!"

        DI "I don't know. She asked for help from Lileva again. To change her..
        So that she doesn't remain as you mother anymore. Her relationship with Adam was already broken.
        Adam knew something was off. He knew how she felt about you."

    if not renpy.loadable("patch.rpy"):

        DI "All those years of abuse scarred her life.."

        DI "After you came.. She started changing.."

        A "What do you mean?!"

        DI "She started feeling attracted to you.. Not in a bad way.."

        A "WHAT?! Why would she?!"

        DI "I don't know. She asked for help from Lileva again. To change her to a completely different person..
        So that she can present herself to you as a new woman. Her relationship with Adam was already broken.
        Adam knew something was off. He knew how she felt about you."

    A "Then.."

    DI "Lileva asked Rachel to bring you to her. The only way to bring you in her world was through lust.."

    DI "It is her only strength. She feed on lust. Rachel moved out knowing you would be looking for her..
        I know you've had interaction with multiple girls by now. Lileva fueled the lust inside you and the girls around you."

    DI "I don't blame you for feeling attracted to them or them feeling attracted to you."

    DI "But it opened the door to her world."

    A "I...I...."


    A "What about me making [Mom_name] pregnant? What about that baby? And how do you come into this?"

    scene scene_41-16 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:

        DI "I've been with her all the time. I've helped her however I could.
            She is the only family I have.
            But everything that has happened yesterday shouldn't have happened."

        DI "Lileva betrayed us! She called it a ritual to change Rachel.
            But no. Instead it was a ritual to punish her."

        DI "Lileva got furious. She felt Rachel was following the path of Dad.
            Lileva doesn't like double faced people.
            So she brought you in to replace her and then entrap her."


    if not renpy.loadable("patch.rpy"):

        DI "I've been with her all the time. I've helped her however I could.
            She is the only person I have in my life.
            But everything that has happened yesterday shouldn't have happened."

        DI "Lileva betrayed us! She called it a ritual to change Rachel.
            But no. Instead it was a ritual to punish her."

        DI "Lileva got furious. She felt Rachel was becoming too greedy.
            Lileva doesn't like greedy people.
            So she brought you in to replace her and then entrap her."


    scene scene_41-17 with Dissolve (1.0)

    A "I don't understand..!"

    if renpy.loadable("patch.rpy") or patch:

        DI "That baby now carries the soul of Rachel. Lileva will use that baby to manipulate you and make you her slave.
            She needs lust to live. She can't get anything from Rachel now but you have what she needs."

        A "So what now? Did I just kill my mother? Is this what you are saying?
           Oh god!! I can't believe this!"

    if not renpy.loadable("patch.rpy"):

        DI "That baby now carries the soul of Rachel. Lileva will do everything to lure you in and make you her slave.
            She needs lust to live. She can't get anything from Rachel now but you have what she needs."

        A "So what now? Did I just kill Rachel? Is this what you are saying?
           Oh god!! I can't believe this!"


    scene scene_41-16 with Dissolve (1.0)

    DI "No [player_name].. She is still alive. I can't say anything more than this.
        I was there the whole time. And now Lileva is looking for me. You have to figure things out by yourself."

    scene scene_41-18 with Dissolve (1.0)

    DI "I'm so sorry for putting you into this. We should have just died with those monsters.
        Everything is so messed up now.. Only because of us."

    scene scene_41-19 with Dissolve (1.0)

    A "[Aunt_name].."

    DI "You have to save her [player_name]. You are her only hope.."

    A "But how?!"

    DI "I don't know. I would have done something if I knew how.
        You are the only key to her door [player_name]."

    DI "You will soon find out. Lileva will try to lure you in. You have to figure out how to deceive her and save Rachel."

    A "What about you [Aunt_name]?"

    DI "I'm leaving this country. I'll move to USA. I can't stay here."

    A "NO!! Are you going to leave me like this?!"

    DI "I'm so sorry [player_name].. I can't do anything.
        I'm powerless and I have to leave.
        You are a strong man [player_name].. I know you can do it.."

    DI "I love you my baby.."

    A "[Aunt_name]..."

    DI "Remember [player_name].. Don't forget her. Everyone around you already did.
        You have to remember.."

    A "I will.. I love you [Aunt_name].."

    scene scene_41-20 with Dissolve (1.0)

    DI "Goodbye [player_name]. I hope we can meet again but don't look for me."

    A "*sniff* Goodbye [Aunt_name].."

    scene scene_41-21 with Dissolve (1.0)

    A "...."

    A "GOD!!!! NO!!!"

    A "(My mind is completely blank right now... What has just she just said?!
       How can all this be possible? Why would [Mom_name] go through all these?
       And how am I even going to save her?!)"

    A "([Aunt_name] can't do anything. She's just left me like this."

    A "(She is moving to USA. USA?)"

    scene scene_41-22 with Dissolve (1.0)

    A "(ELLA!!)" with hpunch

    A "(Shit!! I've completely forgotten about her!! She must be worried sick right now!!)"


    jump ellacallalan

    # Scene 42

    # Ella first scene

label ellacallalan:

    scene blackscreen with Dissolve (1.0)

    "*Ring* *Ring*"

    scene scene_42-1 with Dissolve (1.0)

    E "(Why isn't he picking it up?)"

    E "(I've been calling him for such a long time)"

    scene scene_42-2 with Dissolve (1.0)

    E "(Baby pick up the phone.. Please!)"

    E "(Oh god! I have called him over 100 times already)"

    scene scene_42-3 with Dissolve (1.0)

    E "(I hope you are okay.. Maybe it's just the network.. Maybe you're busy.. Maybe)"

    scene scene_42-4 with Dissolve (1.0)

    E "([player_name].. I don't know what to do)"

    E "(Did something bad happen to him? No no no.. I'm thinking way too much)"

    scene scene_42-5 with Dissolve (1.0)

    E "(I'm sure he is just busy or maybe lost his phone.. He is okay)"

    E "(I'm sure he will call..me..back)"

    scene scene_42-6 with Dissolve (1.0)

    E "(I need to calm down.. Maybe his phone died or something)"

    scene scene_42-7 with Dissolve (1.0):
            subpixel True
            yalign 1.0
            linear 7.0 yalign 0.0

    M "Ella.."

    M "You are finally up..."

    scene scene_42-8 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:

        E "Mom..."

    if not renpy.loadable("patch.rpy"):

        E "Maddy.."

    M "Oh my.. What's wrong honey?"

    M "Did you have trouble sleeping?"

    M "Why do you look so down?"

    scene scene_42-9 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:

        E "Mom...*sniff* *sniff*"

        M "Tell me what's wrong.. Did you have a bad dream?"

        E "Mom.. It's [player_name].."

    if not renpy.loadable("patch.rpy"):

        E "Maddy...*sniff* *sniff*"

        M "Tell me what's wrong.. Did you have a bad dream?"

        E "Maddy.. It's [player_name].."


    M "What happened?"

    E "I've been trying to reach out to him since yesterday but I can't..
       He isn't picking up his phone.. I don't know what to do.. I've called him so many times.."

    E "But no one's answering.. What if something bad happened to him? *sniff* *sniff*"

    E "Something like this has never happened before.."

    scene scene_42-10 with Dissolve (1.0)

    M "So he has finally showed his true color.. huh!"

    M "Finally decided to ditch my daughter after trying to play for so long."

    if renpy.loadable("patch.rpy") or patch:

        E "MOM!!"

    if not renpy.loadable("patch.rpy"):

        E "MADDY!!"

    M "Why am I not surprised? Long distance relationships don't work! You should have listened to me.."

    scene scene_42-11 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:

        E "MOM!! What if something bad really happened to him? I'm so worried and sad right now.."

    if not renpy.loadable("patch.rpy"):

        E "MADDY!! What if something bad really happened to him? I'm so worried and sad right now.."

    scene scene_42-12 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:

        M "Oh my sweet little girl.. Don't worry.. I'll have someone look for him..
           Why don't you go and take a nice warm bath? In the meantime I'll make something to eat.
           You didn't have your breakfast yet."

        E "Will you really do that for me?"

        M "Anything for my baby girl.."

        E "*sniff* *sniff* thank you so much mom.."

    if not renpy.loadable("patch.rpy"):

        M "Oh sweety.. Don't worry.. I'll have someone look for him..
           Why don't you go and take a nice warm bath? In the meantime I'll make something to eat.
           You didn't have your breakfast yet."

        E "Will you really do that for me?"

        M "Anything for you sweety.."

        E "*sniff* *sniff* thank you so much Maddy.."


    scene blackscreen with Dissolve (1.0)

    A "(I need to call her. Where did they keep my phone?)"

    $ veronica_cafe_1 = True

    scene waitingroom with dissolve

    call screen waitingroom


    # Scene 43

    # Alan call Ella first scene

    $ alan_call_ella = False

label alancallella:

    scene scene_43-1

    A "SELINA..!"

    scene scene_43-2 with Dissolve (1.0)

    S "HUH? What's going on? Are you alright?"

    A "Did you see my phone?"

    S "Uhh it's in that drawyer.. What's wrong?"

    scene scene_43-3 with Dissolve (1.0)

    A "I haven't talked to Ella since yesterday morning. She must be getting worried sick now.
       I need to call her ASAP!"

    scene scene_43-4 with Dissolve (1.0)

    S "Oh Ella... Yes you should call her..."

    A "Come on.. Pick up the phone.."

    scene scene_43-5 with Dissolve (1.0)

    "*Ring* *Ring*"

    "......"

    A "Where is she?"

    scene scene_43-6 with Dissolve (1.0)

    "*Ring* *Ring*"

    "*Crank* Door opens"

    "*Ring* *Ring*"

    scene scene_43-7 with Dissolve (1.0)

    "...."

    scene scene_43-8 with Dissolve (1.0)

    A "ELLA..Baby..I'm so sorry.."

    M "Hi [player_name]..."

    A "Oh Maddy.. Hi.. How are you? Is Ella there?"

    scene scene_43-9 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:

        M "How dare you?!! How dare you call her?!!
           Hasn't she suffered enough?! My daughter hasn't slept for a whole night and here you are asking how am I and where is she?!"


    if not renpy.loadable("patch.rpy"):

        M "How dare you?!! How dare you call her?!!
           Hasn't she suffered enough?! Ella hasn't slept for a whole night and here you are asking how am I and where is she?!"


    A "Maddy.. I'm really really sorry. I had a little accident."

    M "A little one, right? Then you should have called. She has been crying all day long.
       For how long do you plan on hanging on to her? She is older than you and should be getting married for Christ's sake!!"


    scene scene_43-10 with Dissolve (1.0)

    A "Maddy.. It's not what you think it is.. I really love her and I do want to be with her."

    if renpy.loadable("patch.rpy") or patch:

        M "Oh yeah? How would a kid keep my daughter happy? Do you think I'll fall for your bullshit?!
           Aren't you ashamed of yourself?! She should be living happily with a very nice man.
           Instead she is hanging around with a kid from the Internet!"

    if not renpy.loadable("patch.rpy"):

        M "Oh yeah? How would a kid keep her happy? Do you think I'll fall for your bullshit?!
           Aren't you ashamed of yourself?! She should be living happily with a very nice man.
           Instead she is hanging around with a kid from the Internet!"

    A "Maddy.. I.."

    scene scene_43-11 with Dissolve (1.0)

    M "Stop everything with her. Get the hell out of her life!"

    A "Maddy.. Please try to understand.."

    scene scene_43-12 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:

        E "Mom.. Who is it?"

    if not renpy.loadable("patch.rpy"):

        E "Maddy.. Who is it?"

    E "Why are you shouting?"

    scene scene_43-13 with Dissolve (1.0)

    A "Ella..."

    M "It's.. It's [player_name].."

    scene scene_43-14 with Dissolve (1.0)

    E "[player_name]!!! OH MY GODD!! GIVE ME THE PHONE!!!"

    M "El..."

    scene scene_43-15 with Dissolve (1.0)

    E "BABY!!!"

    M "Oh for Christ's sake! You are so naive!!"

    scene scene_43-16 with Dissolve (1.0)

    E "[player_name].. Baby.. Where were you? *sniff* I was so worried about you..
       I've called you so many times *sniff*"

    scene scene_43-17 with Dissolve (1.0)

    A "(I can't tell her about what happened. She will literally go crazy)"

    E "Please say something..."

    A "Baby.. I'm so sorry.. I had a little food poisoning yesterday.. I'm in hospital right now.."

    E "OH MY GOD!! HOW ARE YOU NOW?!!"

    A "I'm fine Ella. It's nothing serious. Doctor said I'm totally fine now and I can go back home very soon.."

    E "Oh thank god.."

    A "I'm sorry for making you worried baby.. I should have called.."

    scene scene_43-18 with Dissolve (1.0)

    E "It's okay baby. I'm just glad that you are okay.. Nothing else matters to me.."

    A "Maddy told me that you haven't slept at all and been crying all day.."

    scene scene_43-19 with Dissolve (1.0)

    E "Hehe you know me baby.. You are my everything..
       I can't live a day without you..
       I just love you way too much.."

    scene scene_43-20 with Dissolve (1.0)

    E "I'm sorry baby.."

    A "For what?"

    if renpy.loadable("patch.rpy") or patch:

        E "I've heard mom shouting at you.. Don't take her words to your heart.. You know how she is.."

    if not renpy.loadable("patch.rpy"):

        E "I've heard Maddy shouting at you.. Don't take her words to your heart.. You know how she is.."

    A "I can understand where she is coming from Ella. It's alright.."

    scene scene_43-21 with Dissolve (1.0)

    A "*Sign* What Selina?"

    E "She is just way too protective of me.."

    if renpy.loadable("patch.rpy") or patch:

        M "I'm your mother. So I should be.."

        E "Yeah yeah Mom.. And I love you for being so protective.. But [player_name] is my boyfriend.
           You need to go easy on him.. He truly loves me.."

    if not renpy.loadable("patch.rpy"):

        M "I should be.."

        E "Yeah yeah Maddy.. And I love you for being so protective.. But [player_name] is my boyfriend.
           You need to go easy on him.. He truly loves me.."

    A "*Sign* What??"

    scene scene_43-22 with Dissolve (1.0)

    S "*Sign* Nothing.."

    S "**Sigh**"

    scene scene_43-23 with Dissolve (1.0)

    E "Who brought you to the hospital baby?"

    A "Veronica and Selina did."

    E "huh? Were you at their place?"

    A "Uh yes.. I was invited there to have dinner."

    E "I'm glad that they were there for you. I wish I could too.
       I feel so empty without you."

    A "Oh baby.. You are always with me.."

    scene scene_43-24 with Dissolve (1.0)

    E "*GASP**"

    scene scene_43-25 with Dissolve (1.0)

    M "**Shush**"

    E "I want to be with you in real life baby. Hugging you, touching you, kissing you.. I want to be with you all the time.."

    A "One day.."

    scene scene_43-26 with Dissolve (1.0)

    E "Hehe and and we will have babies too."

    A "Hahah yeah.. That would be nice.."

    scene scene_43-27 with Dissolve (1.0)

    M "**Lick** **Lick**"

    M "**Whispering** You taste very nice today.."

    scene scene_43-28 with Dissolve (1.0)

    E "Ukkhh..."

    A "What's wrong Ella?"

    E "It's nothing.."

    A "Ah okay.."

    scene scene_43-29 with Dissolve (1.0)

    A "Baby I need to go now.. I'll call you at night.."

    E "Okay baby.. Please don't forget to call. I can't sleep without hearing your voice."

    E "I love you so much baby.."

    A "I love you so much too.."

    scene scene_43-30 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:

        E "OH GOD!!! MOM!!! UUnnnghhh...mmmmm...yesssss..."

    if not renpy.loadable("patch.rpy"):

        E "OH GOD!!! MADDY!!! UUnnnghhh...mmmmm...yesssss..."

    scene scene_43-31 with Dissolve (1.0)

    A "(I'm sorry for lying to you Ella.. But it's better if you don't know)"

    scene scene_43-32 with Dissolve (1.0)

    A "What's up with you? Why are you making that kind of face?
       Are you still mad at me?"

    scene scene_43-33 with Dissolve (1.0)

    S "No.. It's nothing.. Forget it.."

    A "Forget what? I can clearly see that you aren't happy about something.."

    scene scene_43-34 with Dissolve (1.0)

    S "Oh really?! But do you even care [player_name]? You don't care at all..!!"

    A "Care about what?!"

    scene scene_43-35 with Dissolve (1.0)

    S "*mwah**!!"

    A "(WHAT THE FUCK?!)"

    scene scene_43-34 with Dissolve (1.0)

    S "Tell me.. Did it make any difference? Do you even care?!"

    A "What the hell are you talking about?! What was that all about?"

    S "Forget it.."

    scene scene_43-36 with Dissolve (1.0)

    "Selina left the cabin"

    A "(What the hell was that? Why is she acting so weird?
       Did I do something wrong to piss her off?)"

    $ alan_call_ella = True

    scene alancabin with dissolve

    call screen hospitalnavigate


    # Scene 44

    # Kiley family hospital 2



    $ kylie_family_hospital = False

label kyliefamilyhospital2:

    # if Kiley

    if stayriley == "no":

        scene scene_44-1 with Dissolve (1.0)

        A "(Looks Kylie has woken up)"

        A "(I should go and talk to her)"

        scene scene_44-2 with Dissolve (1.0)

        A "(She looks lost.. Wonder what she is thinking about)"

        scene scene_44-3 with Dissolve (1.0)

        A "Kylie..."

        scene scene_44-4 with Dissolve (1.0)

        K "Huh?"

        A "Thank god you are okay. I was so worried about you."

        scene scene_44-5 with Dissolve (1.0)

        K "[player_name]? What..?"

        scene scene_44-6 with Dissolve (1.0)

        K "What the hell? What's wrong with you [player_name]? Why are you touching me?!"

        A "Ky... I thought you and I.."

        A "(She probably doesn't remember anything since she was influenced by Lileva)"

        scene scene_44-7 with Dissolve (1.0)

        A "I.. I'm sorry Kylie.. I was so worried that I got carried away.."

        A "Hope you won't think bad of me.."

        A "How are you feeling now?"

        scene scene_44-8 with Dissolve (1.0)

        K "I'm feeling good but it still feels so strange and I can't wrap my head around it.."

        A "Yes it's very weird.."

        K "What about you? Are you okay now?"

        A "Yes.. I'm alright.."

        A "Do you remember what happened yesterday?"

        scene scene_44-9 with Dissolve (1.0)

        K "Not much.. It's just that there was a crying voice.. A baby crying.. And I started feeling dizzy. Don't remember anything after that.."

        A "Oh I feel sorry you and them.. Don't know why this is happening to us.."

        K "I'm glad you care [player_name].."

        scene scene_44-10 with Dissolve (1.0)

        A "Can I give you hug Kylie?"

        A "I feel like we both need it.."

        K "That's so sweet of you honey.. Come here."

        scene scene_44-11 with Dissolve (1.0)

        K "Thank you [player_name].."

        A "I feel much better now.."

        K "So do I.."

        $ kylie_family_hospital2 = True

        scene hospitalroom1 with dissolve

        call screen hospitalnavigate


    # if Riley

    if stayriley == "yes":

        scene scene_44-12 with Dissolve (1.0)

        A "(Looks Riley has woken up)"

        A "(I should go and talk to her)"

        scene scene_44-13 with Dissolve (1.0)

        A "(She looks lost.. Wonder what she is thinking about)"

        scene scene_44-14 with Dissolve (1.0)

        A "Riley..."

        scene scene_44-15 with Dissolve (1.0)

        R "Huh?"

        A "*mwah*"

        scene scene_44-16 with Dissolve (1.0)

        A "Thank god you are okay. I was so worried about you."

        R "[player_name]? What..?"

        scene scene_44-17 with Dissolve (1.0)

        R "What the hell? What's wrong with you [player_name]? Why did you kiss me?!"

        A "Ri... I thought you and I.."

        A "(She probably doesn't remember anything since she was influenced by Lileva)"

        scene scene_44-18 with Dissolve (1.0)

        A "I.. I'm sorry Riley.. I was so worried that I got carried away.."

        A "Hope you won't think bad of me.."

        A "How are you feeling now?"

        scene scene_44-19 with Dissolve (1.0)

        R "I'm feeling good but it still feels so strange and I can't wrap my head around it.."

        A "Yes it's very weird.."

        R "What about you? Are you okay now?"

        A "Yes.. I'm alright.."

        A "Do you remember what happened yesterday?"

        scene scene_44-20 with Dissolve (1.0)

        R "Not much.. It's just that there was a crying voice.. A baby crying.. And I started feeling dizzy. Don't remember anything after that.."

        A "Oh I feel sorry you and them.. Don't know why this is happening to us.."

        R "I'm glad you care [player_name].."

        scene scene_44-21 with Dissolve (1.0)

        A "Can I give you hug Kylie?"

        A "I feel like we both need it.."

        R "That's so sweet of you [player_name].. Come here."

        scene scene_44-22 with Dissolve (1.0)

        R "Thank you [player_name].."

        A "I feel much better now.."

        R "So do I.."

        $ kylie_family_hospital2 = True

        scene hospitalroom1 with dissolve

        call screen hospitalnavigate



    # Scene 45

    # Selina Hospital Entrance Scene

    $ selina_hospital_entrance = False

label selinahospitalentrance:


    scene scene_45-1 with Dissolve (1.0)

    A "(I have to know what's going on with her.. Can't have my own friend to have grudges on me when things are so bad right now)"

    scene scene_45-2 with Dissolve (1.0)

    A "Selina.. We need to talk."

    scene scene_45-3 with Dissolve (1.0)

    S "What do you want now?"

    scene scene_45-4 with Dissolve (1.0)

    A "You are not making any sense Selina. Tell me what's wrong. You have been acting weird. Did I do something wrong?"

    A "You are my friend and I should know if there's something bugging you.."

    scene scene_45-5 with Dissolve (1.0)

    S "There's nothing to talk about.."

    S "Why don't you just go and talk to your girlfriend? Stop bothering me!"

menu:

    A "This is going nowhere. She is dead set on not wanting to talk. What do I do now?"

    "Be forceful [gr]\[AlanForceSelina\]":
        $ alanforceselina = "yes"
        jump alanforceselina

    "Be understanding":
        $ alanforceselina = "no"
        jump alannoforceselina


    # if force

label alanforceselina:

    scene scene_45-6 with vpunch

    A "Enough.."

    S "**Gasp**"

    A "What's wrong with you? I keep asking you but you keep ignoring me. How about you show a little respect?"

    scene scene_45-7 with Dissolve (1.0)

    S "[player_name]! What are you doing?! Go away!"

    scene scene_45-8 with Dissolve (1.0)

    A "I have got your attention now. I'm not going anywhere unless you tell me what's going on!"

    S "[player_name]! Stop! People are watching us!"

    Un "Miss.."

    scene scene_45-9 with Dissolve (1.0)

    Un "What's going on? Is this guy bothering you?"

    A "Why don't you just get the fuck out of here bro?!"

    Un "I'm going to call the security if you don't let her go right now."

    scene scene_45-10 with Dissolve (1.0)

    S "No. I'm alright. We are friends and just having a chat. Please don't bother yourself with this."

    Un "Okay if you say so miss."

    scene scene_45-11 with Dissolve (1.0)

    S "[player_name] we are drawing way too much attention. You need to stop right now.."

    scene scene_45-12 with Dissolve (1.0)

    S "Please [player_name].. Yes I'm upset.. But can we talk about it later.."


menu:

    "Kiss her [gr]\[AlanKissHospital\]":
        $ alankisshospital = "yes"
        jump alankisshospital

    "Let her go":
        $ alankisshospital = "no"
        jump alanletselinago



    # if alan decides to kiss selina

label alankisshospital:

    scene scene_45-13 with Dissolve (1.0)

    A "*mwah*"

    S "[player_name]..."

    scene scene_45-14 with Dissolve (1.0)

    S "Why?"

    A "Well I'm returning the favor. Felt like you needed me to do the same."

    S "[player_name].. I.."

    scene scene_45-15 with Dissolve (1.0)

    A "*mwah* *mwah*"

    scene scene_45-16 with Dissolve (1.0)

    S "So you do care, huh?"

    S "Thank you [player_name].."

    A "Are we good now Selina?"

    S "Yes we are.."

    S "I have to go now [player_name].."

    A "Okay. See you later.."

    scene scene_45-17 with Dissolve (1.0)

    "Selina left"

    scene scene_45-18 with Dissolve (1.0)

    Do "Hmmm..."

    scene scene_45-17 with Dissolve (1.0)

    Do "Hello Mr. [player_name].."

    scene scene_45-19 with Dissolve (1.0)

    A "Oh hi doctor.."

    Do "Please meet me at my office when you have the time. It's right beside your friend's cabin."

    A "Okay doctor."

    $ selina_hospital_entrance = True

    scene waitingroom with dissolve

    call screen hospitalnavigate


    # if alan doesn't kiss selina

label alanletselinago:

    scene scene_45-20 with Dissolve (1.0)

    A "Okay. I'm letting you go for now. But we will have a talk."

    S "Okay [player_name].."

    scene scene_45-17 with Dissolve (1.0)

    "Selina left"

    scene scene_45-18 with Dissolve (1.0)

    Do "Hmmm..."

    scene scene_45-17 with Dissolve (1.0)

    Do "Hello Mr. [player_name].."

    scene scene_45-19 with Dissolve (1.0)

    A "Oh hi doctor.."

    Do "Please meet me at my office when you have the time. It's right beside your friend's cabin."

    A "Okay doctor."

    $ selina_hospital_entrance = True

    scene waitingroom with dissolve

    call screen hospitalnavigate




    # if no force

label alannoforceselina:

    A "Come here.."

    scene scene_45-21 with Dissolve (1.0)

    S "Huh?"

    A "You silly silly girl.."

    scene scene_45-22 with Dissolve (1.0)

    S "What is this all about? Why are you suddenly hugging me in front of everyone?"

    A "Felt like you needed a hug.. You know that I can never be angry or upset at you. I expect the same from you. You are my best friend Selina.."

    scene scene_45-23 with Dissolve (1.0)

    S "Oh [player_name].. Thank you.. I really needed this.."

    A "Don't cry now. People will think we are breaking up or some shit."

    scene scene_45-24 with Dissolve (1.0)

    S "Haha you idiot. We can never break up. We are set for life."

    A "Absolutely.."

    S "Okay I'll go now. See you later."

    scene scene_45-17 with Dissolve (1.0)

    "Selina left"

    scene scene_45-18 with Dissolve (1.0)

    Do "Hmmm..."

    scene scene_45-17 with Dissolve (1.0)

    Do "Hello Mr. [player_name].."

    scene scene_45-19 with Dissolve (1.0)

    A "Oh hi doctor.."

    Do "Please meet me at my office when you have the time. It's right beside your friend's cabin."

    A "Okay doctor."

    $ selina_hospital_entrance = True

    scene waitingroom with dissolve

    call screen hospitalnavigate


    # Scene 46

    # Doctor Room scene

    $ doctor_room = False

label doctorroom:

    scene scene_46-1 with Dissolve (1.0)

    A "Hello doctor. You've asked me to meet you here."

    Do "Aah yes Mr. [player_name]."

    scene scene_46-2 with Dissolve (1.0)

    Do "Please take a seat."

    A "Thank you."

    scene scene_46-3 with Dissolve (1.0)

    Do "So how are you feeling right now?"

    A "I'm feeling better now. No headache or anything. The rest helped."

    Do "Good to know."

    scene scene_46-4 with Dissolve (1.0)

    A "But is there any way of knowing the cause?"

    Do "We have few guesses."

    scene scene_46-5 with Dissolve (1.0)

    Do "We have informed the police about this incident. They will likely meet you to ask few questions."

    A "Yes I've heard from [Dad_name] that the police is looking into this matter."

    Do "So the reason I've called you for.. We've determined that there's no additional test needed to do on you."

    Do "You can leave as early as tonight if you want. But Jason and his people will have stay few more days."

    scene scene_46-6 with Dissolve (1.0)

    A "Wow that's great to know."

    Do "I have already informed Mr. Adam and Mrs. Veronica."

    Do "Rest of the matter will be handled by the police. I'm confident that nothing malicious has been done. It's more likely to be due to exhaustion."

    A "I hope you are right. Thanks for letting me know doctor."

    A "Thank you for taking taking a good care of me."

    scene scene_46-7 with Dissolve (1.0)

    Do "You are most welcome Mr. [player_name]. If there's any problem then give us a call. We will respond as quickly as possible."

    A "Thank you doctor."

    Do "Take care."

    $ doctor_room = True

    scene hospitalroom1 with dissolve

    call screen hospitalnavigate



    # Scene 47

    # Veronica Hospital Room Scene

    $ veronica_hospital = False

label veronicahospitalroom:


    scene scene_47-1

    A "(Oh Veronica is here. What's she got there? Did she do shopping with [Dad_name]?)"

    scene scene_47-2 with Dissolve (1.0)

    A "Hey Veronica.."

    scene scene_47-3 with Dissolve (1.0)

    V "Oh hey [player_name].."

    V "Looks like you didn't listen when I've asked you to rest."

    A "Ahh I couldn't fall asleep.."

    scene scene_47-4 with Dissolve (1.0)

    V "Well I've heard from the doctor. So you can rest at your place from today."

    V "Look I've bought a set of dress for you. You've been wearing the same thing for two days now."

    A "Aahh yes. Thanks Veronica."

    scene scene_47-5 with Dissolve (1.0)

    V "I've also bought some food for you. I'm sorry for not being able to bring any homemade food.
       I didn't have the time. Hope you don't mind."

    A "No it's alright. You've done more than enough Veronica. Thank you."

    A "Where's [Dad_name]?"

    scene scene_47-6 with Dissolve (1.0)

    V "He'll be here shortly to pick us up."

    V "Why don't you eat the food and then get changed."

    A "Aahh okay."

    "Door opens"

    scene scene_47-7 with Dissolve (1.0)

    V "Where have you been all this time? Both of you were missing from here.
       Didn't I ask you to take here of him?"


    if renpy.loadable("patch.rpy") or patch:

        S "He isn't a baby mom."

    if not renpy.loadable("patch.rpy"):

        S "He isn't a baby Veronica."

    scene scene_47-8 with Dissolve (1.0)

    V "I've bought some food for you both. Would you like to eat Selina?"

    S "Yeah sure. I'm starving."

    scene scene_47-9 with Dissolve (1.0)

    A "Well this is really good Veronica."

    V "I'm glad you like it."

    scene scene_47-10 with Dissolve (1.0)

    V "Here you go.."

    "As she moves forward her leg bumps into the bed and"

    scene scene_47-11 with hpunch

    V "Oh SHI.."

    A "Uhh.."

    scene scene_47-12 with Dissolve (1.0)

    V "Oh god! I'm so sorry [player_name].. Wait let me grab a tissue.."

    scene scene_47-13 with Dissolve (1.0)

    V "Let me clean it up for you or you'll catch cold.."

menu:

    "Let her do it [gr]\[VeronicaClean\]":
        $ veronicaclean = "yes"
        jump veronicaclean


    "Clean it yourself":
        $ veronicaclean = "no"
        jump alanclean


    # if veronica clean

label veronicaclean:

    A "Uhh okay Veronica.."

    scene scene_47-14 with Dissolve (1.0)

    V "I'm sorry [player_name].. I was very clumsy.."

    A "It's okay Veronica. Don't beat yourself up for such a little matter.."

    scene scene_47-15 with Dissolve (1.0)

    V "You need to get changed soon.. You can't go out like this."


    window hide

    scene scene_47-14 with Dissolve (1.0)
    scene scene_47-15 with Dissolve (0.5)
    scene scene_47-14 with Dissolve (0.5)
    scene scene_47-15 with Dissolve (0.5)
    scene scene_47-14 with Dissolve (0.5)
    scene scene_47-15 with Dissolve (0.5)

    A "(This is getting awkward. She is rubbing on top my penis and it's getting hard so fast.
       It's only a matter of time before notices a giant hardon)"

    A "(I need to stop her but this feels good)"

    scene scene_47-14 with Dissolve (0.5)
    scene scene_47-15 with Dissolve (0.5)
    scene scene_47-14 with Dissolve (0.5)
    scene scene_47-15 with Dissolve (0.5)
    scene scene_47-14 with Dissolve (0.5)
    scene scene_47-15 with Dissolve (0.5)
    scene scene_47-14 with Dissolve (0.5)
    scene scene_47-15 with Dissolve (0.5)

    A "(FUCK!! It's fully erect by now)"

    scene scene_47-16 with Dissolve (1.0)

    V "*Gasp* Oh.."

    A "(Shit!! She noticed my boner!)"

    A "(What do I do now?!)"

    scene scene_47-17 with Dissolve (1.0)

    S "How long does it take clean? You'll make him impotent if you rub on him so much.."

    A "(WHAT THE HELL SELINA?!)"

    scene scene_47-18 with Dissolve (1.0)

    V "I..I..It's done.. You better get changed [player_name].."

    scene scene_47-19 with Dissolve (1.0)

    A "(I can see she is so embarrassed right now. I should have done it myself)"

    scene scene_47-20 with Dissolve (1.0)

    V "What's up with you Selina? You've been awfully quite.
       Did you two fight or something?"

    jump veronicadadpolice

    # if alan clean

label alanclean:

    A "It's okay. I'll do it. Don't worry about it."

    scene blackscreen with Dissolve (1.0)

    "You clean yourself"

    scene scene_47-21 with Dissolve (1.0)

    V "You better get changed [player_name].. You don't want to catch cold at night. It gets worse."

    A "I will.."

    scene scene_47-20 with Dissolve (1.0)

    V "What's up with you Selina? You've been awfully quite.
       Did you two fight or something?"

    jump veronicadadpolice



    # Scene 48

    # Veronica Dad Police Scene


label veronicadadpolice:

    "*Crank* Door opens"

    scene scene_48-1 with Dissolve (1.0)

    V "Hi Adam.."

    A "Oh.. Hi [Dad_name]."

    DA "Someone came to meet you.."

    A "Who?"

    scene scene_48-2 with Dissolve (1.0)

    Po "Hello Mr. [player_name]."

    scene scene_48-3 with Dissolve (1.0)

    DA "The police department sent him to investigate on the case. My friend has decided to give this case full priority.
        We can head home after this.."

    scene scene_48-4 with Dissolve (1.0)

    V "Selina.. Will you please step outside for a while?"

    scene scene_48-5 with Dissolve (1.0)

    S "Wait! Why do I need to go out? What's going on? What are you going to do to [player_name]?!"

    scene scene_48-6 with Dissolve (1.0)

    DA "Calm down love bird.. He won't do anything to [player_name]. The officer will just ask few questions.
        And it's going to be a boring one. You don't wanna listen to it.."

    S "Aahh alright.."

    scene scene_48-7 with Dissolve (1.0)

    "Selina left"

    Po "So shall we start Mr. [player_name]?"

    A "Yes. Go ahead please.."

    scene scene_48-8 with Dissolve (1.0)

    A "(This sofa has enough space but you are sitting right next to her and touching her waist.
       Aren't you ashamed of yourself?!)"

    scene scene_48-9 with Dissolve (1.0)

    A "(Look how he is trying to tease me! [Aunt_name] said he knew about [Mom_name]'s affection towards me.
       So he must despise me a lot.. Asshole)"

    scene scene_48-10 with Dissolve (1.0)

    Po "I have already gone through the details given by your doctor and the witnesses.
        There's a specific part that everyone seemed to have missed. I would like to know if you can shed any light on it."

    A "Well what is it?"

    scene scene_48-11 with Dissolve (1.0)

    Po "We have gone through the cameras set outside of both Mr. Jason's house and Mrs. Veronica's house.
        We have noticed a female person hanging around both houses. At the same time. So we are pretty sure they are twins."

    Po "After going through all the criminal records, we can confirm that they aren't listed as criminals."

    Po "But we would like to if you can recognise either of them. Could be someone you know.
        We aren't already thinking of them as the perpetrators but they are under our suspect list."

    Po "Here's a photo taken from Mr. Jason's house."

    scene scene_48-12 with Dissolve (1.0)

    A "(Could be anybody. If [Aunt_name] is right then they are doubting on innocent people)"

    A "Okay I'll take a look."

    scene scene_48-13 with Dissolve (1.0)

    A "(Hmm.. Doesn't look like anyone that I know. She is hot though)"

    A "Sorry officer. I haven't seen her before."

    scene scene_48-14 with Dissolve (1.0)

    Po "I see."

    Po "Well then. Thanks for your time Mr. [player_name]."

    Po "I hope you can get back to your everyday life."

    Po "If there's any advances, we will let you know."

    Po "I'll take my leave."

    A "Okay. Thank you officer."

    scene scene_48-15 with Dissolve (1.0)

    DA "I'll go fill up the paper works. We are leaving soon."

    scene scene_48-16 with Dissolve (1.0)

    V "[player_name] get ready. We are heading home. I'll get Selina.."

    A "Okay Veronica.."

    scene blackscreen with Dissolve (1.0)

    A "(Time to head home)"

    $ veronica_hospital = True

    jump map



    # Scene 49

    # Veronica Dad Alan Devil Scene

    $ veronica_alan_room = False


label veronicaalanroom:


    scene scene_49-1 with Dissolve (1.0)

    V " Well everything seems to be in place."

    V "Do you need anything [player_name]?"

    A "No I'm good. Thanks."

    scene scene_49-2 with Dissolve (1.0)

    V "Okay then. You should go to sleep. You had a rough ride."

    A "Will you be staying here tonight?"

    scene scene_49-3 with Dissolve (1.0)

    V "Uh no honey. Selina is all alone at home. You know how she is."

    A "Yeah. A scaredy cat."

    V "Yeah that. I'll take my leave then. Take care. I'll see you tomorrow."

    A "Thanks for taking such good care of me Veronica."

    V "Anything for you honey."

    scene scene_49-4 with Dissolve (1.0)

    V "Mwah"

    V "Bye."

    $ veronica_alan_room = True

    scene scene_49-5 with Dissolve (1.0)

    A "Well I'm all alone again."

    $ veronica_alan_room = True

    scene alanroomnight

    call screen alanroom


label veronicadaddevil:

    "Inaudible sound coming"

    scene scene_49-6 with Dissolve (1.0)

    A "(I thought she left already. What are they doing now? Can't hear anything properly)"

    scene scene_49-7 with Dissolve (1.0)

    A "(Hope I don't get noticed)"

    scene scene_49-8 with hpunch

    A "(WHAT THE FUCK!!!)"

    DA "Oh come on Veronica. You have seen me like this way too many times)"

    DA "All I'm asking for is just one night."

    scene scene_49-9 with Dissolve (1.0)

    V "You are just impossible Adam!"

    V "You are back to your old self right after we decided to get back together. Can't you be a bit more respectful?"

    scene scene_49-10 with Dissolve (1.0)

    DA "What can I do honey? I'm addicted to you. I promise that this is the last time.
        I won't touch you again unless you let me."

    V "NO! Adam stop!"

    scene scene_49-11 with Dissolve (1.0)

    DA "Trust me Veronica. I'm a better person now. Just give me a chance to show you.."

    V "Adam..."

    DA "Trust me..."

    A "(NO!! DON'T LET HIM VERONICA!!)"

    scene scene_49-12 with Dissolve (2.0)

    V "I can't believe this."

    DA "You don't have to say anything. Just let me show you how much you mean to me.."

    scene scene_49-13 with Dissolve (1.0)

    DA "You are still so gorgeous. I can't get enough of your breath taking beauty.."

    V "uuhmmm...Ada...mmmm"

    DA "I love you Veronica. I always did and will always do.."

    scene scene_49-14 with Dissolve (1.0)

    V "You're so hard. God I've missed this.."

    D "I missed these too.."

    V "Will you please turn the lights off except for the dim light?"

    DA "As your wish honey.."

    scene scene_49-15 with Dissolve (1.0)

    DA "Your wish has been granted my lady.. Now where were we?"

    A "(This has gone too far. What should I do?)"

menu:

    "Stop them [gr]\[AlanIntervene\]":

        $ alanintervene = "yes"

        jump ifalanintervene

    "Just leave":

        $ alanintervene = "no"

        jump ifalanleave


    # if alan intervene

label ifalanintervene:

    scene scene_49-16 with vpunch

    A "STOP!!!!"

    A "HOW COULD YOU?!!"

    scene scene_49-17 with Dissolve (1.0)

    A "How could you forget mom just like that?! It hasn't even been a day and you are already trying to sleep with her?!"

    A "You are such a pathetic human being!!"

    A "How dare you?!!"

    scene scene_49-18 with Dissolve (1.0)

    V "[player_name] please calm down. It's my fault. Don't say anything to him. Please."

    A "It's not your fault. It's that motherfucker's fault!"

    V "Stop it [player_name]! You're not making this any better. I'll just leave. Please don't fight.
       You just came back from hospital. Don't stress yourself."

    A "I'm not leaving unless this motherfucker apologises to you and [Mom_name]!"

    scene scene_49-19 with Dissolve (1.0)

    DA "You've said enough you brat!! Threatening me while living under my own roof!!"

    DA "Know your limits!! You are this close to crossing the line!"

    scene scene_49-20 with Dissolve (1.0)

    V "Adam! He is a kid. Let's stop this right here. Please."

    scene scene_49-21 with Dissolve (1.0)

    A "Oh yeah?!! What are you going to do if I cross the line?! Are you going to beat me up?!"

    A "Do you think I'll hold back after all the things you've done?!! YOU ASSHOLE!!!"

    scene scene_49-22 with hpunch

    DA "THAT'S IT!! YOU'VE JUST CROSSED THE LINE!! I'M GONNA KILL YOUR SORRY ASS!!!"

    scene scene_49-23 with Dissolve (1.0)

    V "NOOOO!!! STOP!!!!"

    scene scene_49-24 with Dissolve (1.0)

    DA "Nobody dares to ra..."

    scene scene_49-25 with vpunch

    DA "UUUgghhhhhhhhhh....."

    V "ADAM!!!"

    if renpy.loadable("patch.rpy") or patch:

        A "DAD!! WHAT THE FUCK!!!"

    if not renpy.loadable("patch.rpy"):

       A "ADAM!! WHAT THE FUCK!!!"


    scene scene_49-26 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:

        D "NOBODY TOUCHES MY DADDY!!!!"

    if not renpy.loadable("patch.rpy"):

        D "NOBODY TOUCHES HIM!!!!"

    scene scene_49-27 with Dissolve (1.0)

    V "AAAAAAHHHHHH NOOOOOOOO....!!!!"


    jump dadjourneytodark


    # if alan leaves

label ifalanleave:

    scene scene_49-28 with Dissolve (1.0)

    A "(I have seen enough. This is pathetic)"

    A "(I'll fucking kill you! How could you do this to [Mom_name]?!)"

    A "(How could you?!)"

    V "AAAAAAAAAAAAAAAAAAAA.....!!!!!" with hpunch

    A "WHAT THE FUCK!"

    scene scene_49-29 with Dissolve (1.0)

    A "VERONICA!!"

    A "WHAT'S WRONG?!"

    scene scene_49-30 with hpunch

    A "WHAT THE FUCK?!!!!"

    DA "Ukkh..kkkhh..."

    A "WHO ARE YOU?!!!"

    A "LET HIM GO!!! NOW!!!"

    V "PLEASE DO SOMETHING!!!"

    if renpy.loadable("patch.rpy") or patch:

        A "DAD!!"

    if not renpy.loadable("patch.rpy"):

        A "ADAM!!"

    scene scene_49-31 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:

        D "SHE ONLY BELONGS TO DADDY!!!"

    if not renpy.loadable("patch.rpy"):

        D "IT'S TIME FOR YOU TO JOIN HER!!!"

    "**CRACK**"

    scene scene_49-32 with hpunch

    A "NOOOOOOOOOO!!!!!"

    D "AAAHHHAHAHA AHHHAAHHAHA..."

    scene scene_49-33 with Dissolve (1.0)

    V "OH GOOOOOOOD!!! NOOOOOOO!!!!"


    jump dadjourneytodark
