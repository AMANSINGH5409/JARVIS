import datetime
import sys
import time
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import psutil
import PyPDF2
import gettext


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
  hour = int(datetime.datetime.now().hour)
  tt = time.strftime("%I:%M %p")
  if hour >= 0 and hour < 12:
    speak(f"Good Morning!,its {tt}")
  elif hour >= 12 and hour < 18:
    speak(f"Good Afternoon!,its {tt}")
  else:
    speak(f"Good Evening!,its {tt}")

  speak("I am Jarvis, Please tell me how may I help you")

def takeCommand():
# It takes mic input from user and returns string output
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening..........")
      r.pause_threshold = 1
      r.energy_threshold = 350
      audio = r.listen(source)

   try:
     print("Recognizing.....")
     query = r.recognize_google(audio,language='en-in')
     print(f"User said: {query}\n")
   except Exception as e:
       # print(e)
       print("Say that again please.....")
       return "None"
   return query
def sendEmail(content,to):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('200303105095@paruluniversity.ac.in','ParulSem3')
    server.sendmail('200303105095@paruluniversity.ac.in',to,content)
    server.close()

def read_pdf():
    book = open("D:\V. K. Mehta, Rohit Mehta - Principles of Electronics-S. Chand & Co Ltd (2008).pdf","rb")
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    speak(f"Total no of pages in this book is {pages}")
    speak("sir the content in the pdf is ")
    text = book.read()
    speak(text)



def sendWhatsapp(message,contact):
    if 'vivek' in contact:
       pywhatkit.sendwhatmsg("+917984564991","Hello Bro",6,46)
    elif 'yash' in contact:
        pywhatkit.sendwhatmsg('+917043749514', message, datetime.datetime.now())

def TasksExecution():
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif'read pdf'in query:
            read_pdf()
        elif 'open youtube' in query:
            speak("Starting Youtube..")
            webbrowser.open("https://www.youtube.com/")
        elif 'play song on youtube' in query:
            speak("Which song you want to play")
            mysong = takeCommand().lower()
            pywhatkit.playonyt(f"{mysong}")
        elif 'overflow' in query:
            webbrowser.open("https://stackoverflow.com/")
        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'open google' in query:
            # speak("What should is search on google?")
            # cm = takeCommand().lower()
            speak("Opening google..")
            # webbrowser.open(f"{cm}")
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        elif 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}\n")
        elif 'open vs code' in query:
            codePath = "C:\\Users\\ACER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Starting VS Code!")
            os.startfile(codePath)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "t0120cse434@paruluniversity.ac.in"
                sendEmail(content, to)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir I am not able to send email right now!")
        elif 'send whatsapp' in query:
            try:
                speak("To whom I send the whatsapp?")
                contact = takeCommand()
                speak("What should I say?")
                message = takeCommand()
                sendWhatsapp(message, contact)
                speak("Message sent!")
            except Exception as e:
                print(e)
                speak("Unable to send whatsapp right now!")
        elif'search'in query:
            speak("Yes sir tell me what to search?")
            search = takeCommand()
            result = webbrowser.open(f"https://www.google.com/search?q={search}")
            speak(result)
        elif 'open whatsapp' in query:
            speak("Opening Whatsapp Web...")
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open android studio' in query:
            speak("Starting Android Studio for you sir..")
            codepath1 = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(codepath1)
        elif 'open eclipse' in query:
            speak("Starting eclipse IDE for your JAVA work...")
            codepath2 = "C:\\Users\\ACER\\eclipse\\java-2020-12\\eclipse\\eclipse.exe"
            os.startfile(codepath2)
        elif 'open github' in query:
            speak("Starting git bash for U sir...")
            codepath3 = "C:\\Program Files (x86)\\Git\\git-bash.exe"
            os.startfile(codepath3)
        elif 'close github' in query:
            speak("Ok sir , closing git")
            os.system("taskkill /f /im git-bash.exe")
        elif 'open notepad' in query:
            speak("Opening for you")
            codepath4 = "%windir%\\system32\\notepad.exe"
            os.startfile(codepath4)
        elif 'how much power left'in query or 'how much power we have'in query or "battery"in query:
            battery = psutil.sensors_battery()
            persentage = battery.percent
            speak(f"sir our system have {persentage} percent battery")
        elif 'hello jarvis' in query:
            speak("hello sir ,may I help you with something")
        elif 'you can go now' in query:
            speak("Ok bye Sir !. You can call me anytime for help!")
            break
        elif 'leave' in query:
            speak("Ok sir as you wish,call me I am here for you")
            break
        elif'sleep'in query:
            speak("ok sir ,I am going to sleep you can call me anytime")
            break


name = "main"
if name == "main":
    while True:
        permission = takeCommand()
        if 'wake up'in permission:
            TasksExecution()
        elif 'goodbye'in permission:
            speak("Thanks for using me sir , have a good day!")
            sys.exit()
