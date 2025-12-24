from function.core import Text_to_speech, speech_recognization
import webbrowser
import random
import subprocess
import logging 

speak = Text_to_speech.speak



class Websites:
    @staticmethod
    def google():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        logging.info("User requested to open Google.")

    @staticmethod
    def youtube():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        logging.info("User requested to open YouTube.")

    @staticmethod
    def facebook():
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
        logging.info("User requested to open Facebook.")

    @staticmethod
    def twitter():
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
        logging.info("User requested to open Twitter.")

    @staticmethod
    def instagram():
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
        logging.info("User requested to open Instagram.")

    @staticmethod
    def github():
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
        logging.info("User requested to open GitHub.")

    @staticmethod
    def linkedin():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
        logging.info("User requested to open LinkedIn.")

    @staticmethod
    def reddit():
        speak("Opening Reddit")
        webbrowser.open("https://www.reddit.com")
        logging.info("User requested to open Reddit.")

    @staticmethod
    def stackoverflow():
        speak("Opening Stack Overflow")
        webbrowser.open("https://stackoverflow.com")
        logging.info("User requested to open Stack Overflow.")

    @staticmethod
    def gmail():
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")
        logging.info("User requested to open Gmail.")

    @staticmethod
    def yahoo():
        speak("Opening Yahoo")
        webbrowser.open("https://www.yahoo.com")
        logging.info("User requested to open Yahoo.")

    @staticmethod
    def amazon():
        speak("Opening Amazon")
        webbrowser.open("https://www.amazon.com")
        logging.info("User requested to open Amazon.")

    @staticmethod
    def flipkart():
        speak("Opening Flipkart")
        webbrowser.open("https://www.flipkart.com")
        logging.info("User requested to open Flipkart.")

    @staticmethod
    def quora():
        speak("Opening Quora")
        webbrowser.open("https://www.quora.com")
        logging.info("User requested to open Quora.")

    @staticmethod
    def wikipedia():
        speak("Opening Wikipedia")
        webbrowser.open("https://www.wikipedia.org")
        logging.info("User requested to open Wikipedia.")

    @staticmethod
    def netflix():
        speak("Opening Netflix")
        webbrowser.open("https://www.netflix.com")
        logging.info("User requested to open Netflix.")

    @staticmethod
    def primevideo():
        speak("Opening Amazon Prime Video")
        webbrowser.open("https://www.primevideo.com")
        logging.info("User requested to open Prime Video.")

    @staticmethod
    def spotify():
        speak("Opening Spotify")
        webbrowser.open("https://www.spotify.com")
        logging.info("User requested to open Spotify.")

    @staticmethod
    def soundcloud():
        speak("Opening SoundCloud")
        webbrowser.open("https://www.soundcloud.com")
        logging.info("User requested to open SoundCloud.")

    @staticmethod
    def tiktok():
        speak("Opening TikTok")
        webbrowser.open("https://www.tiktok.com")
        logging.info("User requested to open TikTok.")

    @staticmethod
    def pinterest():
        speak("Opening Pinterest")
        webbrowser.open("https://www.pinterest.com")
        logging.info("User requested to open Pinterest.")

    @staticmethod
    def telegram():
        speak("Opening Telegram")
        webbrowser.open("https://web.telegram.org")
        logging.info("User requested to open Telegram.")

    @staticmethod
    def whatsapp():
        speak("Opening WhatsApp Web")
        webbrowser.open("https://web.whatsapp.com")
        logging.info("User requested to open WhatsApp.")

    @staticmethod
    def vimeo():
        speak("Opening Vimeo")
        webbrowser.open("https://www.vimeo.com")
        logging.info("User requested to open Vimeo.")

    @staticmethod
    def bing():
        speak("Opening Bing")
        webbrowser.open("https://www.bing.com")
        logging.info("User requested to open Bing.")

    @staticmethod
    def stackexchange():
        speak("Opening Stack Exchange")
        webbrowser.open("https://stackexchange.com")
        logging.info("User requested to open Stack Exchange.")

    @staticmethod
    def hackernews():
        speak("Opening Hacker News")
        webbrowser.open("https://news.ycombinator.com")
        logging.info("User requested to open Hacker News.")

    @staticmethod
    def medium():
        speak("Opening Medium")
        webbrowser.open("https://medium.com")
        logging.info("User requested to open Medium.")

    @staticmethod
    def devto():
        speak("Opening Dev.to")
        webbrowser.open("https://dev.to")
        logging.info("User requested to open Dev.to.")

    @staticmethod
    def cnn():
        speak("Opening CNN")
        webbrowser.open("https://www.cnn.com")
        logging.info("User requested to open CNN.")

    @staticmethod
    def bbc():
        speak("Opening BBC")
        webbrowser.open("https://www.bbc.com")
        logging.info("User requested to open BBC.")



