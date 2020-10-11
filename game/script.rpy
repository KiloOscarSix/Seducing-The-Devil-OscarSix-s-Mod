# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define config.version = "0.9"

define patch = renpy.loadable("patch.rpy")


image splash = "gui/splash.png"
image warning = "gui/warning.png"
image thanks = "gui/thanks.png"


image main_menu = Movie(play="gui/main_menu.ogv")


label splashscreen:
    return #Fix
    scene warning with dissolve
    pause

    scene splash with dissolve
    pause

    scene thanks with dissolve
    pause

    return

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    add Movie(size=(1920, 1080))
    on "show" action Play("movie", "gui/main_menu.ogv", loop=True)
    on "hide" action Stop("movie")
    on "replace" action Play("movie", "gui/main_menu.ogv", loop=True)
    on "replace" action Play("music", "music/menu_music.mp3", loop=True)
    on "replaced" action Stop("movie")

    if renpy.loadable("patch.rpy") or patch:
        imagebutton auto "gui/patched_%s.png" xpos 0 ypos 0 focus_mask None action NullAction()

    vbox:
        pos (60, 343)
        spacing 15

        imagebutton auto "gui/start_%s.png" focus_mask None action Start()
        imagebutton auto "gui/load_%s.png" focus_mask None action ShowMenu('load')
        imagebutton auto "gui/preferences_%s.png" focus_mask None action ShowMenu('preferences')
        imagebutton:
            idle "/oscarAdditions/images/galleryIdle.png"
            hover "/oscarAdditions/images/galleryHover.png"
            action [Show("sceneGalleryMenu"), ui.callsinnewcontext("galleryNameChange")]
        imagebutton auto "gui/about_%s.png" focus_mask None action ShowMenu('about')
        imagebutton auto "gui/quit_%s.png" focus_mask None action Quit()

    imagebutton auto "gui/patreon_%s.png" xpos 1650 ypos 60 focus_mask None action OpenURL("http://www.patreon.com/deafperv")
    imagebutton auto "gui/discord_%s.png" xpos 1710 ypos 117 focus_mask None action OpenURL ("https://discord.gg/Xqegp4Z")


#default player_name = "???"
#default Mom_name = "Mom"
#default Aunt_name = "Aunt"
#default Dad_name = "Dad"


define ellaonlychoice = False

define verselonlychoice = False

define elselverchoice = False

define verselelchoice = False


define DA = Character("[Dad_name]", color = "#a9a9a9")
    # Father/Adam
define MO = Character("[Mom_name]", color = "#ffb6c1")
    # Mother/Rachel
define RA = Character('Rachel', color = "#ffb6c1")
    # Mother/Rachel
define D = Character('Devil', color = "#ff0000")
    # The Devil
define D2 = Character('Devil', color = "#dda0dd")
    # Devil 2
define D3 = Character('Devil', color = "#a0522d")
    # Devil 3
define A = Character("[player_name]")
    # Main Character
define S = Character('Selina', color = "#228b22")
    # Alan's Best Friend
define V = Character('Veronica', color = "#ffd700")
    # Selina's Mother
define Na = Character('Narrator', color = "#800080")
    # Narrator
define J = Character('Jason', color = "#c0c0c0")
    # Alan's Best Friend
define R = Character('Riley', color = "#a52a2a")
    # Jason's Sister
define K = Character('Kylie', color = "#483d8b")
    # Jason's Mother
define C = Character('Cathy', color = "#9932cc")
    # Selina's Friend
define E = Character('Ella', color = "#ff1493")
    # Alan's Girlfriend
define M = Character('Madison', color = "#ffe4e1")
    # Ella's Mother
define N = Character ('Nathan', color = "#f5f5f5")
    # Madison's Husband
define B = Character('Becky', color = "#87ceeb")
    # Ella's Elder Sister
define G = Character('George', color = "#00ff7f")
    # Becky's Husband
define L = Character('Lilith', color = "#ee82ee")
    # Ella's Younger Sister
define T = Character('Tana', color = "#556b2f")
    # Strip Club Girl
define P = Character('Poppy', color = "#556b2f")
    # Tan Salon Girl
define Be = Character('Bethany', color = "#dda0dd")
    # Airhostess
define DI = Character("[Aunt_name]", color = "#9acd32")
    # Aunt/Diana
define Un = Character('???', color = "#1e90ff")
    # Unknown
define UN = Character('???', color = "#9400d3")
    # Unknwon 2
define DG = Character('Goddess Lileva', color = "#9400d3")
    # Mother Devil
define Do = Character('Doctor', color = "#a52a2a")
    # Doctor
define Po = Character('Police Officer', color = "#008000")
    # Police Officer
define Re = Character('Receptionist', color = "#008000")
    # Hotel Receptionist
define Dr = Character('Driver', color = "#a52a2a")
    # Driver
define O = Character('Olivia', color = "#556b2f")
    # Airlines President



define flash = Fade(0.5, 0.5, 0.5, color="#fff")
define flash2 = Fade(0.1, 0.0, 0.5, color="#fff")

# The game starts here.

label start:

    if renpy.loadable("patch.rpy") or patch:

        $ Mom_name="Mom"

    if renpy.loadable("patch.rpy") or patch:

        $ Dad_name="Dad"

    if renpy.loadable("patch.rpy") or patch:

        $ Aunt_name="Aunt"


    if not renpy.loadable("patch.rpy"):

        $ Mom_name="Rachel"

    if not renpy.loadable("patch.rpy"):

        $ Dad_name="Adam"

    if not renpy.loadable("patch.rpy"):

        $ Aunt_name="Diana"

    stop music

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    scene scene_0-1 with Dissolve(1.0)
    pause

    scene scene_0-2 with Dissolve(1.0)
    pause

    scene scene_0-3


menu:

    Na "Are you old enough to play adult games?"

    "NO":
        jump exit

    "YES":
        jump enter


label exit:

    Na "Oh well. You may leave now and come back once you are old enough."

    return

label enter:

    Na "Well then.. You may enter the game"

    jump begin


    # SCENE 1

label begin:

    scene introduction1 with Dissolve (1.0)

    "Hello there!"

    "Welcome to the game where we get to fuck whoever we want. Crazy, isn't it?"

    "Before we start let's take a moment to get to know each other.."

    scene introduction3 with Dissolve (1.0)

    "Strange.."

    "But I'm You! And you are Me!"

    "Hmmm.."

    scene introduction1 with Dissolve (1.0)

    "Oh well.. Whatever.. Let's sort out a few things before we start.."

    "So we have a name.."

    $ player_name = renpy.input("And that name is")
    if player_name == "":
        $ player_name="Alan"

    A "Yes.. [player_name].. I think we are syncing up perfectly."

    scene introduction3 with Dissolve (1.0)

    A "So.. Here's how the things are right now."

    A "You are [player_name]. A young 22 year old English guy.

       You have an online relationship with a beautiful American girl Ella."

    A "You still haven't met each other but it's about time you do."


    if renpy.loadable("patch.rpy") or patch:

        A "You are currently living with your friend Selina and her mother Veronica.
           They are a bit ummm handful."

        A "Where are your dad and mom?"

        A "Well that's something we'll find out very soon."


    if not renpy.loadable("patch.rpy"):

        A "You are currently living with your friend Selina and her housemate Veronica.
           They are a bit ummm handful."

        A "Why are you living with them?"

        A "Well that's something we'll find out very soon."

    scene introduction4 with Dissolve (1.0)

    A "We have a very bumpy ride ahead."

    A "Things will get confusing as we keep moving forward. But bear with me and the guy making this game."

    A "There'll be multiple time jumps. In fact, we are going to start from a future point. And then we will
       go back to the past to find out how things got the way they are."

    A "Please pay attention to everything. Don't miss out on any clues or hints."

    A "It's already very confusing but the guy up there is adamant on making his game this way."

    A "And oh.. Deafperv has been constantly working on the character models. So don't panic if you see a different face on me all of a sudden."

    A "This game has 4 different paths. Each has a different story and characters."

    A "Every choice you make will steer you towards one of these paths."

    A "The first half of the game is pre-determined. You'll only get to make very few choices.
       But they will still matter a lot so don't get disheartened if you think the game is too linear."

    A "Just wait for the game to split in 4 different major branches."

    scene introduction3 with Dissolve (1.0)

    A "Now let's get ready.."

    A "It's time.."

    A "Gotta fuck em' all.."


    scene blackscreen with Dissolve (1.0)
    pause

    scene episode1 with Dissolve (1.0)

    pause

    "Present Day"
    label galleryScene1:
    scene 1-1 with Dissolve(1.0)

    "...mmmmhhm..."

    "...mmmm..."

    "uckk..kkhhaa.."

    "**slurp** **slurp**"


    scene 1-2 with Dissolve(1.0)

    A "Huh.. what? what's going on?"

    scene 1-3 with Dissolve(1.0)

    S "Good morning babe! You taste so good today."

    S "Look how it's twitching mhhhmm."

    scene 1-2 with Dissolve(1.0)

    S "mmmmmm..ahhh..*slurp* *slurp*"

    A "What the hell Selina?!"

    A "Veronica's at home and it's almost breakfast time. What if she comes and sees us like this?"

    scene 1-4 with Dissolve(1.0)

    S "Do you hate me for doing this every morning?"

    A "What!.. No!.. no I don't. But I wish you'd find a more appropriate time."

    scene 1-5 with Dissolve(1.0)

    A "(sigh)"

    A "Okay go on babe."

    scene 1-6 with Dissolve(1.0)

    A "(I'm terrible at acting. I don't want her to stop)"

    scene 1-3 with Dissolve(1.0)

    if renpy.loadable("patch.rpy") or patch:
        S "Then you need to finish off fast.
        I'm not letting go of your big hard cock until you blow your load all over my face.
        And who cares about what mom sees anyway."

    if not renpy.loadable("patch.rpy"):
        S "Then you need to finish off fast.
        I'm not letting go of your big hard cock until you blow your load all over my face.
        And who cares about what Veronica sees anyway."


    scene 1-2 with Dissolve(1.0)



    S "*slurp* *mmm* *slurp* *ummh*"

    A "(Lately she's been doing this very frequently)"


    if renpy.loadable("patch.rpy") or patch:
        A "(The thought of getting caught by her own mother excites her.
        It turns her on so much that one day she decided to give me a footjob at the dinner table.
        I barely managed to escape from Veronica's eyes)"

    if not renpy.loadable("patch.rpy"):
        A "(The thought of getting caught by Veronica excites her.
        It turns her on so much that one day she decided to give me a footjob at the dinner table.
        I barely managed to escape from Veronica's eyes)"



    scene 1-7 with Dissolve(1.0)

    A "Oh damn Selina! What's gotten into you today?"

    scene 1-8 with Dissolve(1.0)

    A "(She is taking me to the edge.
      I can't hold on for much longer.
      She's being extra careful with her moves today)"

    if renpy.loadable("patch.rpy") or patch:
        S "You owe me this after everything you've told us last night!
        Tonight I'll fuck you so hard that your balls will fall off.
        And I'll make sure mom gets a really nice view mmhhmmm **slurp** **slurp**."


    if not renpy.loadable("patch.rpy"):
        S "You owe me this after everything you've told us last night!
        Tonight I'll fuck you so hard that your balls will fall off.
        And I'll make sure Veronica gets a really nice view mmhhmmm **slurp** **slurp**."

    window hide

    image animation1-1 = Movie(channel="animation1-1", play="video/animation1-1.webm", start_image="animation1-1", image="animation1-1")
    scene animation1-1 with dissolve:
        size (config.screen_width, config.screen_height)

    #image selinablow01 = Movie(channel="selinablow01", play="video/selinablow01.webm")
    #scene selinablow01 with dissolve:
        #size (config.screen_width, config.screen_height)


    if renpy.loadable("patch.rpy") or patch:
        A "(I can tell she's just teasing to make me cum faster.
        She somehow figured out that her mother gives me a hard on.
        Huuh what have I gotten myself into?)"


    if not renpy.loadable("patch.rpy"):
        A "(I can tell she's just teasing to make me cum faster.
        She somehow figured out that Veronica gives me a hard on.
        Huuh what have I gotten myself into?)"

    A "I'm almost there. Fuck fuck fuck!!"

    scene 1-9 with Dissolve(1.0)

    S "Are you going to cum for me baby?"

    S "Come on then! Cum on my pretty little slutty face!"

    "The sultry tone of her voice pushes you over the edge."

    A "Fuck! Can't!!! ANYMORE!!! AAAHHHHHH!!"

    scene 1-10
    with vpunch

    A "OH BABEEE!!!"

    scene white with dissolve
    $ renpy.pause(0.7, hard = True)

    scene 1-11 with Dissolve(1.0)

    "You blast your load all over her face and her eyes start glowing."

    S "Oh my god!! It's so much.. Ummm... Yummm.."

    S "You came so much for me babe. Let me taste you now mmmmmm."

    scene 1-12 with Dissolve(1.0)

    "She moans with pleasure while licking off every bit of semen from your dick."

    "Your eyes roll over. You just can't think of a better way to start the morning."

    scene 1-13 with Dissolve(1.0)

    S "You did good, [player_name]. I know you love waking up like this despite what you said. Thanks for not pushing me away."

    if renpy.loadable("patch.rpy") or patch:
        A "Shusshh baby. You know I'll never reject you.
        It's just that I don't want things to get awkward with your mom.
        Thanks for.. ahh emm.. doing this. Bet today will be great!"

    if not renpy.loadable("patch.rpy"):
        A "Shusshh baby. You know I'll never reject you.
        It's just that I don't want things to get awkward with Veronica.
        Thanks for.. ahh emm.. doing this. Bet today will be great!"

    S "I'm sure it will. Even Jason doesn't get to wake up this way."

    A "Uhh,, yeah.."

    A "(If she only knew...)"


    if renpy.loadable("patch.rpy") or patch:
        A "Now I need to take a shower. Go down and keep Veronica occupied. I'll join you soon.
        Don't want your mom to start suspecting things.
        And don't forget to wash your face."


    if not renpy.loadable("patch.rpy"):
        A "Now I need to take a shower. Go down and keep Veronica occupied. I'll join you soon.
        Don't want her to start suspecting things.
        And don't forget to wash your face."

    scene 1-14 with Dissolve(1.0)

    S "Alright alright babe. I'm going. Take your shower and think of me while jerking off hihihi."

    A "You bet I will *giggle*.
       Love you Selina."

    S "Love you too [player_name]."
    $ renpy.end_replay()
    scene blackscreen with Dissolve(1.0)

    A "(Aaah this girl!.. She drives me crazy)"


