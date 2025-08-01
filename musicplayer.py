import os
from pygame import mixer

def init_mixer():
    if not mixer.get_init():
        mixer.init()

def play_file(file_path):
    try:
        init_mixer()
        abs_path = os.path.join(os.path.dirname(__file__), file_path)
        mixer.music.load(abs_path)
        mixer.music.play()
        print(f"Playing: {file_path}")
    except Exception as e:
        print(f"[Audio Error] {e}")

def pause():
    try:
        init_mixer()
        mixer.music.pause()
        print("⏸Music paused.")
    except Exception as e:
        print(f"[Pause Error] {e}")

def resume():
    try:
        init_mixer()
        mixer.music.unpause()
        print("▶Music resumed.")
    except Exception as e:
        print(f"[Resume Error] {e}")

def stop():
    try:
        init_mixer()
        mixer.music.stop()
        print("Music stopped.")
    except Exception as e:
        print(f"[Stop Error] {e}")

def set_volume(volume):
    try:
        init_mixer()
        vol = float(volume)
        if 0.0 <= vol <= 1.0:
            mixer.music.set_volume(vol)
            print(f"Volume set to {vol}")
        else:
            print("Volume must be between 0.0 and 1.0")
    except Exception as e:
        print(f"[Volume Error] {e}")

def is_playing():
    return mixer.get_init() and mixer.music.get_busy()


