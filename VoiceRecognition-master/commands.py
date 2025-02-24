from datetime import *
import pandas as pd 
from google_trans_new import google_translator
import os
import platform
import pyttsx3
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys
import wikipedia

plat = platform.platform()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
translator = google_translator()  

class base_functions:
    def __init__(self):
        pass

    def say(self, text):
        engine.say(text)
        engine.runAndWait()


class commands:
    def __init__(self):
        self.running = True
        self.sleep = False
        self.date = str(date.today())
        os.chdir("./Notes")
        self.dirs_note_dir = os.listdir()
        os.chdir("..")
        self.base = base_functions()
        self.note_t = 0
        self.driver = webdriver.Chrome()
        self.intro = "hieeeeeeee what is up , my name is walter white , hihihi just kidding i am your personal servant here to provide you with all your needs , yes even with those lame ass conversation openers for instagram, "
        if self.date in self.dirs_note_dir:
            os.chdir("./NoteNumber")
            with open(self.date, "r") as f:
                self.note_t = int(f.read())
                print(self.note_t)
            os.chdir("..")
        else:
            os.chdir("./Notes")
            with open(self.date, "w+") as f:
                f.write("Today's Notes")
            os.chdir('..')
            os.chdir("./NoteNumber")
            print(os.curdir)
            with open(self.date, "w+") as f:
                f.write("0")
            os.chdir("..")

    def intro(self):
        self.base.say(self.intro)
    def introduce(self, said):
        if "introduce yourself" in said:
            self.base.say(self.intro)
    def check_termination(self):
        pass

    def name(self, text):
        if "what" in text and "name" in text:
            self.base.say("My name is lolo")

    def how(self, text):
        if "how" in text and "you" in text and "are" in text:
            self.base.say("I am fit and fine, what can I do for you")

    def hi(self, text):
        if "hello" in text:
            self.base.say("Hello There, what can i do for you?\n")

    def exit(self, text):
        if "exit" in text:
            self.base.say("Exiting the program\n")
            self.running = False
            os.chdir("./NoteNumber")
            with open(self.date, "w+") as f:
                f.write(str(self.note_t))
            os.chdir("..")

    def note(self, text):
        if "note" in text and "write" in text:
            self.note_t+=1
            print("Taking you to noting MODE")
            self.base.say("Please say the notes")
            r = sr.Recognizer()
            # to close the mic after listening
            with sr.Microphone() as mic:
                r.adjust_for_ambient_noise(mic)
                print("Listening for notes...\n")
                # listening the sudden change in amplitude in the voice input
                audio = r.listen(mic)
                # var for string of audio
                said = ""
                # update for progress
                print("Recognizing the note\n")
                # in case error
                try:
                    # synthesizing the raw audio
                    said = r.recognize_google(audio)
                    print("You said", said)

                # Exception
                except Exception as e:
                    print("Exception", str(e))

            if said == "cancel" or said == "exit":
                self.base.say("Cacelled the noting")
            else:
                os.chdir("./Notes")
                with open(self.date, "a") as f:
                    f.write("\n")
                    f.write(str(self.note_t)+" ) "+said)
                    self.base.say("Saved the file")
                os.chdir("..")

    def check_sleep(self, text):
        if "go to sleep" in text:
            self.sleep = True
            self.base.say("Went to sleep mode")
            while self.sleep:
                r = sr.Recognizer()
                with sr.Microphone() as mic:
                    r.adjust_for_ambient_noise(mic)
                    print("Waiting for the Wake Up Command\n")
                    audio = r.listen(mic)
                    said = ""
                    print("Recognizing\n")
                    try:
                        said = r.recognize_google(audio)
                        print(said)

                    except Exception as e:
                        print("Exception", str(e))
                
                if "get up" in said:
                    self.sleep = False
                    self.base.say("Welcome back sir")
                else:
                    self.sleep = True

    def time(self, said):
        if "time" in said and "what" in said:
            print("Go check the Clock...")
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            current_time = current_time.replace(":", "_")
            self.base.say(current_time)

    def show_notes(self, said):
        if "tell" in said and "notes" in said:
            self.base.say("Under Development")

    def tell_age(self, said):
        if "age" in said and "what" in said:
            self.base.say("My age is hundred years")

    def wiki_search(self, said):
        if "search" in said and "wikipedia" in said:
            self.base.say(wikipedia.summary(said[18:]))
            wikipedia.summary(said[18:])

    def translate(self, said):
        if 'translate' in said and 'for me' in said:
            to_translate_temp = said[17:]
            self.base.say("Indev")

    def googleSearch(self, said):
        if "search" in said and "google" in said:
            arr = said.split()
            found = False
            string=""
            for i in arr:
                if i == "search":
                    found = True
                if found:
                    string+= (i+" ")
            tosearch = string[7:]
            urlTogo = "https://www.google.com/search?q="+tosearch
            self.driver.get(urlTogo)