menu:

    "Take a shower":
        with dissolve
        jump shower

    # SCENE 2

label shower:

    scene 2-1 with Dissolve(1.0)

    A "(Damn, she really did a number on me! Now I gotta take care of this problem)"

    A "(Or I can just leave it like this.
       It's not like this boner is going away anytime soon.
       Maybe I could try teasing Veronica with this.
       I'm pretty sure she'll give me an earful for what I said last night)"


menu:

    "Jerk off":
        $ boner = "none"
        with dissolve
        jump fap

    "Just take a shower [gr]\[Boner\]":
        $ boner = "hardon"
        with dissolve
        jump nofap

label fap:

    image animation1-2 = Movie(channel="animation1-2", play="video/animation1-2.webm", start_image="animation1-2", image="animation1-2")
    scene animation1-2 with dissolve:
        size (config.screen_width, config.screen_height)


    #image showermustarbate01 = Movie(channel="showermustarbate01", play="video/showermustarbate01.webm")
    #scene showermustarbate01 with dissolve:
        #size (config.screen_width, config.screen_height)

    A "(Oh baby)"

    A "(You dirty little slutty girl. I'll pound your dirty pussy so hard tonight)"

    A "(The whole neighborhood will hear you screaming)"

    if renpy.loadable("patch.rpy") or patch:
        A "(Even your own mother won't be able to resist watching us fuck)"

    if not renpy.loadable("patch.rpy"):
        A "(Even Veronica won't be able to resist watching us fuck)"

    A "(Do you want my cum honey?)"

    A "(Do you want me to spray all over your pretty face?)"

    if renpy.loadable("patch.rpy") or patch:
        A "(Why don't you ask your mom to join us?)"

    if not renpy.loadable("patch.rpy"):
        A "(Why don't you ask Veronica to join us?)"

    A "(I'll blow my load on both of your pretty faces)"

    A "(mmmmmmmm...mmmmm)"

    A "(FUCK!! Here you go girls!!)"

    scene 2-2
    with vpunch

    A "(AAAHH!!)"
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)

    scene 2-3 with Dissolve(1.0)

    A "(Damn I came so much again! Where did all that come from?)"

    A "(The thoughts about Veronica are getting stronger day by day.
       Don't know how much longer I can resist)"

    A "(I need to hurry up now)"

    A "(A morning shower after a freaking great blowjob feels so nice)"

    scene blackscreen with Dissolve(1.0)
    jump diningroom

label nofap:

    scene blackscreen with Dissolve (1.0)

    jump diningroom

    # SCENE 3

label diningroom:


    "You take a shower for half an hour and then head towards the dining room."

    "You enter the dining room."

    scene 3-1 with Dissolve(1.0)

    "Veronica and Selina are already there waiting for you."

    A "(I haven't been able reach Ella for the past 12 hours. For some reason the network there is pretty bad right now.
       She can't come online either.
       I miss her so much already)"

    V "Good morning [player_name]"

    A "(Veronica isn't wearing her bra again. Damn! I want to bury my face in those knockers!)"

    S "[player_name]."

    A "(She's been acting a bit weird for a while. Always wearing skimpy outfits.
       I don't blame her though since I've led her on.
       Now the only thing missing is my dick between her tits)"

    S "HELLO!!! EARTH TO MR. [player_name]!! IS ANYBODY THERE?!"

    A "(Huh! I spaced out again. So embarassing!)"

    A "Oh hey!"

    A "Good morning Veronica. Good morning Selina."

    S "Good morning babe!"

    scene 3-2 with Dissolve(0.5)

    "She gives you a wink"

    scene 3-3 with Dissolve(1.0)

    if renpy.loadable("patch.rpy") or patch:
        V "Oh Selina! I get that you both are childhood friends but don't call him babe.
        It's not appropriate. You could've been step siblings if his dad didn't decide to leave us out of the blue.
        Besides I'm sure Jason won't like it if he finds out. You are dating, remember?"

        S "Come on mom! Jason wouldn't mind.
        It's just a friendly joke I make since this ''could've been step son'' of yours can't even get a REAL girlfriend."


    if not renpy.loadable("patch.rpy"):
        V "Oh Selina! I get that you both are childhood friends but don't call him babe.
        It's not appropriate. Besides I'm sure Jason won't like it if he finds out. You are dating, remember?"

        S "Come on Veronica! Jason wouldn't mind.
        It's just a friendly joke I make since this kid here can't even get a REAL girlfriend."

    A "(Damn she had to bring that up. Specially after what I've told them last night.
      This isn't gonna go great)"

    V "About that..."

    A "(Here we go...)"

    scene 3-4 with Dissolve(1.0)

    V "[player_name], I'm really really mad. I didn't expect such things from you.
       What were you thinking? I was so shocked."

    if renpy.loadable("patch.rpy") or patch:
        S "Mom, can't this wait?"

    if not renpy.loadable("patch.rpy"):
        S "Veronica, can't this wait?"

    A "Yeah let's at least finish breakfast first."

    scene 3-5 with Dissolve(1.0)

    V "FINE!! But we are going to have a talk right after this."

    A "Sure honey."

    V "No honey bunny..!!"

    S "*giggle*"

    A "Okay honey.."

    A "(I know she likes it.. Gotta play it smooth)"

    A "(Time to bust out my sweet talking skills again)"

    scene 3-6 with Dissolve(1.0)

    if renpy.loadable("patch.rpy") or patch:
        S "Thanks for the food mom."

    if not renpy.loadable("patch.rpy"):
        S "Thanks for the food Veronica."

    A "Yeah it was delicious."

    V "Now now.. You don't need to be so sweet. Clean your plates and meet me in the living room."

    V "Both of you!"

    A "(sigh)"

    A "We'll be with you soon."

    S "Be right there."

    with dissolve

    # SCENE 4

    scene 4-1 with Dissolve(1.0)

    A "She's been too harsh on me for such a little issue."

    scene 4-2 with Dissolve(1.0)

    S "Really [player_name]?"

    S "Is that really how you think of it? A little issue??"

    A "Come on babe! I'm a grown up now."

    A "I have the right to choose."

    scene 4-3 with Dissolve(1.0)

    if renpy.loadable("patch.rpy") or patch:
        S "Of course you do but try seeing it from mom's perspective as well."

    if not renpy.loadable("patch.rpy"):
        S "Of course you do but try seeing it from Veronica's perspective as well."

    scene 4-4 with Dissolve(1.0)

    A "I guess. Ahh whatever."

    S "Now now. I thought you said your day was gonna be great earlier.
       What's with that face then? Didn't you like my morning gift?"

    scene 4-5 with Dissolve(1.0)

    "She puts her hand on the bulge of your pant."

    scene 4-6 with Dissolve(1.0)

    A "It was great and I loved it babe. Don't worry about it."

    scene 4-7 with Dissolve(0.5)

    S "Happy to hear it sweety."

    scene 4-8 with Dissolve(1.0)

    A "We are done here. Let's go to the living room."
    with dissolve

    scene 4-9 with Dissolve(1.0)

    "As she takes a few steps forward you can't help but admire her ass from the back."

    scene 4-10 with Dissolve(1.0)

    "Like you always do."

    scene 4-11 with Dissolve(1.0)

    "She notices you checking out her butt."
    "and decides to shake it a little bit for you."

    window hide

    image animation1-3 = Movie(channel="animation1-3", play="video/animation1-3.webm", start_image="animation1-3", image="animation1-3")
    scene animation1-3 with dissolve:
        size (config.screen_width, config.screen_height)


    S "Feeling better now?"

    A "You bet I am babe."

