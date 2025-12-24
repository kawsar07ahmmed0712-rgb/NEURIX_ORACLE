from function.core import Text_to_speech
import os, random, logging

speak = Text_to_speech.speak

BASE_MUSIC_DIR = r"C:\Users\USER\DATA-SCINCE-AI\INCEPTION_BD_WORKSPACE\FSDS_BOOTCAMP\FSDS_LESSONS\NEURIX_ORACLE\assets\music"
BASE_VIDEO_DIR = r"C:\Users\USER\DATA-SCINCE-AI\INCEPTION_BD_WORKSPACE\FSDS_BOOTCAMP\FSDS_LESSONS\NEURIX_ORACLE\assets\videos"


def play_from_folder(base_dir, folder_name, media_type="song"):
    try:
        path = os.path.join(base_dir, folder_name)
        files = os.listdir(path)

        if files:
            media = random.choice(files)
            speak(f"Playing {folder_name} {media_type} sir")
            os.startfile(os.path.join(path, media))
            logging.info(f"Playing {media_type}: {folder_name}/{media}")
        else:
            speak(f"{folder_name} folder is empty sir")

    except Exception as e:
        speak("Sorry sir, I could not play this media")
        logging.error(e)



# MUSIC
def play_alan_walker():
    play_from_folder(BASE_MUSIC_DIR, "alan_walker")

def play_artcell():
    play_from_folder(BASE_MUSIC_DIR, "artcell")

def play_odd_signature():
    play_from_folder(BASE_MUSIC_DIR, "odd_signature")

def play_passenger():
    play_from_folder(BASE_MUSIC_DIR, "passenger")

def play_anuv_zain():
    play_from_folder(BASE_MUSIC_DIR, "anuv_zain")

def play_atif_aslam():
    play_from_folder(BASE_MUSIC_DIR, "atif_aslam")

def play_arijit_singh():
    play_from_folder(BASE_MUSIC_DIR, "arijit_singh")

def play_shreya_ghoshal():
    play_from_folder(BASE_MUSIC_DIR, "shreya_ghoshal")

def play_kishore_kumar():
    play_from_folder(BASE_MUSIC_DIR, "kishore_kumar")

def play_lata_mangeshkar():
    play_from_folder(BASE_MUSIC_DIR, "lata_mangeshkar")

def play_bollywood_song():
    play_from_folder(BASE_MUSIC_DIR, "bollywood_movie")

def play_hollywood_song():
    play_from_folder(BASE_MUSIC_DIR, "hollywood_movie")

def play_bangla_modern():
    play_from_folder(BASE_MUSIC_DIR, "bangla_modern")

def play_bangla_folk():
    play_from_folder(BASE_MUSIC_DIR, "bangla_folk")

def play_lofi():
    play_from_folder(BASE_MUSIC_DIR, "lofi")

def play_sad_song():
    play_from_folder(BASE_MUSIC_DIR, "sad_song")

def play_romantic_song():
    play_from_folder(BASE_MUSIC_DIR, "romantic_song")

def play_motivational_song():
    play_from_folder(BASE_MUSIC_DIR, "motivational_song")

def play_english_pop():
    play_from_folder(BASE_MUSIC_DIR, "english_pop")

def play_instrumental():
    play_from_folder(BASE_MUSIC_DIR, "instrumental")


# VIDEOS

def play_sports_video():
    play_from_folder(BASE_VIDEO_DIR, "sports", "video")

def play_football_video():
    play_from_folder(BASE_VIDEO_DIR, "football", "video")

def play_cricket_video():
    play_from_folder(BASE_VIDEO_DIR, "cricket", "video")

def play_video_game():
    play_from_folder(BASE_VIDEO_DIR, "video_game", "video")

def play_gaming_montage():
    play_from_folder(BASE_VIDEO_DIR, "gaming_montage", "video")

def play_esports():
    play_from_folder(BASE_VIDEO_DIR, "esports", "video")

def play_quran_tilawat():
    play_from_folder(BASE_VIDEO_DIR, "quran_tilawat", "video")

def play_islamic_waz():
    play_from_folder(BASE_VIDEO_DIR, "islamic_waz", "video")

def play_documentary():
    play_from_folder(BASE_VIDEO_DIR, "documentary", "video")

def play_science_video():
    play_from_folder(BASE_VIDEO_DIR, "science_video", "video")

def play_technology_video():
    play_from_folder(BASE_VIDEO_DIR, "technology", "video")

def play_ai_video():
    play_from_folder(BASE_VIDEO_DIR, "ai_ml", "video")

def play_programming_video():
    play_from_folder(BASE_VIDEO_DIR, "programming", "video")

def play_movie_scene():
    play_from_folder(BASE_VIDEO_DIR, "movie_scene", "video")

def play_short_film():
    play_from_folder(BASE_VIDEO_DIR, "short_film", "video")

def play_motivation_video():
    play_from_folder(BASE_VIDEO_DIR, "motivation", "video")

def play_travel_vlog():
    play_from_folder(BASE_VIDEO_DIR, "travel_vlog", "video")

def play_nature_video():
    play_from_folder(BASE_VIDEO_DIR, "nature", "video")

def play_space_video():
    play_from_folder(BASE_VIDEO_DIR, "space", "video")

def play_history_video():
    play_from_folder(BASE_VIDEO_DIR, "history", "video")
