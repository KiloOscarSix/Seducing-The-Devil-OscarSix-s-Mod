init python:
    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1

define galleryPageNumber = 1

define sceneGalleryMenuDict = {
    "galleryMenu": [
    ["Selina", "/images/1-6.webp"],
    ["The Devil", "/images/1-6.webp"],
    ["Kylie", "/images/1-6.webp"],
    ["Riley", "/images/1-6.webp"],
    ["Ella", "/images/1-6.webp"],
    ["Veronica", "/images/1-6.webp"],
    ["Other", "/images/1-6.webp"],
    ],
    "Selina": {
    1: [
    ["galleryScene1", {}, "/images/1-6.webp"], # Selina
    ["galleryScene3", {}, "/images/88-25.webp"], # Selina
    ["galleryScene4", {}, "/images/92-21.webp"], # Selina
    ["galleryScene5", {}, "/images/99-9.webp"], # Selina
    ["galleryScene6", {}, "/images/102-12.webp"], # Selina
    ["selinaaccept119", {"selinabuttslap":"yes", "veronicakiss":"yes"}, "/images/119-20.webp"], # Selina
    ["galleryScene12", {"confession125":"yes", "selinabuttslap":"yes"}, "/images/126-11.webp"], # Selina + Riley
    ["galleryScene13", {"selinabuttslap":"yes"}, "/images/134-24.webp"], # Selina
    ],
    2: [
    ["galleryScene15", {"selinabuttslap":"yes"}, "/images/141-9.webp"], # Selina + Veronica
    ["alanpeekselina2", {}, "/images/scene_25-24.webp"], # Selina
    ["cherrypop", {"alanforceselina":"yes", "alankisshospital":"yes"}, "/images/scene_84-24.webp"], # Selina + Devil
    ]
    },
    "The Devil": {
    1: [
    ["devilappear1", {}, "/images/scene_11-2.webp"], # Devil
    ["before_devilappear2", {}, "/images/12-1.webp"], # Devil
    ["devilappear3", {}, "/images/18-10.webp"], # Devil
    ["galleryScene10", {}, "/images/110-3.webp"], # Devil
    ["galleryScene11", {}, "/images/124-4.webp"], # Devil
    ["ellacherrypopped", {}, "/images/scene_85-24.webp"], # Devil
    ["cherrypop", {"alanforceselina":"yes", "alankisshospital":"yes"}, "/images/scene_84-24.webp"], # Selina + Devil
    ]
    },
    "Kylie": {
    1: [
    ["galleryScene2", {}, "/images/17-11.webp"], # Kylie
    ["galleryScene7", {"stayriley":"yes"}, "/images/105-10.webp"], # Kylie
    ["galleryScene8", {}, "/images/105-34.webp"], # Kylie + Riley
    ["galleryScene9", {}, "/images/106-5.webp"], # Kylie
    ["kylierileyaccept", {}, "/images/116-26.webp"], # Kylie + Riley
    ["elselver", {}, "/images/121-7.webp"], # Kylie + Riley
    ],
    },
    "Riley": {
    1: [
    ["stayriley", {}, "/images/scene_31-31.webp"], # Riley
    ["galleryScene12", {"confession125":"yes", "selinabuttslap":"yes"}, "/images/126-11.webp"], # Selina + Riley
    ["galleryScene8", {}, "/images/105-34.webp"], # Kylie + Riley
    ["kylierileyaccept", {}, "/images/116-26.webp"], # Kylie + Riley
    ["elselver", {}, "/images/121-7.webp"], # Kylie + Riley
    ]
    },
    "Ella": {
    1: [
    ["jerktoella", {}, "/images/scene_22-5.webp"], # Ella
    ["alancallella", {}, "/images/scene_43-28.webp"], # Ella
    ["galleryScene17", {}, "/images/scene_73-11.webp"], # Ella
    ]
    },
    "Veronica": {
    1: [
    ["galleryScene15", {"selinabuttslap":"yes"}, "/images/141-9.webp"], # Selina + Veronica
    ["galleryScene16", {}, "/images/scene_27-35.webp"], # Veronica
    ["veronicafirstsex", {}, "/images/scene_64-23.webp"], # Veronica
    ]
    },
    "Other": {
    1: [
    ["cathygloryblow", {}, "/images/91-30.webp"], # Other
    ["ellaonly", {}, "/images/114-6.webp"], # Lilith + Madison
    ["tana131accept", {}, "/images/131-22.webp"], # Tana
    ["galleryScene14", {}, "/images/137-3.webp"], # Diana + Rachel
    ["helpKylie", {}, "/images/scene_32-35.webp"], # Kylie
    ["momslavedevil", {"stayriley":"yes", "selinapeek":"yes"}, "/images/scene_35-16.webp"], # Rachel
    ["door6", {}, "/images/scene_55-11.webp"], # Rachel
    ["ver07", {}, "/images/scene_79-13.webp"], # Madison
    ],
    2: [
    ["galleryScene18", {}, "/images/scene_82-29.webp"], # Tana
    ]
    },
    }