menu:

    "Slap her butt [gr]\[Butt Stuff\]":

        $ selinabuttslap = "yes"

        jump slap

    "Go to the living room":

        $ selinabuttslap = "no"

        scene 4-11 with Dissolve (1.0)

        A "*giggles* Thanks for the butt show."

        A "Let's go to the living room now."

        S "*giggles* Sure babe.."

        jump living


label slap:

    scene 4-12
    with hpunch
    with Dissolve (1.0)

    "You slap her butt and grab a boob. She moans with pleasure."

    scene 4-13 with Dissolve (1.0)

    S "Uunhhh...Oh you naughty naughty boy. Not now. You can have them all for yourself tonight."

    scene 4-14 with Dissolve (1.0)

    "You move closer to her and press yourself onto her buttcheeks."

    scene 4-15 with Dissolve (1.0)

    A "**whispering** I'll fuck you so good tonight that you will forget Jason once and for all."

    S "Oh my! Somebody sounds jealous but.. umm.. I can't wait to see how you'll do that."

    scene 4-16 with Dissolve (1.0)

    "She kisses you on the lips."

    "The sweet taste of her lips leaves you breathless for a moment."

    scene 4-17 with Dissolve (1.0)

    "Selina leaves the kitchen and you follow her."


    # Scene 5


label living:

    scene 5-1 with Dissolve (1.0)

    "You enter the living room and sit beside Veronica."

    scene 5-2 with Dissolve (1.0)

    "You try to ease the tension by putting your arm around her neck."

    scene 5-3 with Dissolve (1.0)

    "She looks at you and smiles."

    V "[player_name], I'm sorry for lashing out at breakfast."

    A "Lashing out? Pfft.. Veronica.. it was nothing. You weren't rude at all."

    A "I can understand what you are feeling right now."

    scene 5-4 with Dissolve (1.0)

    V "1 whole month? Honey do you know how long that is?"

    V "I don't even remember living a day without you."

    A "The beach tri.."

    V "..and suddenly I discover that you have everything planned and we knew nothing about it."

    V "I'm just... This is so sudden and shocking."

    A "I know Veronica. I know. But I've waited too long already."

    S "Are you really, really serious about her?"

    scene 5-5 with Dissolve (1.0)

    A "Of course I am!"

    A "You guys already know everything."

    A "She waited 2 years for me to graduate.
       And now that I've finally done it, I think we can start moving forward."

    scene 5-6 with Dissolve (1.0)

    V "I've never been against your virtual relationship.
       Even though she is like 5 years older than you she has stayed loyal."

    V "At her age she should be settling down with someone. Not hooking up on the Internet."

    scene 5-7 with Dissolve (1.0)

    S "What if she already has? All we know about her is what she has shown us."

    scene 5-8 with Dissolve (1.0)

    A "Selina, please!"

    S "If she is really serious about you, how come she's not here?"

    A "You know that she has a full time job."

    scene 5-9 with Dissolve (1.0)

    S "What kind of job doesn't let you take a break? I'm sure she could take a week off if she really wanted.."

    A "It's complicated there. Also her family isn't entirely on board with this relationship."

    A "I need to meet them face to face and let them know I'm not some silly internet fling, you know?
       Show them it's a real, serious relationship."

    A "We just can't do everything through video calls."

    A "Living in two different countries is hard enough already."

    S "What do you mean by \"can't do everything\"?"

    S "Don't tell me you are dying to have sex with her?"

    scene 5-10 with Dissolve (1.0)

    "Selina giggles."

    scene 5-11 with Dissolve (1.0)

    "Veronica joins her as well."

    "You feel embarrassed because it is partially true. Ella is just too hot.
     Such a curvalicious body with big beautiful tits and a perfect, round ass."

    scene 5-12 with Dissolve (1.0)
    pause (1.0)

    scene 5-12:
        subpixel True
        yalign 1.0
        linear 7.0 yalign 0.0

    "Who wouldn't die to fuck such a hot girl?"

    "It drives you insane that despite having gotten such a girlfriend you can neither touch nor feel her."

    scene 5-13 with Dissolve (1.0)

    V "Cat got your tongue?"

    scene 5-14 with Dissolve (1.0)

    "Both of them burst into laughter."

    A "(Damn I need to come up with something real fast)"

    A "(I think I should take charge here. Can't just let Selina tease me like this. So what am I going to say?)"


menu:

    # Harem Path

    "Be bold [HaremPath]":
        jump bebold

    # Ella only path

    "Be calm [EllaPath]":
        jump calm


    # Scene 6

    # Path for Sel-Ver only & Sel-Ver-Ella

label bebold:

    A "Well yeah. Isn't that obvious?"

    A "I'm 22 now and guys of my age are already fathering kids while I'm sitting here with two ladies that I can't be intimate with."

    A "I have desires too and, yeah, guess what.. the first thing I'll do when I get there is fuck her brains out.
       What are you gonna do about it?"

    scene 6-1 with Dissolve (1.0)

    "Selina is shocked by your response"

    if renpy.loadable("patch.rpy") or patch:
        S "OH MY!! What's wrong with you [player_name]?
        Did you totally forget that mom's here?"

    if not renpy.loadable("patch.rpy"):
        S "OH MY!! What's wrong with you [player_name]?
        Did you totally forget that Veronica's here?"

    "Surprisingly Veronica isn't disturbed."

    scene 6-2 with Dissolve (1.0)

    "She pulls herself onto your chest and puts your arm on top of her belly."

    V "It's kinda true Selina. Back then, guys of [player_name]'s age were already in sexual relationships."

    V "He should expect things to be more intense now."

    V "But [player_name] has been such a loyal boyfriend and stayed true to the one he wants.
       I say he is a true gentleman."

    V "By the way, those were pretty obscene words [player_name]. I hope you won't use them again. But I do understand your situation."

    scene 6-3 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:
        S "Mom! What are you talking about?"

    if not renpy.loadable("patch.rpy"):
        S "Veronica! What are you talking about?"

    V "It's normal for a grown up male, Selina. Hot blood is always running through their brains and.. you know.. \"other parts\"."

    S "Penis?"

    scene 6-4 with Dissolve (1.0)

    V "Yeah that. I find it really hard to believe that a big, strong guy like [player_name] is still a virgin.
       It must be so hard for you down there, honey."

    S "Yeah right!"

    "You are utterly shocked by Veronica's words. You were trying to take charge here, instead she is the one leading the game."

    A "Uh huh.. I guess so.. I mean, hard, yeah.."


    # Scene 7


    # Sel-Ver Path
    if boner == "none":

        scene 7-1 with Dissolve (1.0)

        V "Maybe you should have just dated one of us hihihi."

        V "Then all your needs would have been taken care of."

        A "(WHAT THE?!)"

        scene 7-2 with Dissolve (1.0)

        if renpy.loadable("patch.rpy") or patch:
            S "MOM!"

        if not renpy.loadable("patch.rpy"):
            S "VERONICA!"

        scene 7-3 with Dissolve (1.0)

        V "Don't tell me you haven't seen his morning wood, honey.
        You even touched it once while he was sleeping if I'm not wrong."

        A "WAIT! She did what?!"

        if renpy.loadable("patch.rpy") or patch:
            S "Mom!! That was our secret!"

        if not renpy.loadable("patch.rpy"):
            S "VERONICA!! That was our secret!"

        V "Why are you acting so surprised [player_name]?"

        A "I uhh.."

        scene 7-4 with Dissolve (1.0)

        V "Haven't you been peeking on her when she's been showering?"

        A "(I'm FUCKED)"

        A "I uhh.. I wasn't peeking. I just wanted to take a leak."

        scene 7-5 with Dissolve (1.0)

        "Veronica makes a jerking off gesture with her hand."

        V "Yeah right.. Couldn't wait so you had to take your thing out right there and relieve yourself."

        if renpy.loadable("patch.rpy") or patch:
            S "What are you saying Mom?!"

        if not renpy.loadable("patch.rpy"):
            S "What are you saying Veronica?!"

        S "Why would he do such thing?"

        V "Like I told you sweetheart. Hot blood running through brain and manhood."

        V "But it was nice of him not to do anything else I guess. He kept his cool. I'll give you that, [player_name]"

        A "(Why is this happening?! My mind is completely blank right now! What's going on?!)"

        scene 7-6
        with vpunch

        "Veronica pushes you down and gets on top of you."

        V "So, [player_name].."

        A "Uh huh.."

        V "If you didn't have Ella, would you have dated one of us?"

        A "What!?"

        scene 7-7 with Dissolve (1.0)

        if renpy.loadable("patch.rpy") or patch:
            S "MOM!"
        if not renpy.loadable("patch.rpy"):
            S "Veronica!"

        V "What about me?"

        V "I have noticed you staring at my breasts whenever you think I'm not looking."

        A "No I haven't.. I'm just spacing out.. yeah spacing.."

        scene 7-8 with Dissolve (1.0)

        V "Do you want to touch them honey?"

        A "WHAT THE?!"
        with flash2

        if renpy.loadable("patch.rpy") or patch:
            S "Mom! Back off! He is mine!"

        if not renpy.loadable("patch.rpy"):
            S "Veronica! Back off! He is mine!"

        S "I told you to wait! But you aren't listening to me at all!"
        with flash2

        V "Come on [player_name]"

        scene 7-9 with Dissolve (1.0)

        V "Take me now."
        with flash2

        A "WHAT THE HELL?!"
        with flash2

        V "Touch them baby!"

        S "You fucking slut!"
        with flash2

        A "What's happening? OH GOD!!"
        with flash2

        "[player_name]!! [player_name]!! [player_name]!!"
        with flash2
        with flash
        with flash2
        hide 7-9

        jump devilappear1



    # Scene 8


    # Sel-Ver-Ella Path

    if boner == "hardon":
        scene 8-1 with Dissolve (1.0)

        V "Oh honey.. I wish I could help you but I can't."

        A "(Wait! Is she trying to flirt with me now? I'm confused.
        Why did she change all of a sudden?)"

        A "(Is it an attempt to make me stay here?)"
        scene 8-2
        with vpunch

        A "(Holy fuck!!)"

        A "(My plan worked!! She noticed my boner and  is putting pressure on it. All this sex talk must have made her wet and she isn't even bothered by my hard-on)"

        V "**Whispers** Your body is so warm uhhh.."

        S "Hey! What's going on over there?"

        A "(Should I make a move now?)"

        A "(At least I'd find out what her intentions are)"

