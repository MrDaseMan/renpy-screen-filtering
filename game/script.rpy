define ai = Character('Aiko', color="#c8ffc8")
define me = Character('Me', color="#c8ffc8")

transform ai_zoomed: 
    xanchor 0.5
    xpos 0.5
    ypos 0.1
    zoom 0.4

transform bg_zoomed: 
    zoom 1.1

transform bg_zoomed2: 
    zoom 1.2

define main_theme = "audio/main-theme.mp3"

label start:
    $ quick_menu = False
    window hide

    scene bg park at bg_zoomed
    play music main_theme fadein 0.5
    show ai summersera frown blush at ai_zoomed

    window show
    $ quick_menu = True

    "Today, Aiko and I are spending time together again."
    "We do it every weekend and, to be honest, I can't imagine my life without her anymore."
    "It seems like we only recently met..."

    $ filter.enable("sepia", Fade(0.5, 1.0, 0.5, color="#ffffff"))

    "It was a tranquil summer day when I first met Aiko."
    "The sun was shining, and the air was filled with the sweet scent of blooming flowers."
    "I remember walking through the park, feeling the warmth of the sun on my skin, and my mind was restless."
    "That's when I saw her, sitting on a bench, immersed in a book."
    "Her presence was captivating, and I felt drawn to her like a moth to a flame."
    
    menu:
        "Approach Aiko":
            call get_closer
        "Ask Aiko to continue the conversation":
            call continue_conversation

    $ filter.disable("sepia", Fade(0.5, 1.0, 0.5, color="#ffffff"))

    "I feel a sense of connection, and I knew that it was time to say goodbye."
    "Today is the last day we see each other, our last spring."
    "Tomorrow, Aiko leaves for another prefecture and we'll never see each other again."
    "A tear involuntarily rolled down my cheek."
    "I want so much for us to always be together. But fate has decided otherwise."
    me "Aiko..."
    ai "Hm?..."
    "Aiko timidly looked from the clouds in the sky to me."
    me "I've been meaning to tell you for a long time."
    "My thoughts were confused and my heart was pounding furiously."
    me "Listen!{w=.5} I...{w=1.0}, I..."
    with hpunch
    me "{b}I LOVE YOU AIKO!{/b}"
    "Finally, I was able to say it! My shout was like a bolt of lightning through the park."
    "Now..."
    "Now it's time to say goodbye. I've said all I wanted to say, my conscience is clear."

    show ai summersera closed smile at ai_zoomed with dissolve
    "Before I could finish my thought, my lips were suddenly touched by Aiko's."

    $ quick_menu = False
    window hide
    scene black with Dissolve(2.0)
    "Now I'm happy. By all means, I'll wait for you, Aiko!"

    stop music fadeout 2.0
    pause (2.0)

    return

label get_closer:
    "Gathering my courage, I approached her, and as she looked up and smiled at me. I was spellbound."

    show ai summersera smile blush sepia at ai_zoomed with dissolve
    "We started talking, and her words felt like a melody in the breeze."
    "She had an effortless charm, and her laughter was like music to my ears."
    "Time seemed to slip away as we shared stories and dreams. The park transformed into our own little world, and I didn't want to leave."
    return

label continue_conversation:
    "As the sun dipped below the horizon, painting the sky in a symphony of colors, Aiko suggested continuing our chat over dinner."
    "I agreed, feeling a surge of excitement."

    scene bg sakura sepia at bg_zoomed2
    show ai summersera frown blush sepia at ai_zoomed
    with dissolve
    "As we walked to the nearby restaurant, I couldn't help but feel grateful for that fateful moment in the park."
    "That day marked the beginning of a journey filled with laughter, adventures, and unforgettable memories."
    "Aiko became a beacon of light in my life, and I cherished every moment with her."
    "As I sit here, reminiscing about that first meeting, I can't help but smile at the thought of the beautiful destiny that we built together."
    return