label galleryNameChange:
    default persistent.player_name = ""
    if persistent.player_name == "":
        $ persistent.player_name = renpy.input("Your name?", default="Alan")
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "#23272a"

    text "Oscar's Scene Gallery":
        style "galleryHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                action Hide("sceneGalleryMenu"), Show("main_menu")
                idle "/oscarAdditions/images/button.png"
                hover Transform(im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2)))
            text "Back":
                style "galleryBody"
                xcenter 0.5
                ycenter 0.5

        imagebutton:
            action OpenURL("https://www.patreon.com/oscarsix/overview")
            idle Transform("/oscarAdditions/images/become_a_patron_button.png", zoom=0.7465437788)
            hover Transform(im.MatrixColor("/oscarAdditions/images/become_a_patron_button.png", im.matrix.brightness(0.2)), zoom=0.7465437788)
            xanchor 1.0

    vpgrid:
        cols 4
        xspacing 50
        yspacing 37
        pos (117, 360)

        for i in sceneGalleryMenuDict["galleryMenu"]:
            vbox:
                imagebutton:
                    action Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")
                    idle Transform(i[1], zoom=0.2)
                    hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                text i[0]:
                    style "galleryBody"
                    xcenter 0.5

screen sceneCharacterMenu(galleryCharacter="All"):
    tag menu
    modal True
    add "#23272a"

    text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
        style "galleryHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                if galleryPageNumber == 1:
                    action Show("sceneGalleryMenu"), Hide("sceneCharacterMenu")
                else:
                    action Function(galleryDecreasePageNumber)
                idle "/oscarAdditions/images/button.png"
                hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "galleryBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            if galleryPageNumber != len(sceneGalleryMenuDict[galleryCharacter]):
                imagebutton:
                    action Function(galleryIncreasePageNumber)
                    idle "/oscarAdditions/images/button.png"
                    hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
                text "Next":
                    style "galleryBody"
                    xcenter 0.5
                    ycenter 0.5

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for i in sceneGalleryMenuDict[galleryCharacter][galleryPageNumber]:
            $ scopeDict = {"player_name":persistent.player_name, "Mom_name":"Rachel", "Aunt_name":"Diana", "Dad_name":"Adam"}
            $ scopeDict.update(i[1])
            imagebutton:
                action Replay(i[0], scope=scopeDict, locked=False)
                idle Transform(i[2], zoom=0.2)
                hover Transform(im.MatrixColor(i[2], im.matrix.brightness(0.2)), zoom=0.2)


label before_devilappear2:
    menu:
        A "(Maybe this is a bad idea. So what is it gonna be?)"

        "Put your hand on her chest":
            $ chest = "hand"

        "Use Selina":
            $ chest = "none"

    jump devilappear2
