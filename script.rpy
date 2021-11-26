# characters

define you = Character("You") # player
define uk_cha = Character("??") # Unknow character dialogue name
define autumn = Character("Autumn") # Autumn
define winter = Character("Winter") # Winter
define spring = Character("Spring") # Spring


# images, resize to screen size,

image black = im.Scale("black.png", 1280, 720) # black screen
image op_eye = im.Scale("op-eye.png", 1280, 720) # barely open eyes
image op = im.Scale("op.png", 1280, 720) # opening
image a = im.Scale("a.png", 1280, 720) # autumn_1
image a_2 = im.Scale("a-2.png", 1280, 720) # autumn_2
image a_night = im.Scale("a-night.png", 1270, 720) # autumn_night
image a_c = im.Scale("a-c.png", 1280, 720) # autumn_change

image w = im.Scale("w.png", 1280, 720) # winter_1
image w_2 = im.Scale("w-2.png", 1280, 720) # winter_2
image w_night = im.Scale("w-night.png", 1270, 720) # winter_night
image w_c = im.Scale("w-c.png", 1280,720) # winter_change

image s = im.Scale("s.png", 1280, 720) # spring_1
image s_2 = im.Scale("s-2.png", 1280, 720) # spring_2
image s_night = im.Scale("s-night.png", 1270, 720) # spring_night
image s_c = im.Scale("s-c.png", 1280, 720) # spring_change

image autumn_cha = im.Scale("autumn-cha.png", ) # autumn character image
image winter_cha = im.Scale("winter-cha.png", ) # winter character image
vimage spring_cha = im.Scale("spring-cha.png", ) # spring character image

# start of the game

label start:
    scene black with fade # black nacground

    uk_cha "Hey!"
    uk_cha "Hey you!"

      # hide black background
    scene op_eye with fade
    hide black

    you "Your eyes open just slightly, still getting used to the light"

    uk_cha "You finally woke up"

    menu first_encounter: # first encounter
        "Where am I?":
            jump fe_where

        "Who are you?":
            jump fe_who

label fe_where:

    uk_cha "We are on a mountain, you were just sleeping under this tree"

    you "Your eyes finally see the tree and the voice, the voice is coming from a pink haired girl"


    show op with fade
    hide op_eye

    you "You ask her what her name is"

    uk_cha "I'm Spring!"

    jump chapter_1

label fe_who:

    uk_cha "I'm Spring!"
    spring "I just found you here on this mountain"

    you "Your eyes finally see the big tree, there is a pink haired girl in front of you"

    jump chapter_1

label chapter_1:


    spring "Why where you sleeping in here?"

    you "You shake your head, not quite sure why"
    you "At this point you stand up, and take a look around"

    show a with fade
    hide op

    you "There are a lot of trees, and fallen leaves everywhere"
    you "Just then a different voice comes from behind"

    uk_cha "Spring, who are you talking to?"

    spring "I found this guy in the middle of this forest, he just woke up"

    uk_cha "Oh hi, my name is Autumn"

    autumn "What are you doing here?"

    menu:
        "I don'know":
            pass

    spring "That is very weird"
    spring "Do you know anything about how you ended up here or your name?"

    you "You still don't know the answer to any of her questions"

    autumn "You seem to be very confused"

    spring "Do you want to come with us?"
    spring "We are just travelling around, maybe we can find where you even came from"

    menu:
        "Sorry, I will continue here, sleeping":
            jump end_1

        "I'll go with you":
            jump chapter_1_2

label chapter_1_2:

    spring "We wanted to go on top of the mountain, to see the views"

    autumn "We should find Winter there"

    spring "Oh, true! Winter is also with us, you'll see her when we get to the top"

    show a_2 with dissolve
    hide a

    you "You finally see the end of the rock road, at the end, there is a huge tree, and the sky can be clearly seen"

    spring "Winteeer, we found this guy sleeping under a tree"

    winter "What?"

    spring "Yeah he doesn't know how he ended up there"
    spring "He will be coming with us"

    winter "Ok, I don't really mind"

    spring "Perfect!"

    autumn "This view is amazing, isn't it?"

    winter "It's quite relaxing"

    you "You stay there for a long time, looking at the view"

    you  "Suddenly, a mild wind brushes you skin."

    autumn "It's getting a bit cold, we should head back to the forest"

    spring "Lets head back"

    show a_night with fade
    hide a_2 with fade

    autumn "Night seems to be approaching"

    spring "Yeah, it's quite dark already"
    spring "Lets just sleep under the trees"

    show black with fade
    hide a_night

    you "You fall asleep in the middle of the forest, just like where they found you"

    show a with fade
    hide a_night

    spring "Good morning!"

    winter "Good morning"

    spring "Where is Autumn?"

    winter "No idea"

    you "You shake your head, not knowing either the answer to the question"

    spring "He might be on top of the mountain, maybe he woke up very early"

    winter "We should go check there"

    show black
    hide a

    spring "WHAT THE F-!"

    show a_c
    hide black

    you "The moment you see the tree, you realise where Autumn is"
    you "His body hanging right under the tree"

    spring "Autumn?"
    spring "Autumn?!!"

    you "Still, no movement, Autumn is dead"

    show black with fade
    hide a_c

    you "You suddenly black out, everything around you falls apart"

    jump chapter_2

