import random
import pygame
import os
import time
import sys
import basic
import threading
import shutil
from colorama import Fore, Style
import musicplayer


ozzy_facts = [
    " Ozzy once bit the head off a bat... on stage.",
    " Tony Iommi played with prosthetic fingertips made from plastic bottles.",
    "Lemmy from Motörhead drank a bottle of Jack a day.",
    "Bill Ward set himself on fire by accident during a gig.",
    "Sabbath invented metal while tuning down to match Tony’s severed fingers.",
    "Never trust a quiet riff... it might explode.",
]

# Display text with a typewriter-style animation
def typewriter(text, delay=0.002):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

# Load ASCII intro
def load_ascii_face():
    face_path = os.path.join(os.path.dirname(__file__), "ozzy_face.txt")
    if os.path.exists(face_path):
        with open(face_path, "r", encoding="utf-8") as f:
            return f.read()
    return "[Ozzy face not found]"

#Play intro sound in background
def play_intro_sound():
    time.sleep(5)
    pygame.mixer.init()
    intro_path = os.path.join(os.path.dirname(__file__), "sounds", "intro.mp3")
    if os.path.exists(intro_path):
        try:
            sound = pygame.mixer.Sound(intro_path)
            sound.play()
        except Exception as e:
            print(f"[Startup Sound Error] {e}")
    else:
        print("[Warning] intro.mp3 not found!")

# Show intro (concurrently run sound and ASCII)
def show_intro():
    sound_thread = threading.Thread(target=play_intro_sound)
    sound_thread.start()
    ascii_face = load_ascii_face()
    typewriter(ascii_face, delay=0.0000001)
    print("\n\t\tType 'Bless Bat = 666' to begin the madness!\n")
def play_ritual_audio(audio_file="ritual.mp3"):
    try:
        pygame.mixer.init()
        pygame.mixer.music.stop()  # Stop any current music
        path = os.path.join(os.path.dirname(__file__), "sounds", audio_file)
        if os.path.exists(path):
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
        else:
            print(f"[Warning] {audio_file} not found.")
    except Exception as e:
        print(f"[Audio Error] {e}")


#Farewell Tribute on Exit
def farewell_tribute(quote, audio_file="mama.mp3"):
    try:
        pygame.mixer.init()
        path = os.path.join(os.path.dirname(__file__), "sounds", audio_file)
        if os.path.exists(path):
            sound = pygame.mixer.Sound(path)
            channel = sound.play()
        else:
            print(f"[Warning] {audio_file} not found.")
            channel = None
    except Exception as e:
        print(f"[Farewell Audio Error] {e}")
        channel = None

    # Center and print each line of the quote
    cols = shutil.get_terminal_size().columns
    lines = quote.strip("\n").split("\n")
    print(Fore.YELLOW + Style.BRIGHT)
    for line in lines:
        print(line.center(cols))
    print(Style.RESET_ALL)

    # Wait for audio to finish
    if channel:
        while channel.get_busy():
            time.sleep(0.1)

    print(Fore.RED + Style.BRIGHT + "\n💀 ROCK IN PEACE.\n")
    time.sleep(1)
    sys.exit(0)






def metal_prompt():
    prompts = [
        "OZZY SPEAKS > ",
        "BARK YOUR COMMAND > ",
        "UNLEASH DARKNESS > ",
        "WHAT IS THY WILL > ",
        "SPELL YOUR CURSE > ",
    ]
    return input(random.choice(prompts))

chaos_mode = False