menu:

    A "(Maybe this is a bad idea. So what is it gonna be?)"

    "Put your hand on her chest [RileyPath] [KyliePath]":
        $ chest = "hand"
        jump handchest

    "Use Selina":
        $ chest = "none"
        jump pushselina

    # Scene 9


     # Sel-Ver-Ella-Riley-Kylie path

label handchest:



    scene 9-1 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:
        S "What the hell are you doing [player_name]?! Why are you touching mom?!"

    if not renpy.loadable("patch.rpy"):
        S "What the hell are you doing [player_name]?! Why are you touching her?!"

    A "(They are so soft and big)"

    scene 9-2 with Dissolve (1.0)

    V "mmmmmhmpp.. Your touch feels so good [player_name]."

    scene 9-3 with Dissolve (1.0)

    S "What the fuck?!"

    scene 9-4 with Dissolve (1.0)

    "You untie her robe and start squeezing both boobs."

    A "Fucking hell! You look so wet honey."

    scene 9-5 with Dissolve (1.0)

    V "Oh [player_name]. I need you.. right now."

    V "Please [player_name]! I can't wait anymore. I've been wanting you for so fucking long!"

    if renpy.loadable("patch.rpy") or patch:
        S "WHAT THE FUCK!!! MOM!! ARE YOU GUYS FOR REAL?!!!"

    if not renpy.loadable("patch.rpy"):
        S "WHAT THE FUCK!!! VERONICA!! ARE YOU GUYS FOR REAL?!!!"

    A "(FINALLY!!)"

    S "OH MY FREAKING GOD!"

    A "(This is my chan...)"
    with flash2

    A "What the fuck?!"

    with flash2
    with flash
    hide 9-5

    jump devilappear2


    # Scene 10

    # Sel-Ver-Ella Path

label pushselina:

    A "You know what Veronica?"

    V "What honey?"

    A "Things aren't actually as bad as you think it is."

    scene 10-1 with Dissolve (1.0)

    V "What do you mean?"

    scene 10-2 with Dissolve (1.0)

    S "[player_name].."

    A "I've been fucking Selina for a while now.."

    scene 10-3 with Dissolve (1.0)

    V "WHAT?!"

    scene 10-4 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:
        S "[player_name]!! Mom I can explain!"

    if not renpy.loadable("patch.rpy"):
        S "[player_name]!! Veronica I can explain!"

    scene 10-5 with Dissolve (1.0)

    V "You guys have been fucking behind my back?"

    "Suddenly Veronica's language becomes very vulgar."

    scene 10-6 with Dissolve (1.0)

    A "Don't you wanna how it felt?"

    V "I.. uhh.. [player_name]!"

    S "What the fuck [player_name]?"

    scene 10-7 with Dissolve (1.0)

    A "Come on babe! Let's be realistic here. You have tried your level best to get caught."

    A "But you have failed everytime. Better I make things clear now. It's not like we are doing anything illegal."

    V "How could you both? What about Jason? Did you even think about him?"

    A "Jason knows everything."

    V "Wow! I am out of words!"

    A "She was blowing me just before breakfast. She said that it doesn't matter if you see us or not."

    S "[player_name].. That was just a joke!"

    scene 10-8 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:
        V "So my daughter wants me to see her fucking the only guy I have been dying to fuck?"

    if not renpy.loadable("patch.rpy"):
        V "So Selina wants me to see her fucking the only guy I have been dying to fuck?"

    A "WAIT WHAT?"

    if renpy.loadable("patch.rpy") or patch:
        S "Mom!"
    if not renpy.loadable("patch.rpy"):
        S "Veronica!"

    scene 10-9 with Dissolve (1.0)

    V "THAT'S FUCKING RIGHT! You are having two dicks to yourself and I don't even get one?!"

    if renpy.loadable("patch.rpy") or patch:
        S "Mom! What are you talking about?
        [player_name] say something!"

        V "Don't be so dense Selina. I've been trying every little thing just to get [player_name]'s attention!
        And this is what I get? My daughter fucking him!"

        S "Mom I.."

    if not renpy.loadable("patch.rpy"):
        S "Veronica! What are you talking about?
        [player_name] say something!"

        V "Don't be so dense Selina. I've been trying every little thing just to get [player_name]'s attention!
        And this is what I get? That you fucking him!"

        S "Veronica I.."

    V "Guess what? [player_name] already has a hard-on for me. LOOK!"

    scene 10-10
    with hpunch

    "Veronica pulls your shorts down and grabs on your raging boner."

    A "Oh fuck!"

    A "(Well that escalated so quickly)"

    if renpy.loadable("patch.rpy") or patch:
        S "Mom don't!"

    if not renpy.loadable("patch.rpy"):
        S "Veronica don't!"

    scene 10-11 with Dissolve (1.0)

    V "This is mine you little cunt!!"

    V "You had enough for yourself already!"

    if renpy.loadable("patch.rpy") or patch:
        A "Don't be rude to your daughter Veronica. Let her make it up to you.
        Come here babe"

    if not renpy.loadable("patch.rpy"):
        A "Don't be rude to her Veronica. Let her make it up to you.
        Come here babe."

    S "[player_name].. I..."

    scene 10-12 with Dissolve (1.0)

    V "Are you sure?"

    A "Yes I am honey. Honestly I've been wanting to get into your pants for a while.
       Selina knew about it. I think she kinda wanted us to fuck maybe."

    scene 10-13 with Dissolve (1.0)

    V "Is that true Selina?"

    if renpy.loadable("patch.rpy") or patch:
        S "Ayy ye yes yes mom.."

    if not renpy.loadable("patch.rpy"):
        S "Ayy ye yes yes Veronica.."

    A "Come here Selina. Don't just stand there."

    V "Didn't you hear what he just said? Come here young lady!"

    scene 10-14 with Dissolve (1.0)

    "Selina steps towards you while looking really nervous."

    scene 10-15
    with vpunch

    "Without prior warning Veronica starts working on your dick."

    A "Oh fuck veronica!"

    V "**slurp** **slurp** mmmhmmm mmm."

    scene 10-16 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:
        "You notice Selina getting turned on by her mother's move."

    if not renpy.loadable("patch.rpy"):
        "You notice Selina getting turned on by Veronica's move."

    A "Babe take off your clothes and sit beside me."

    "Selina starts feeling little more comfortable."

    scene 10-17 with Dissolve (1.0)

    "She takes of her clothes."

    "You can never get enough of such beauty."

    "She doesn't show any signs of being shy anymore."

    scene 10-18 with Dissolve (1.0)

    "Selina sits beside you."

    "You start rubbing her clit and Selina starts moaning with pleasure."

    A "The best fucking day ev..."
    with flash2

    A "What's going on?!"
    with flash2
    A "What the fuck?!"
    with flash
    with flash2
    hide 10-18

    jump devilappear2


    # Scene 11

label devilappear1:


    scene scene_11-1

    D "Hey hey baby!"

    D "Not so fast!"

    D "Did you think everything would be that easy? heh!"

    A "Your were again messing with my mind, weren't you?"

    A "And what is this? I don't even get a warning before you start doing your things!"

    scene scene_11-2 with Dissolve (1.0)

    D "Shut up!!"

    D "It's my turn now!"

    D "Now please me if you don't want your head chopped off!"

    scene scene_11-3 with Dissolve (1.0)

    A "How come you are still so tight after so many times?"

    scene scene_11-4 with Dissolve (1.0)

    D "unngghhh.."

    A "Feels like my dick is on fire aarghh!"

    D "SHUT UP!"

    window hide

    scene scene_11-3 with Dissolve (0.5)
    scene scene_11-4 with Dissolve (0.5)
    scene scene_11-3 with Dissolve (0.5)
    scene scene_11-4 with Dissolve (0.5)
    scene scene_11-3 with Dissolve (0.5)
    scene scene_11-4 with Dissolve (0.5)

    D "Oh yeah oh yeah!! mmhmmm!!"

    A "Fuck it's so tight! I can't hold on for much longer!"

    window hide

    scene scene_11-3 with Dissolve (0.5)
    scene scene_11-4 with Dissolve (0.5)
    scene scene_11-3 with Dissolve (0.5)
    scene scene_11-4 with Dissolve (0.5)
    scene scene_11-3 with Dissolve (0.5)
    scene scene_11-4 with Dissolve (0.5)

    A "I'm cumming! arrghhh!!"

    scene scene_11-5
    with vpunch

    D "Yes yes shoot it in my asshole mmhmmm!"

    A "aaaahhhhh...!"
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)

    scene scene_11-6

    A "huuuuuh huuuuh aahhhh...!"

    scene scene_11-7 with Dissolve (1.0)

    D "*laughter* you filled me up with your cum. mmmhhmm so thick mmmm...!"

    A "Thank me for not shooting my piss instead."

    D "*laughter* I won't mind."

    A "Eww gross!"

    scene scene_11-8 with Dissolve (1.0)

    D "mmhmm ummm you taste so good mmmm."

    D "A bit salty and smelly."

    A "Yeah I didn't eat anything good yesterday."

    D "Well you had something good just now. My ass is better than anything."

    A "In that case I won't mind having it again."

    A "Like right now."

    D "You must be kidding!"

    A "AGAIN!"

    scene scene_11-9 with Dissolve (1.0)

    D "NO!!"

    A "Bend over you fucking bitch!"

    scene scene_11-10
    with vpunch

    D "NO NO NO!! Arrgghhh!! Get off!!"

    A "Did you forget our deal? You fucking slutty bitch! You are my whore and I get to do whatever I want!"

    scene scene_11-11 with Dissolve (1.0)

    D "IT HURTS!!"

    A "Not tight anymore huh!"

    window hide

    scene scene_11-10 with Dissolve(0.5)
    scene scene_11-11 with Dissolve(0.5)
    scene scene_11-10 with Dissolve(0.5)
    scene scene_11-11 with Dissolve(0.5)
    scene scene_11-10 with Dissolve(0.5)
    scene scene_11-11 with Dissolve(0.5)
    scene scene_11-10 with Dissolve(0.5)
    scene scene_11-11 with Dissolve(0.5)

    D "Owh fuck! aahhh stop!! stop!!"

    scene scene_11-12 with Dissolve (1.0)

    A "Oh yes! This feels good mmmhmm!"

    D "No it doesn't!!"

    scene scene_11-13 with Dissolve (1.0)

    A "You are one the who started this!"

    D "And now I'm telling you to stop!! Gggghhhhhh noowwwhhhh!"

    window hide

    scene scene_11-12 with Dissolve (0.5)
    scene scene_11-13 with Dissolve (0.5)
    scene scene_11-12 with Dissolve (0.5)
    scene scene_11-13 with Dissolve (0.5)
    scene scene_11-12 with Dissolve (0.5)
    scene scene_11-13 with Dissolve (0.5)
    scene scene_11-12 with Dissolve (0.5)
    scene scene_11-13 with Dissolve (0.5)
    scene scene_11-12 with Dissolve (0.5)
    scene scene_11-13 with Dissolve (0.5)

    D "Be done with it already!"

    scene scene_11-14 with Dissolve (1.0)

    A "I'm cumming againnnn aaaarrgghhh...!"

    scene scene_11-15
    with vpunch
    with flash2


    A "mmmmhhmmm aaaahhhh!"

    scene scene_11-16
    with vpunch
    with flash2

    D "What have you done?!"

    scene scene_11-17 with Dissolve (1.0)

    A "Just made you my bitch!"

    scene scene_11-18 with Dissolve (1.0)

    D "**sniff** **sniff**"

    A "It is done."

    scene scene_11-19 with Dissolve (1.0)

    A "You are mine again.."

    A "I missed you.."
    $ renpy.end_replay()
    $ elselverchoice = True

    jump backstory


    # Scene 12