class Apps:
    @staticmethod
    def calculator():
        speak("Opening Calculator")
        subprocess.Popen("calc.exe")
        logging.info("User requested to open Calculator.")

    @staticmethod
    def notepad():
        speak("Opening Notepad")
        subprocess.Popen("notepad.exe")
        logging.info("User requested to open Notepad.")

    @staticmethod
    def cmd():
        speak("Opening Command Prompt")
        subprocess.Popen("cmd.exe")
        logging.info("User requested to open Command Prompt.")

    @staticmethod
    def powershell():
        speak("Opening PowerShell")
        subprocess.Popen("powershell.exe")
        logging.info("User requested to open PowerShell.")

    @staticmethod
    def word():
        speak("Opening Microsoft Word")
        subprocess.Popen(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
        logging.info("User requested to open Word.")

    @staticmethod
    def excel():
        speak("Opening Microsoft Excel")
        subprocess.Popen(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
        logging.info("User requested to open Excel.")

    @staticmethod
    def powerpoint():
        speak("Opening PowerPoint")
        subprocess.Popen(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")
        logging.info("User requested to open PowerPoint.")

    @staticmethod
    def teams():
        speak("Opening Microsoft Teams")
        subprocess.Popen(r"C:\Users\YourUserName\AppData\Local\Microsoft\Teams\Update.exe")
        logging.info("User requested to open Teams.")

    @staticmethod
    def outlook():
        speak("Opening Outlook")
        subprocess.Popen(r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE")
        logging.info("User requested to open Outlook.")

    @staticmethod
    def chrome():
        speak("Opening Google Chrome")
        subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
        logging.info("User requested to open Chrome.")

    @staticmethod
    def firefox():
        speak("Opening Mozilla Firefox")
        subprocess.Popen(r"C:\Program Files\Mozilla Firefox\firefox.exe")
        logging.info("User requested to open Firefox.")

    @staticmethod
    def edge():
        speak("Opening Microsoft Edge")
        subprocess.Popen(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        logging.info("User requested to open Edge.")

    @staticmethod
    def spotify():
        speak("Opening Spotify")
        subprocess.Popen(r"C:\Users\YourUserName\AppData\Roaming\Spotify\Spotify.exe")
        logging.info("User requested to open Spotify.")

    @staticmethod
    def vlc():
        speak("Opening VLC Media Player")
        subprocess.Popen(r"C:\Program Files\VideoLAN\VLC\vlc.exe")
        logging.info("User requested to open VLC.")

    @staticmethod
    def zoom():
        speak("Opening Zoom")
        subprocess.Popen(r"C:\Users\YourUserName\AppData\Roaming\Zoom\bin\Zoom.exe")
        logging.info("User requested to open Zoom.")

    @staticmethod
    def paint():
        speak("Opening Paint")
        subprocess.Popen("mspaint.exe")
        logging.info("User requested to open Paint.")

    @staticmethod
    def snippingtool():
        speak("Opening Snipping Tool")
        subprocess.Popen("snippingtool.exe")
        logging.info("User requested to open Snipping Tool.")

    @staticmethod
    def sticky_notes():
        speak("Opening Sticky Notes")
        subprocess.Popen("stikynot.exe")
        logging.info("User requested to open Sticky Notes.")

    @staticmethod
    def wordpad():
        speak("Opening WordPad")
        subprocess.Popen("write.exe")
        logging.info("User requested to open WordPad.")

    @staticmethod
    def camera():
        speak("Opening Camera")
        subprocess.Popen("microsoft.windows.camera:")
        logging.info("User requested to open Camera.")

    @staticmethod
    def control_panel():
        speak("Opening Control Panel")
        subprocess.Popen("control.exe")
        logging.info("User requested to open Control Panel.")

    @staticmethod
    def task_manager():
        speak("Opening Task Manager")
        subprocess.Popen("taskmgr.exe")
        logging.info("User requested to open Task Manager.")

    @staticmethod
    def file_explorer():
        speak("Opening File Explorer")
        subprocess.Popen("explorer.exe")
        logging.info("User requested to open File Explorer.")

    @staticmethod
    def cmd_prompt():
        speak("Opening Command Prompt")
        subprocess.Popen("cmd.exe")
        logging.info("User requested to open Command Prompt.")

    @staticmethod
    def registry_editor():
        speak("Opening Registry Editor")
        subprocess.Popen("regedit.exe")
        logging.info("User requested to open Registry Editor.")

    @staticmethod
    def powershell_ise():
        speak("Opening PowerShell ISE")
        subprocess.Popen("powershell_ise.exe")
        logging.info("User requested to open PowerShell ISE.")

    @staticmethod
    def system_information():
        speak("Opening System Information")
        subprocess.Popen("msinfo32.exe")
        logging.info("User requested to open System Information.")

    @staticmethod
    def disk_cleanup():
        speak("Opening Disk Cleanup")
        subprocess.Popen("cleanmgr.exe")
        logging.info("User requested to open Disk Cleanup.")

    @staticmethod
    def event_viewer():
        speak("Opening Event Viewer")
        subprocess.Popen("eventvwr.msc")
        logging.info("User requested to open Event Viewer.")

    @staticmethod
    def services():
        speak("Opening Services")
        subprocess.Popen("services.msc")
        logging.info("User requested to open Services.")

    @staticmethod
    def device_manager():
        speak("Opening Device Manager")
        subprocess.Popen("devmgmt.msc")
        logging.info("User requested to open Device Manager.")





