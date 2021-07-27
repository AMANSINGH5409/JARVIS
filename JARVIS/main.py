import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
  hour = int(datetime.datetime.now().hour)
  if hour >= 0 and hour < 12:
    speak("Good Morning!")
  elif hour >= 12 and hour < 18:
    speak("Good Afternoon!")
  else:
    speak("Good Evening!")

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

def sendWhatsapp(message,contact):
    if 'vivek' in contact:
       pywhatkit.sendwhatmsg("+917984564991","Hello Bro",6,46)
    elif 'yash' in contact:
        pywhatkit.sendwhatmsg('+917043749514', message, datetime.datetime.now())


name = "main"
if name == "main":
   wishMe()
   while True:
     query = takeCommand().lower()
    # logic for executing tasks based on query
     if'wikipedia' in query:
        speak("Searching Wikipedia....")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
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
            os.startfile(os.path.join(music_dir,songs[0]))
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
                sendEmail(content,to)
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
              sendWhatsapp(message,contact)
              speak("Message sent!")
            except Exception as e:
                print(e)
                speak("Unable to send whatsapp right now!")
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
     elif 'open git' in query:
            speak("Starting git bash for U sir...")
            codepath3 = "C:\\Program Files (x86)\\Git\\git-bash.exe"
            os.startfile(codepath3)
     elif 'close git'in query:
         speak("Ok sir , closing git")
         os.system("taskkill/f/in git-bash.exe")
     elif 'you can go now' in query:
         speak("Ok bye Sir !. You can call me anytime for help!")
         exit()
     elif 'leave' in query:
         speak("Ok sir as you wish,call me I am here for you")
         exit()