label devilappear2:

    if chest == "hand":

        scene scene_12-1

        D "Hey hey baby!"

        D "Not so fast!"

        D "Did you think everything would be that easy? heh!"

        A "Your were again messing with my mind, weren't you?"

        A "And what is this? I don't even get a warning before you start doing your things!"

        scene scene_12-2 with Dissolve (1.0)

        D "Shut up!!"

        D "It's my turn now!"

        D "Please me if you don't want your head chopped off!"

        A "You won't do anything like that since you are stuck with me."

        D "Don't test your luck boy! I'll fuck your corpse instead."

        A "*giggle* you're so cute."

        scene scene_12-3 with Dissolve (1.0)

        D "Oh my! Really? Don't start having ideas. You know what I'm capable of"

        scene scene_12-4
        with vpunch

        A "Oh really?!"

        D "FUCK!!"

        A "Did I just hear you moan now?"

        D "Don't kid yourself. You heard nothing"

        A "Oh I see...."

        scene scene_12-5 with Dissolve (1.0)

        A "Why are you pulling yourself away?"

        scene scene_12-4
        with vpunch

        D "To put it in again, you idiot!"

        A "aaahh mmhmm so tight and warm."

        D "aaaarrggghh mmhmmphh..."

        window hide

        scene scene_12-5 with Dissolve (0.5)
        scene scene_12-4 with Dissolve (0.5)
        scene scene_12-5 with Dissolve (0.5)
        scene scene_12-4 with Dissolve (0.5)
        scene scene_12-5 with Dissolve (0.5)
        scene scene_12-4 with Dissolve (0.5)
        scene scene_12-5 with Dissolve (0.5)
        scene scene_12-4 with Dissolve (0.5)
        scene scene_12-5 with Dissolve (0.5)
        scene scene_12-4 with Dissolve (0.5)
        scene scene_12-5 with Dissolve (0.5)
        scene scene_12-4 with Dissolve (0.5)

        D "Feels so good.. I love your big cock inside my pussy mmmhmmm.."

        scene scene_12-6 with Dissolve (1.0)

        A "I love the exotic smell of your feet."

        D "Mmmhmmmm suck on them like a good boy."

        scene scene_12-7 with Dissolve (1.0)

        A "mmmm mmmmm..."

        D "oh yeah.. .mmhmmm.."

        scene scene_12-8 with Dissolve (1.0)

        D "Do you like it mmmmhmmmm?"

        window hide

        scene scene_12-8 with Dissolve (1.0)
        scene scene_12-7 with Dissolve (0.5)
        scene scene_12-8 with Dissolve (0.5)
        scene scene_12-7 with Dissolve (0.5)
        scene scene_12-8 with Dissolve (0.5)
        scene scene_12-7 with Dissolve (0.5)
        scene scene_12-8 with Dissolve (0.5)
        scene scene_12-7 with Dissolve (0.5)
        scene scene_12-8 with Dissolve (0.5)
        scene scene_12-7 with Dissolve (0.5)

        A "uuhghghhh I'm almost there.."

        window hide

        scene scene_12-8 with Dissolve (0.5)
        scene scene_12-7 with Dissolve (0.5)
        scene scene_12-8 with Dissolve (0.5)
        scene scene_12-7 with Dissolve (0.5)
        scene scene_12-8 with Dissolve (0.5)
        scene scene_12-7 with Dissolve (0.5)
        scene scene_12-8 with Dissolve (0.5)
        scene scene_12-7 with Dissolve (0.5)

        D "Shoot your load on me baby!"

        D "Give it to me [player_name]."

        scene scene_12-9
        with vpunch

        A "Aaareghhhh huuuughhhh..."
        scene white with dissolve
        $ renpy.pause(0.5, hard = True)

        scene scene_12-10 with Dissolve (1.0)

        D "So muchh...mmmmm.."

        A "There's more..."

        scene scene_12-11
        scene white with dissolve
        $ renpy.pause(0.5, hard = True)


        A "aaaaaahhhhhhh"

        D "mmmmmmmmhmmmm....."

        scene scene_12-12 with Dissolve (1.0)

        D "I'm covered with your sticky cum."

        "You start breathing heavily."

        A "hhhhuuuuuhhh huuuuhhhhhh...."

        A "I need you again.... again!"

        D ".............!!"

        scene scene_12-13 with Dissolve (1.0)

        A "Take this argh argh..."

        D "............"

        scene scene_12-14 with Dissolve (1.0)

        A "You are still so warm mmmmmhmmm..."

        scene scene_12-15 with Dissolve (1.0)

        D "................."

        "You keep thrusting her but she makes no sound."

        window hide

        scene scene_12-15 with Dissolve (1.0)
        scene scene_12-14 with Dissolve (0.5)
        scene scene_12-15 with Dissolve (0.5)
        scene scene_12-14 with Dissolve (0.5)
        scene scene_12-15 with Dissolve (0.5)
        scene scene_12-14 with Dissolve (0.5)
        scene scene_12-15 with Dissolve (0.5)
        scene scene_12-14 with Dissolve (0.5)
        scene scene_12-15 with Dissolve (0.5)
        scene scene_12-14 with Dissolve (0.5)
        scene scene_12-15 with Dissolve (0.5)

        A "Are you feeling it?"

        D ".........."

        A "I know what's going to happen next..."

        A "It's inevitable..."

        scene scene_12-16 with Dissolve (1.0)

        A "It's like fire down there aaarrgghhh...."

        D "..........."

        A "Almost there....."

        scene scene_12-17 with Dissolve (1.0)

        "Thrust after thrust... You can feel her breaking apart..."

        scene scene_12-18 with Dissolve (1.0)

        A "Come to me!! Come to me!!"

        window hide

        scene scene_12-18 with Dissolve (1.0)
        scene scene_12-17 with Dissolve (0.5)
        scene scene_12-18 with Dissolve (0.5)
        scene scene_12-17 with Dissolve (0.5)
        scene scene_12-18 with Dissolve (0.5)
        scene scene_12-17 with Dissolve (0.5)
        scene scene_12-18 with Dissolve (0.5)
        scene scene_12-17 with Dissolve (0.5)
        scene scene_12-18 with Dissolve (0.5)
        scene scene_12-17 with Dissolve (0.5)
        scene scene_12-18 with Dissolve (0.5)

        A "YES YES YES!! I CAN FEEL IT!"

        A "I'm cumming!! AAARRRGHHHHHHHHH!!"
        with hpunch
        scene white with dissolve
        $ renpy.pause(0.7, hard = True)

        scene scene_12-19

        A "huuuuhhh huuuuhh uhhhuuuhhh...it's done!"

        scene scene_12-20 with Dissolve (1.0)

        A "You are mine again..."

        A "I missed you"

        scene scene_12-21 with Dissolve (1.0)

        A "You'll be mine forever"

        $ verselelchoice = True
        $ renpy.end_replay()
        jump backstory

    # Scene 13

    if chest == "none":

        scene scene_13-1

        D "Hey hey baby!"

        D "Not so fast!"

        D "Did you think everything would be that easy? heh!"

        A "Your were again messing with my mind, weren't you?"

        A "And what is this? I don't even get a warning before you start doing your things!"

        scene scene_13-2 with Dissolve (1.0)

        D2 "Shut up!!"

        D2 "It's my turn now!"

        D2 "Please me if you don't want your head chopped off!"

        A "Well I don't really mind having two of you at the same time but..."

        D "No ifs and buts!"

        scene scene_13-3 with Dissolve (1.0)

        D "I love the smell of your breath mmmmmmm...."

        A "mmmmhmmm mmmmm..."

        D2 "Is it just me or are your dick getting bigger every day?"

        D "Get on your knees and please him."

        D "Meanwhile I'll ride his face."

        D "My pussy is so hungry.. She needs [player_name]'s touch."

        scene scene_13-4 with Dissolve (1.0)

        A "mmhmmm **sllluuurrppp**.... I love the smell of your pussy.. It's so wet."

        D "Oh yes yes!! ahhh..! ahhh.."

        scene scene_13-5 with Dissolve (1.0)

        D2 "**gulp** **gulp** **slurp** **slurp**"

        A "Oh my god!! Ahhhh fuck yes!! Like that!!"

        D "Work on that clit! Make me cum! mmmmm...."

        scene scene_13-6 with Dissolve (1.0)

        A "Do you like it? Do you like it when I lick your cute little pussy? huh?"

        D "YES!! YES!! DON'T STOP!!"

        window hide

        scene scene_13-6 with Dissolve (1.0)
        scene scene_13-5 with Dissolve (0.5)
        scene scene_13-6 with Dissolve (0.5)
        scene scene_13-5 with Dissolve (0.5)
        scene scene_13-6 with Dissolve (0.5)
        scene scene_13-5 with Dissolve (0.5)
        scene scene_13-6 with Dissolve (0.5)
        scene scene_13-5 with Dissolve (0.5)
        scene scene_13-6 with Dissolve (0.5)
        scene scene_13-5 with Dissolve (0.5)
        scene scene_13-6 with Dissolve (0.5)

        A "Uuhhhh you are taking me to the edge...mmmmmhhhhpphh.."

        scene scene_13-7 with Dissolve (1.0)

        D2 "I want to taste your cum.. give it to me..."

        window hide

        scene scene_13-8 with Dissolve (1.0)
        scene scene_13-7 with Dissolve (0.5)
        scene scene_13-8 with Dissolve (0.5)
        scene scene_13-7 with Dissolve (0.5)
        scene scene_13-8 with Dissolve (0.5)
        scene scene_13-7 with Dissolve (0.5)
        scene scene_13-8 with Dissolve (0.5)
        scene scene_13-7 with Dissolve (0.5)
        scene scene_13-8 with Dissolve (0.5)
        scene scene_13-7 with Dissolve (0.5)
        scene scene_13-8 with Dissolve (0.5)
        scene scene_13-7 with Dissolve (0.5)
        scene scene_13-8 with Dissolve (0.5)

        A "I'm cumming!! aaahhhh...!!!"

        scene scene_13-9
        with vpunch

        A "aaarggghhhh....hhhhuuugghhh.."
        scene white with dissolve
        $ renpy.pause(0.7, hard = True)

        scene scene_13-10

        D2 "Wow!! mmmmmhmmm... so much cum on my face..."

        D "Here comes mine!! ahhhhahhhhh.."

        scene scene_13-11 with Dissolve (1.0)

        "The devil gives out a huge scream."

        scene scene_13-12
        with hpunch

        "And squirts all over you."

        D "aaaaaahhhhhhh hhmmmmmpphh...."

        scene scene_13-13 with Dissolve (1.0)

        A "mmmm the smell is so exotic and fiery."

        "The devil licks off the last bit of semen from your dick."

        scene scene_13-14 with Dissolve (1.0)

        D "You gave me the best orgasm ever [player_name].. Now your dick deserves something even better."

        D2 "I'm here ready for you."

        D2 "Take me now!"

        scene scene_13-15 with Dissolve (1.0)

        D "Yes yes fuck that pussy hard!! And you! Work on mine!"

        D2 "mmppphh emmhhh.."

        A "aahh ahhh ahhh it's so warm inside.. mmmhhhmmm feels so good hhheekkk.."

        window hide

        scene scene_13-16 with Dissolve (1.0)
        scene scene_13-15 with Dissolve (0.5)
        scene scene_13-16 with Dissolve (0.5)
        scene scene_13-15 with Dissolve (0.5)
        scene scene_13-16 with Dissolve (0.5)
        scene scene_13-15 with Dissolve (0.5)
        scene scene_13-16 with Dissolve (0.5)
        scene scene_13-15 with Dissolve (0.5)
        scene scene_13-16 with Dissolve (0.5)
        scene scene_13-15 with Dissolve (0.5)
        scene scene_13-16 with Dissolve (0.5)
        scene scene_13-15 with Dissolve (0.5)
        scene scene_13-16 with Dissolve (0.5)

        D2 "Don't stop! Fuck me harder and deeper mmmhhh.."

        A "Take this arggh argghh.."

        scene scene_13-17 with Dissolve (1.0)

        D "uhhmmh yes yes lick my cunt aahhh ahhh.."

        D2 "**slurp** **slurp** **lick** **lick**"

        A "It's getting tighter uuhhhh.."

        window hide

        scene scene_13-18 with Dissolve (1.0)
        scene scene_13-17 with Dissolve (0.5)
        scene scene_13-18 with Dissolve (0.5)
        scene scene_13-17 with Dissolve (0.5)
        scene scene_13-18 with Dissolve (0.5)
        scene scene_13-17 with Dissolve (0.5)
        scene scene_13-18 with Dissolve (0.5)
        scene scene_13-17 with Dissolve (0.5)
        scene scene_13-18 with Dissolve (0.5)
        scene scene_13-17 with Dissolve (0.5)
        scene scene_13-18 with Dissolve (0.5)
        scene scene_13-17 with Dissolve (0.5)
        scene scene_13-18 with Dissolve (0.5)

        A "I'm cumming again!! I'm gonna fill up your pussy with my cum."

        scene scene_13-19

        "Both you and the devil reach climax and cum at the same time."
        with flash2


        A "aaarrrgghhh.."

        D2 "aahhhmm I can feel my pussy dripping with your cum."
        scene white with dissolve
        $ renpy.pause(0.7, hard = True)

        scene scene_13-20

        "You shoot another load on the devil's buttcheeks."

        D "You had so much inside you huh.. Wow!"

        A "I can't believe myself either."

        D2 "But why did you piss on me?"

        A "Wait what?!"

        D "Drink it all!"

        A "Yuck!! I can't believe you just did that."

        D2 "As your wish my lady."

        D2 "**gulp** **gulp**"

        A "UGHH! Gross!"

        D "You know why I did this [player_name]."

        "Suddenly she changes her tone."

        scene scene_13-21 with Dissolve (1.0)

        A "I....."

        D "You know the deal.."

        A "I... Things went out of hands.."

        D "You are responsible for your actions and you know the outcome."

        A "Please don't do this."

        D "Stand up now girl!"

        D2 "Yes my lady."

        scene scene_13-22 with Dissolve (1.0)

        A "I won't do such thing again.. I promise."

        D "Your promises mean nothing to me.. \"Make a wrong move and she becomes mine\" that was the deal."

        A "I'm the one at fault. Punish me, not her!"

        D "You don't make the rules."

        A "Plea...."

        scene scene_13-23
        with vpunch

        D2 "ugghhh......"

        A "No please no!"

        scene scene_13-24 with Dissolve (1.0)

        D2 "Aaaaaaaaaaaaahhhhhhhh....."

        D "HAHAHAHHAHA....!!!!"

        "She cries out in pain and her body starts getting numb."

        "The devil keep strangling her harder and harder."

        D "Look away [player_name]... You don't want to see this..."

        A ".........."

        scene scene_13-25 with Dissolve (1.0)

        "Total silence."

        "You watch her transform right before looking away."

        A "I'm sorry....**sniff** **sniff**.. I'm sorry."

        D "It's done!"

        scene scene_13-26 with Dissolve (1.0)

        "The lifeless body lies right in front of you."

        A ".........."

        D "Now where were we?"

        D "Reverseus"
        $ renpy.end_replay()
        $ verselonlychoice = True

        jump backstory


    # scene 14