if __name__ == "__main__":
    show_intro()

    while True:
        
        
		
                
        
        text = metal_prompt()
        
        if text.strip() == "":
            continue
        if text.lower().startswith("runfile "):
            filename=text[8:].strip()
            if filename.endswith("ozzy") and os.path.exists(filename):
                with open(filename,"r") as f:
                    code=f.read()
                result,error =basic.run(filename,code)
                if error:
                    print(error.as_string())
                elif result:
                    print(repr(result))
            else:
                print("Only .ozzy files are allowed")
            continue
        if text.lower().startswith("playfile "):
            musicplayer.play_file(text[9:].strip())
            continue
        if text.lower()=="pause":
            musicplayer.pause()
        if text.lower()=="resume":
            musicplayer.resume()
            continue
        if text.lower() =="stop":
            musicplayer.stop()
            continue
        if text.lower().startswith("volume "):
            musicplayer.set_volume(text[7:].strip())
            continue
        
        if text.lower().startswith("spotifysearch "):
            from webbrowser import open as open_browser
            song=text[14:].strip()
            url = f"https://open.spotify.com/search/{song.replace(' ', '%20')}"
            open_browser(url)
            print(f"Searching Spotify for : {song}")
            continue
        if text.lower() == "help":
            print("""
OzzyLang Syntax Guide 

Core Shell Commands:
• scream "text"         → print a loud message
• chant "text"          → same as scream (stops music)
• yell "text"           → another loud message
• runfile path.ozzy     → run an OzzyLang script from a file
• help                  → show this help menu
• rock in peace         → exit the shell

Rituals & Chaos:
• summon ozzy           → play default ritual track
• summon chaos          → enable chaos mode
• banish chaos          → disable chaos mode
• animate bat N         → animate flying bats
• paint chaos N         → display glitch chaos effect
• summon bat = N        → same as animate bat N
• glitch blood = N      → same as paint chaos N

Music & Visuals:
• playfile path         → play a local .mp3 file
• pause / resume / stop → control music playback
• volume 0.5            → set volume (0.0 to 1.0)
• visualize             → mic-based real-time visualizer
• visualizefile path    → bar visualizer for local .mp3

External Tools:
• spotifysearch name    → open Spotify search in browser

Language Keywords (for use in .ozzy scripts):
• BLESS             → variable declaration (like VAR)
• CRY                → if condition
• THENCRY        → else if (elif)
• BEWARE         → else
• SHRED var=value TO val AMP step(optional) → for loop (like: SHRED i=1 TO 5 AMP 1 THEN)
• BLAST condition       → while loop
• RIFF name(args)       → define function
• CURSE value           → return from function
• RIDE                  → continue (loop)
• SMASH                 → break (loop)
• AND / OR / NOT        → logical operators
• THEN                  → keyword to start block (optional)
• END                   → end any block or function

.ozzy Scripting:
- You can write OzzyLang code in `.ozzy` files.
- Run them using: runfile yourscript.ozzy

Example:
    BLESS count = 3
    CRY count > 0 THEN
        SCREAM ("Still alive!")
    END

 Tip: All keywords are case-SENSITIVE, and designed with metal vibes 
""")
    

        

        if text.strip().lower() == "rock in peace":
            farewell_tribute(
                quote="""
THANK YOU
FOR EVERYTHING,
PRINCE OF DARKNESS!
""",
                audio_file="mama.mp3"
            )
            sys.exit(0)
            

		

        # --- CHAOS COMMANDS ---
        if text.lower() == "summon chaos":
            chaos_mode = True
            print("PRINCE OF DARKNESS AWAKEN")
            continue
        if text.lower() =="banish chaos":
            chaos_mode = False
            print("BANISHED")
            continue

        if chaos_mode:
            if text.lower().startswith("scream"):
                msg = text[7:].strip('" ')
                for _ in range(3):
                    print(f"\033[91m⚡ {msg.upper()} ⚡\033[0m")
                    time.sleep(0.3)
                continue
            elif text.lower().startswith("paint chaos"):
                try:
                    count = int(text.split()[-1])
                    for _ in range(count):
                        print(random.choice([
                            "\033[95m~(=^\u0361‿͡^)\u30ce﻿\033[0m",
                            "\033[94m/\\/\\/\\//\\ GLITCH \033[0m",
                            "\033[96mBAT SCRATCH ☠️\033[0m",
                            "\033[93m**CRASHING COLORS**\033[0m"
                        ]))
                        time.sleep(0.2)
                except:
                    print("Use like: paint chaos 5")
                continue
            elif text.lower().startswith("animate bat"):
                try:
                    n = int(text.split()[-1])
                    bat = "🦇"
                    for i in range(n):
                        for col in range(20):
                            print(" " * col + bat, end='\r', flush=True)
                            time.sleep(0.05)
                        print()
                except:
                    print("Use like: animate bat 3")
                continue
        if text.strip() in ["help", "rock in peace", ""]:
            continue

        result, error = basic.run('<stdin>', text)
        if text.lower() =="visualize":
            from visualizer import show_visualizer
            show_visualizer(duration=15)
            continue

        if not text.strip().lower().startswith("scream"):
            basic.last_scream_played = False
        if text.lower() =="summon ozzy":
            play_ritual_audio("ritual.mp3")
            typewriter("The RITUAL BEGINS...\n",0.01)
            time.sleep(1)
            typewriter("Blood of the bat... poured.\n",0.01)
            time.sleep(1)
            typewriter("Pentagram Drawn...\n",0.01)
            time.sleep(1)
            typewriter("OZZY HAS AWAKENED.SPEAK, MORTAL\n",0.01)
            time.sleep(1)
            
            continue
        

    		
            
		
                
        if error:
            print(error.as_string())
        elif result:
            if result and random.random() < 0.2:
                print(random.choice(ozzy_facts))

            if hasattr(result, 'elements') and len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(repr(result))