label chapter_2:

    show w with fade
    hide black

    spring "What is happening?"

    winter "I don't know"
    winter "All the leaves are gone"

    spring "We aren't even on the mountain anymore!"
    spring "There is so much snow"
    spring "How did we even get here?"

    you "You take a look around, there are some dead trees, and a small river"

    spring "Wait isn't that the mountain?"

    you "You can barely see the mountain far away, it's all covered in snow"

    spring "How is that even possible?"
    spring "Did you do anything to us?"

    menu:
        "I didn't!":
            pass

    spring "I, I don't understadn what's happening"

    you "The sky is very dark"

    winter "Let's try to find somewhere to rest, it's very dark"
    winter "We might find something by following the river"

    spring "But, but Autumn is still up there!"

    winter "It's all covered in snow, we won't find him"
    winter "We are all going to die, if we try to find him"
    winter "Just move on"

    spring "I don't understand anything anymore"

    winter "So, are you guys coming with me?"

    menu river_choice:
        "What else can we do anyways?":
            jump chapter_2_2

        "You guys can go, I will just stay here":
            jump end_2

label chapter_2_2:

    you "While going down the river, you notice a bunch of dead trees"

    show w_2 with fade
    hide w

    spring "Everything is so dead here"

    winter "It's too cold, nothing is going to grow"

    show w_night with fade
    hide w_2

    spring "God damm it, it's so dark again!"

    winter "Night seems to be approaching again"
    winter "Lets go back to the bridge we miht be able to sleep there"

    show w with fade
    hide w_night

    you "Once again, you close your eyes to sleep"

    show black with fade
    hide w

    you "Zzzzz"

    show w_c with fade
    hide black

    you "You wake up, and take look around, you see something floating on the river"
    you "It's Winter's corpse"
    you "The posibility of Spring being the killer is present in your mind"

    menu winter_escape:
        "Escape from her":
            jump end_3

        "Continue with her":
            jump chapter_3

label chapter_3:

    you "You black out again, just like what happened after Autumn was found"

    show s
    hide a_c

    spring "Again?"
    spring "We teleported again?"
    spring "What is happening?"
    spring "What is that tree doing there?"

    you "You ig nore her, and start travelling to the huge tree"

    spring "Hey!, wait, where are you going?"

    show s_2 with fade
    hide s

    spring "What are you doing?!"
    spring "Tell me the truth!"
    spring "What happened to Autumn and Winter?"
    spring "Did you kill them?!"

    menu:
        "Yes":
            pass

        "No":
            pass

    you "I killed them"

    spring "WHAT IS WRONG WITH YOU?"

    you "Just as she finishes the sentence, you feel and urge to kill her aswell"

    show black with fade
    hide s_2

    you "You can only hear her screams as you hang her on the tree"
    you "A few minutes pass, and she finally goes silent"

    show s_c
    hide black

    you "You killed them yourself"
    you "You are the murderer"
    you "You black out again"

    show black with fade
    hide s_c

    you "Everything goes dark"

    jump end_4

label end_1:

    spring "We wish you good luck and farewell!"

    you "You go back to sleep, wondering what would have happened if you went with them"

    return

label end_2:

    winter "Well, I don't know what are you going to do"
    winter "This might be better for all of us"
    winter "But good luck"

    show black with fade
    hide w

    you "You lay down on the snow, and close your eyes"
    you "Not quite sure what happened"
    you "This is the end for you"

    return

label end_3:

    you "You try to escape from her, but there is too much snow"
    you "What if she wasn't the murderer?"

    show black with fade
    hide w_c

    you "You lose all your energy, and fall on the ground"
    you "This is the end for you"

    return

label end_4:

    jump start