label calm:

    # Ella Path

    scene 14-1 with Dissolve (1.0)

    A "There's more to it in a relationship than just sex Selina."

    A "I've never got to kiss my girl, not even a hug."

    A "I want to feel her in my arms and let her know of my true feelings."

    A "And being able to embrace the person you love is a beautiful feeling as well."

    scene 14-2 with Dissolve (1.0)

    S "Oh my! I didn't know that you can be this cute."

    scene 14-3 with Dissolve (1.0)

    V "Honey you are too sweet. I totally get what you are trying to say."

    V "I won't push you. Just letting you know that we love you more than anything
       and being apart from you even for a moment is painful for us."

    scene 14-4 with Dissolve (1.0)

    S "Yes, [player_name]. I guess we both over-reacted. You have the right to be with her and decide what kind of life you want.
       Just know that we are always with you."

    A "Thank you both. I love you as well. Trust me. No one will ever take your places."

    A "It's just a matter of a month. It will have passed before you know it."

    scene 14-5 with Dissolve (1.0)

    V "So tomorrow is the day huh."

    S "Sure seems so."

    V "Can't believe you've arranged everything and gave us only a day's heads up."

    V "Honey, are you sure you will be alright in that place all by yourself?"

    scene 14-6 with Dissolve (1.0)

    A "Of course I am. I have already rented a house there. It's only 10 minutes from her place."

    A "If I need anything Ella can help me out."

    S "Good to know. Just don't forget to call us every now and then."

    V "Yes, [player_name]. Make sure you call us right after your land."

    A "Sure thing."

    scene 14-7 with Dissolve (1.0)

    V "But are you sure about not letting her know beforehand?"

    A "Yes I am. I want to surprise her. I'm sure she will love it."

    A "Oh I almost forgot! Jason doesn't know yet."

    scene 14-8 with Dissolve (1.0)

    S "Really [player_name]? You are going away for a month and didn't even tell your best buddy yet?"

    A "Do you guys have any plans for today?"

    scene 14-9 with Dissolve (1.0)

    S "I don't know. Maybe I'll go and do a little shopping. Cathy is throwing a bachelorette party"

    A "That college friend of yours?"

    S "Yes. Her wedding is right around the corner. But guess what? You're gonna miss it. I wanted to take you with me."

    A "Well shoot!"

    scene 14-10 with Dissolve (1.0)

    A "What about you Veronica?"

    scene 14-11 with Dissolve (1.0)

    V "Well since you are leaving tomorrow, I think I'll make you the nicest dinner of your life."

    A "Oh that's sweet honey."

    if renpy.loadable("patch.rpy") or patch:
        A "Okay then. I think I'll go and meet Jason. His mom has been asking me to visit her for quite some time now."

    if not renpy.loadable("patch.rpy"):
        A "Okay then. I think I'll go and meet Jason. Kylie has been asking me to visit her for quite some time now."

    scene 14-12 with Dissolve (1.0)

    V "Honey can you drop me off to the mall? I need to buy few things for the dinner tonight."

    A "Sure Veronica. Meet me outside once you are ready to go.
       I'll get changed right away."


    scene 14-13 with Dissolve (1.0)

    A "See you later Selina."

    scene 14-14 with Dissolve (1.0)

    S "Later babe"

    "Veronica doesn't respond this time."

    jump outsidecar


    # Scene 15


