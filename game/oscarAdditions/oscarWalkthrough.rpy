init python:
    gr = "{color=#0f0}"
    red = "{color=#f00}"
    blue = "{color=#00f}"

    HaremPath = "{color=#0f0}[Harem Path]"
    EllaPath = "{color=#0f0}[Ella Path]"
    AmySubPath = "{color=#0f0}[Amy Sub Path]"
    CarolPath = "{color=#0f0}[Carol Path]"
    CarolLovePath = "{color=#0f0}[Carol Love Path]"
    CarolVoyeurPath = "{color=#0f0}[Carol Voyeur Path]"
    CarolTagTeamPath = "{color=#0f0}[Carol Tag Team Path]"
    CaitlynLovePath = "{color=#0f0}[Caitlyn Love Path]"
    MiraLovePath = "{color=#0f0}[Mira Love Path]"
    SaraLovePath = "{color=#0f0}[Sara Love Path]"
    BeckyLovePath = "{color=#0f0}[Becky Love Path]"
    BeckySubPath = "{color=#0f0}[Becky Sub Path]"
    LillyLovePath = "{color=#0f0}[Lilly Love Path]"
    LillyTagTeam = "{color=#0f0}[Lilly Tag Team Path]"
    DalesPath = "{color=#0f0}[The Dales Path]"
    SistersPath = "{color=#0f0}[The Sisters Path]"
    RileyPath = "{color=#0f0}[Riley Path]"

screen modWalkthroughOptions():
    tag menu
    modal True

    add "#23272a"

    vbox:
        xcenter 0.5
        ypos 50
        spacing 100

        text "Walkthrough Options" style "modTextHeader"

        text "Turn on and off character paths" style "modTextBody" xcenter 0.5

    frame:
        xcenter 0.5
        ycenter 0.5
        padding (20, 20)
        grid 3 3:
            spacing 50
            style_prefix "check"

            textbutton "Amy's Paths":
                action [ToggleVariable("AmyPath", true_value="{color=#0f0}[Amy Path]", false_value=""), ToggleVariable("AmyLovePath", true_value="{color=#0f0}[Amy Love Path]", false_value=""), ToggleVariable("AmySubPath", true_value="{color=#0f0}[Amy Sub Path]", false_value="")]

            textbutton "Carol's Paths":
                action [ToggleVariable("CarolPath", true_value="{color=#0f0}[Carol Path]", false_value=""), ToggleVariable("CarolLovePath", true_value="{color=#0f0}[Carol Love Path]", false_value=""), ToggleVariable("CarolVoyeurPath", true_value="{color=#0f0}[Carol Voyeur Path]", false_value=""), ToggleVariable("CarolTagTeamPath", true_value="{color=#0f0}[Carol Tag Team Path]", false_value="")]

            textbutton "Caitlyn's Path":
                action [ToggleVariable("CaitlynLovePath", true_value="{color=#0f0}[Caitlyn Love Path]", false_value="")]

            textbutton "Mira's Path":
                action [ToggleVariable("MiraLovePath", true_value="{color=#0f0}[Mira Love Path]", false_value="")]

            textbutton "Sara's Path":
                action [ToggleVariable("SaraLovePath", true_value="{color=#0f0}[Sara Love Path]", false_value="")]

            textbutton "Becky's Paths":
                action [ToggleVariable("BeckyLovePath", true_value="{color=#0f0}[Becky Love Path]", false_value=""), ToggleVariable("BeckySubPath", true_value="{color=#0f0}[Becky Sub Path]", false_value="")]

            textbutton "Lilly's Paths":
                action [ToggleVariable("LillyLovePath", true_value="{color=#0f0}[Lilly Love Path]", false_value=""), ToggleVariable("LillyTagTeam", true_value="{color=#0f0}[Lilly Tag Team Path]", false_value="")]

            textbutton "The Dale's Path":
                action [ToggleVariable("DalesPath", true_value="{color=#0f0}[The Dales Path]", false_value="")]

            textbutton "The Sister's Path":
                action [ToggleVariable("SistersPath", true_value="{color=#0f0}[The Sisters Path]", false_value="")]

    textbutton _("Return") action Hide("modWalkthroughOptions"):
        text_font "gui/PoiretOne-Regular.ttf"
        text_color "#a11f1f"
        text_hover_color "#ffffff"
        text_size 50
        yanchor 1.0
        pos (100, 980)