label outsidecar:

    scene 15-1 with Dissolve (1.0)

    A "(Well everything went smoothly. Veronica seemed really calm and Selina didn't mind.
       I need to make it up to her tonight)."

    scene 15-2 with Dissolve (1.0)

    A "Ready to go?"

    V "Let's go honey."

    scene 15-3 with Dissolve (1.0)

    A "Here we are."

    V "Thanks for dropping me off, sweety."

    A "You are welcome, Veronica."

    scene 15-4 with Dissolve (1.0)

    "Veronica opens the door to get out."

    "To make it up to her you decide to kiss her cheek but suddenly.."

    scene 15-5
    with hpunch

    A "(Holy shit!)"

    scene 15-6 with Dissolve (1.0)

    V "[player_name] I..."

    A "Oh my god! I'm so sorry Veronica. I didn't mean to kiss you on there.. I ju.."

    scene 15-7
    with hpunch

    A "(Holy cow!!!)"

    scene 15-8 with Dissolve (1.0)

    V "mmmmhm.."

    A "mmhm.."

    scene 15-9 with Dissolve (1.0)

    V "It's okay [player_name]. You don't have to feel sorry."

    A "(God why is she so beautiful?)"

    A "You are so pretty, Veronica."

    scene 15-10 with Dissolve (1.0)

    V "*giggle* don't you always say that [player_name]?"

    V "See you at night, honey."

    scene 15-11 with Dissolve (1.0)

    A "(What the fuck just happened?!)"

    A "(It was so passionate)"

    "You are left awestruck for a few minutes."

    "You finally get a grip on yourself and head to Jason's home."

    scene 15-12 with Dissolve (1.0)

    A "I'll deal with this later. But WOW! Damn!"

    A "It felt so good and she did it herself the second time!"

    A "Hushh. I need to focus on the road now. Here I go."


    # Scene 16


    scene 16-1 with Dissolve (1.0)

    "You reach Jason's house."

    scene 16-2 with Dissolve (1.0)

    A "I hope he is here. I should probably have called ahead and checked."

    scene 16-3 with Dissolve (1.0)

    "Riley opens the door."

    R "Hey [player_name]!"

    "Riley smiles."

    A "Hey Riley. How are you?"

    scene 16-4 with Dissolve (1.0)

    R "I'm great. Come in."

    scene 16-5 with Dissolve (1.0)

    A "You look beautiful today."

    R "Oh aren't you such a charmer?"

    scene 16-6 with Dissolve (1.0)

    A "Where is Jason?"

    scene 16-7 with Dissolve (1.0)

    if renpy.loadable("patch.rpy") or patch:
        R "With mom.."

    if not renpy.loadable("patch.rpy"):
        R "With Kylie.."

    A "They don't ever stop, do they?"

    scene 16-8 with Dissolve (1.0)

    R "Nope! Thanks to you."

    A "Hey! I wasn't the only one there that day."

    scene 16-9 with Dissolve (1.0)

    A "You almost killed me with that ass of yours."

    scene 16-10 with Dissolve (1.0)

    R "Oh I'm so sorry, honey. But it felt so good sitting on your face hihihi."

    A "Bet it did. You totally forgot that I needed to breathe *laughter*."

    scene 16-11 with Dissolve (1.0)

    A "Anyways, let's go to them. I have something to tell you three."

    R "Don't think they are in any position to listen to you."

    A "Let's find out."


    # Scene 17

    scene 17-1 with Dissolve(1.0)

    A "Are you taking good care of my asset?"

    R "See for yourself *giggle*"

    scene 17-2 with Dissolve(1.0)

    "You reach the second floor."

    "Loud moaning sounds coming out from Kylie's room."

    "**Knock** **Knock**"

    J "Riley! Thought you didn't want to join."

    K "Oh god! yeahh yeah!"

    A "Open up asshole! It's me."

    K "Hey, the door's open. Come on in!"

    K "Fuck fuck!!"
    label galleryScene2:
    scene 17-3 with Dissolve(1.0)

    J "Yeah just like that!"

    scene 17-4 with Dissolve(1.0)

    J "Hey bro! Up for a round?"

    K "Hey [player_name]! You finally came."
    K "Come here honey. Give me a kiss. I missed you a lot."

    scene 17-5 with Dissolve(1.0)

    K "mmmmhhhmmm mmmhmmm.."

    scene 17-4 with Dissolve(1.0)

    K "I wonder if that dick of yours still tastes as good as your lips."

    scene 17-6 with Dissolve(1.0)

    A "Look at you horny bastards!"

    if renpy.loadable("patch.rpy") or patch:
        J "She's been going for hours. Mom can't stop riding me."

    if not renpy.loadable("patch.rpy"):
        J "She's been going for hours. This bitch can't stop riding me."

    J "I need to piss and she isn't even letting me go for a minute."

    if renpy.loadable("patch.rpy") or patch:
        J "How about I release in your pussy mom?"

    if not renpy.loadable("patch.rpy"):
        J "How about I release in your pussy babe?"

    scene 17-7 with Dissolve(1.0)

    K "Don't even fucking dare!"

    J "Just kidding, babe."

    K "Fuck me, you motherfucking asshole!"

    if renpy.loadable("patch.rpy") or patch:
        J "Aww come here mom."

    if not renpy.loadable("patch.rpy"):
        J "Aww come here babe."

    scene 17-8 with Dissolve(1.0)

    J "Damn babe! Ahhh yeah..."

    if renpy.loadable("patch.rpy") or patch:
        K "Son I love your dick so much!!. mmmhh.. yes yes.."

        J "We've got the whole day set aside for you, mom. And look! There's another dick in the house now."

    if not renpy.loadable("patch.rpy"):
        K "I love your dick so much!!. mmmhh.. yes yes.."

        J "We've got the whole day set aside for you, my slut. And look! There's another dick in the house now."

    K "aaahh...ahhh..ummm...harder...."

    window hide

    image animation1-4 = Movie(channel="animation1-4", play="video/animation1-4.webm", start_image="animation1-4", image="animation1-4")
    scene animation1-4 with dissolve:
        size (config.screen_width, config.screen_height)

    K "OH MY GOD!!! MMMHHMMpphh Aaahhhh it feels so good!!"

    if renpy.loadable("patch.rpy") or patch:
        J "Aarrghh...mmmhhmmm.. how can you still be so tight mom?! aarrghhh!! Take this bitch!"

    if not renpy.loadable("patch.rpy"):
        J "Aarrghh...mmmhhmmm.. how can you still be so tight babe?! aarrghhh!! Take this bitch!"

    scene 17-9 with Dissolve(1.0)

    A "Aww look at you two lovebirds."

    R "Maybe we should join as well. I haven't felt your touch for so many days."

    A "Guys!"

    A "I have something important to talk to you about. This can wait."

    scene 17-10 with Dissolve(1.0)

    J "What's more important than pussies?"

    scene 17-11 with Dissolve(1.0)

    K "Come join us honey! It's been long since I tasted your dick."

    A "I was here just a bit more than a week ago."

    K "That's 10 inch dick long fucking days."

    scene 17-12
    with vpunch

    K "Faster you bastard.. harder harder... mmmm..... oh fuckk.."

    scene 17-13 with Dissolve(1.0)

    R "Well I wanted to rest today but I can't miss the chance of being with you.
    Are you up for it [player_name]?"

    A "(I feel so tired but this.. how can I walk away from this?
       It's been days I had these two)"

    A "(Oh well. I have the whole day to talk. I don't mind doing once more before leaving)"

    A "(A month without them will be difficult to endure)"

    scene 17-14 with Dissolve(1.0)

    K "That's my girl. Always up for it."

    R "**gulp** **gulp** **slurp** **slurp** mmmhhmmm ffffpph.."

    A "Suck me dry babe.. come on mmmhmmm.."

    K "You never disappoint [player_name]"

    K "I want you both to fuck our brains out."

    if renpy.loadable("patch.rpy") or patch:
        J "You bet we will mom."

    if not renpy.loadable("patch.rpy"):
        J "You bet we will babe."

    A "Aaahh this feels so good."
    with flash2
    A "The fuck!"
    with flash2
    A "What's going on?"
    $ renpy.end_replay()
    with flash
    with flash2
    hide scene_17-14

    jump devilappear3


    # Scene 18

label devilappear3:

    scene scene_18-1

    D "Hey hey baby!"

    D "Not so fast!"

    D "Did you think everything would be that easy? heh!"

    scene scene_18-2 with Dissolve (1.0)

    A "Your were again messing with my mind, weren't you?"

    A "And what is this? I don't even get a warning before you start doing your things!"

    scene scene_18-3 with Dissolve (1.0)

    D "Shut up!!"

    D "It's my turn now."

    D "Please me if you don't want your head chopped off!"

    if renpy.loadable("patch.rpy") or patch:
        D "And learn to appreciate the efforts of my babies."

    if not renpy.loadable("patch.rpy"):
        D "And learn to appreciate the efforts of these girls."

    A "I neve...."

    D "Look how she is taking the whole thing..."

    scene scene_18-4 with Dissolve (1.0)

    D2 "uuukkkhh mmhmmmm.."

    A "Why is your mouth so hot? It's burning my dick."

    D "She is still a devil, you idiot!"

    D2 "**slurp** **slurp** **uucckk** **slurp**"

    scene scene_18-5 with Dissolve (1.0)

    D "YES YES YES!!! LICK MY PUSSY JUST LIKE THAT!! mmhhhmm ahhhhh..!!"

    D3 "**mmmmhhmmmm** **lick** **lick**"

    D3 "*giggle* it's so delicious"

    window hide

    scene scene_18-6 with Dissolve (1.0)
    scene scene_18-7 with Dissolve (0.5)
    scene scene_18-6 with Dissolve (0.5)
    scene scene_18-7 with Dissolve (0.5)
    scene scene_18-6 with Dissolve (0.5)
    scene scene_18-7 with Dissolve (0.5)
    scene scene_18-6 with Dissolve (0.5)

    D "OWH FUCKKK!!! mhhmmmmmmm keep doing it.."

    window hide

    scene scene_18-7 with Dissolve (0.5)
    scene scene_18-6 with Dissolve (0.5)
    scene scene_18-7 with Dissolve (0.5)
    scene scene_18-6 with Dissolve (0.5)
    scene scene_18-7 with Dissolve (0.5)
    scene scene_18-6 with Dissolve (0.5)
    scene scene_18-7 with Dissolve (0.5)
    scene scene_18-6 with Dissolve (0.5)

    D3 "I will eat this pussy like it's my last ever."

    D "You bet mmhhmmmm.."

    scene scene_18-8 with Dissolve (1.0)

    D "How are you hanging in there [player_name]?"

    A "Ahhhh I can't last that longer"

    A "She is just too good with that tongue."

    scene scene_18-9 with Dissolve (1.0)


    if renpy.loadable("patch.rpy") or patch:
        D "You have no idea what my babies can do."

    if not renpy.loadable("patch.rpy"):
        D "You have no idea what else they can do."

    D "Fuck that slutty face [player_name]!!"

    window hide

    scene scene_18-8 with Dissolve (0.5)
    scene scene_18-9 with Dissolve (0.5)
    scene scene_18-8 with Dissolve (0.5)
    scene scene_18-9 with Dissolve (0.5)
    scene scene_18-8 with Dissolve (0.5)
    scene scene_18-9 with Dissolve (0.5)
    scene scene_18-8 with Dissolve (0.5)
    scene scene_18-9 with Dissolve (0.5)
    scene scene_18-8 with Dissolve (0.5)

    D "aaaahhhhhhh I'm cumming!!!"

    D3 "Yes yes mmmhmmm squirt all over my face mhmmmm.."

    window hide

    scene scene_18-9 with Dissolve (0.5)
    scene scene_18-8 with Dissolve (0.5)
    scene scene_18-9 with Dissolve (0.5)
    scene scene_18-8 with Dissolve (0.5)
    scene scene_18-9 with Dissolve (0.5)
    scene scene_18-8 with Dissolve (0.5)
    scene scene_18-9 with Dissolve (0.5)
    scene scene_18-8 with Dissolve (0.5)
    with hpunch
    with flash2

    A "Arrrrghhhh ahhhhhhhhh haaaahhh...."

    "You shoot your load inside her mouth."

    D2 "ukkhhhh mhmmmm mmmhmmm.."

    "And she swallows it all with great pleasure."

    A "You are so amazing... I never had such a great blowjob before."

    scene scene_18-10 with Dissolve (1.0)

    D "Are you saying mine isn't that good?! Don't test your luck.. You never know what's ahead of you."

    D3 "Come on! Cut him some slack.. He's been through a lot."

    D "......."

    scene scene_18-11 with Dissolve (1.0)

    D3 "Do you like what you see [player_name]?"

    A "Of course I do.. They are so big!! The most amazing tits I have ever seen!!"

    D "You should be thanking me for these!"

    A "I always do."

    scene scene_18-12 with Dissolve (1.0)

    D2 "What about mine? Do you like my tits around your hard cock?"

    A "Oh yes!! mmhhhmmmm!!"

    scene scene_18-13 with Dissolve (1.0)

    D "Na ah! Get up honey! You had enough of him. She can take charge now.
       Why don't you try me instead?"

    D2 "Uh! Yee..Yes my lady"

    scene scene_18-14 with Dissolve (1.0)

    D3 "mmmmhmmm yes baby.. suck on my nipple.."

    D3 "aahh it feels so good...mmmm"

    A "mmm mmm **suck** **suck**"

    D3 "I love the way you run your tongue all over it mmmmmm.."

    "You keep sucking her nipple while pressing the other boob gently."

    scene scene_18-15 with Dissolve (1.0)

    "You pick her up and insert your cock in her vagina."

    D3 "aaahhh so big mmmhmmmmm.."

    D "What were you doing?"

    D2 "I'm so sorry my lady.. I should have known my place."

    D "Good that you realise your mistake.. Why don't you let me take a look at your pretty face, honey?"

    D "Turn around."

    scene scene_18-16 with Dissolve (1.0)

    D2 "Please my lady! Forgive me....**sniff** **sniff**"

    D "Now now.. Don't cry. You don't want to ruin your pretty face.. You made a mistake.
       That's it. Everyone does. Don't worry about it."

    D2 "**sniff** **sniff**"

    D "Stop crying now.. ssshhhh.."

    scene scene_18-17 with Dissolve (1.0)

    D3 "Fuck me harder [player_name]!!! Fuck me fuck me mmmhhh..!!!"

    A "AArrrgghhh ahhhhh mmmmm I love your pussy.. It's so wet."

    D "Look at them go... You could have been there with him as welll..."

    D2 "**sniff** [player_name].... **sniff**"

    window hide

    scene scene_18-18 with Dissolve (0.5)
    scene scene_18-17 with Dissolve (0.5)
    scene scene_18-18 with Dissolve (0.5)
    scene scene_18-17 with Dissolve (0.5)
    scene scene_18-18 with Dissolve (0.5)
    scene scene_18-17 with Dissolve (0.5)
    scene scene_18-18 with Dissolve (0.5)
    scene scene_18-17 with Dissolve (0.5)
    scene scene_18-18 with Dissolve (0.5)
    scene scene_18-17 with Dissolve (0.5)
    scene scene_18-18 with Dissolve (0.5)
    scene scene_18-17 with Dissolve (0.5)
    scene scene_18-18 with Dissolve (0.5)
    with vpunch
    with flash2


    A "aaaaaaahhhhh mmmmmmmmmm!!"

    D3 "Yes yes yes!!! Give me your seeds mmmmhmmmmm!!"

    D2 "**sniff** **sniff**"

    D "Stop crying now.. PLEEEEAAAASE!"

    scene scene_18-19 with Dissolve (1.0)

    A "aahh mmmmhhmmmm I want to go again!"

    D3 "Don't stop then mmmmm!! The way you.. ahh.. use your dick.. ah ahh.. ihhs soo amazing ummmm ahhh.."

    D2 "**sniff** I'm sorry."

    D "STOP...."

    scene scene_18-20
    with hpunch

    D "CRYING!!!"

    D3 "(shocked) aaaahhhhhhhh..!!"

    scene scene_18-21 with Dissolve (1.0)

    D "FUCKING BITCH!! SO ANNOYING!!"

    "You have no idea what's going on behind you."

    "You are completely consumed by lust."

    A "mmhhhmm ah ah ahh can't get enough of your pussy mmmm.."

    A "We are going to make babies soon *giggle*"

    D "THAT FUCKING BITCH IS GOING TOO FAR AGAIN!!!"

    scene scene_18-22 with Dissolve (1.0)

    D3 "NO! NO! NO! STOP!!"

    A "Huh what?! WHY?!"

    D3 "JUST PULL YOUR DICK OUT!! NOW!!"

    D "YOU...FUCKING...."

    scene scene_18-23
    with vpunch

    D "BITCH!!!"

    D3 "Nooooooo!!! Please STOP!!"

    A "WHAT ARE YOU DOING?!! LEAVE HER ALONE!!"

    D "You don't order me, motherfucker!!"

    D3 "[player_name]!! HELP ME!!"

    D "I'M GONNA FUCKING BREAK YOU INTO PIECES!!"

    A "NOOOO!!!"

    scene scene_18-24
    with vpunch

    "You hear the sound of bones cracking."

    A "OH GOODDD!!! NO! NO! NO!!"

    scene scene_18-25 with Dissolve (1.0)

    D "Corruptetus Forgetus"
    with flash2

    A ".............."

    scene scene_18-26 with Dissolve (1.0)

    D "AHAHAHAH poor kid.. You crossed the line way earlier."

    D "I was just letting you have some fun with her."

    A "..............."

    D "You are responsible for everything that has happened."

    D "Now now... We need to fix everything, don't we?"

    scene scene_18-27 with Dissolve (1.0)

    D "Reverseus"

    A "HUH!!"

    D "Hey hey baby!"

    A "What's this? How did I end up here this time?"

    D "I just wanted to have some fun."

    A "You know that rejection has never been a part of me when it comes to you.. So why not just ask me first?"

    D "Where's the fun in it?"

    D "By the way.. Do you like when I press my tits against your dick?"

    scene scene_18-28 with Dissolve (1.0)

    A "Do I even need to answer?"

    D "*giggle* now fuck them like you always do."

    A "Sure thing."

    window hide

    scene scene_18-27 with Dissolve (0.5)
    scene scene_18-28 with Dissolve (0.5)
    scene scene_18-27 with Dissolve (0.5)
    scene scene_18-28 with Dissolve (0.5)
    scene scene_18-27 with Dissolve (0.5)
    scene scene_18-28 with Dissolve (0.5)
    scene scene_18-27 with Dissolve (0.5)
    scene scene_18-28 with Dissolve (0.5)
    scene scene_18-27 with Dissolve (0.5)
    scene scene_18-28 with Dissolve (0.5)
    scene scene_18-27 with Dissolve (0.5)
    scene scene_18-28 with Dissolve (0.5)
    scene scene_18-27 with Dissolve (0.5)
    scene scene_18-28 with Dissolve (0.5)

    A "mmmmhmmmmmm yes yes yes so good.."

    D "mmmmhmmmm don't stop.."

    window hide

    scene scene_18-27 with Dissolve (0.5)
    scene scene_18-28 with Dissolve (0.5)
    scene scene_18-27 with Dissolve (0.5)
    scene scene_18-28 with Dissolve (0.5)
    scene scene_18-27 with Dissolve (0.5)
    scene scene_18-28 with Dissolve (0.5)
    scene scene_18-27 with Dissolve (0.5)
    scene scene_18-28 with Dissolve (0.5)
    scene scene_18-27 with Dissolve (0.5)
    scene scene_18-28 with Dissolve (0.5)

    A "I'm gonna cum anytime now!!"

    D "Spray them all over my tits mmmmmmhmmm!!"

    scene scene_18-29 with Dissolve (1.0)

    A "Look straight into my eyes baby... I want to see your pretty face."

    scene scene_18-30 with Dissolve (1.0)

    D "Come on!! Shoot your load on this slut's tits."

    D "Give your semen to your slutty little bitch."

    A "Aaaahhhhhhhh.."

    scene scene_18-31
    with vpunch
    scene white with dissolve
    $ renpy.pause(0.7, hard = True)

    scene scene_18-32

    A "aahhh ahhh mmmmmmm.."

    D "mmmmm so much cum.. Your bitch is happy."

    A "huh huh huh... Why do I feel so tired?"

    scene scene_18-33 with Dissolve (1.0)

    D "Duh! You came a lot.. that's why."

    A "Yeah... I guess..."

    A "Damn!! This felt so good."

    A "We should be doing this more often."

    D "*laughter* don't we always do that [player_name]?.."

    A "*laughter* true.. You are the best thing ever to happen in my life..."

    D "Aww how adorable!"

    A "Up for another round babe?"

    D "Are you sure?"

    A "I mean we still have your lower body to explore."

    D "Well then... Take me daddy!"

    A "*giggle* come to daddy!"
    $ renpy.end_replay()
    $ ellaonlychoice = True


    jump backstory
