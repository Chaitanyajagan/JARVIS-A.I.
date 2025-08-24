import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime
import pyautogui
import os
import random
import webbrowser
from plyer import notification
from pygame import mixer
import getpass
import subprocess

def get_weather(city):
    api_key = 'api'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        return f"The current temperature in {city} is {temp}°C with {weather}."
    else:
        return "City not found or API error. Please check your API key and city name."

for i in range(3):
    a= getpass.getpass("Enter your password: ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [Hey jarvis] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,5)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "hey" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    speak("Thanks for spending time with me sir")
                    exit()
                elif "weather" in query or "temperature" in query:
                    speak("Please tell me the city name.")
                    city = takeCommand().lower()
                    if city != "none":
                        weather_info = get_weather(city)
                        print(weather_info)
                        speak(weather_info)
                    else:
                        speak("I couldn't understand the city name. Please try again.")
                        print("I couldn't understand the city name. Please try again.")
                elif "Take a break" in query:
                    speak("Taking a break for a while")
                    print("Taking a break for a while")
                    break
                elif "hello" in query:
                    speak("Hello sir how are you ?")
                    print("Hello sir how are you ?")
                elif "i am fine" in query:
                    speak("that's great sir")
                    print("that's great sir")
                elif "how are you" in query:
                    speak("Perfect sir")
                    print("Perfect sir")
                elif "thank you" in query:
                    speak("you are welcome sir")
                    print("you are welcome sir")
                elif "google" in query:
                    from SearchNow import searchGoogle
                    webbrowser.open(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "what's the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                    print(f"Sir, the time is {strTime}")
                elif "today's date" in query:
                    strDate=datetime.datetime.now().strftime("%D:%M:%Y")
                    speak(f"Sir, the date is {strDate}")
                    print(f"Sir, the date is {strDate}")
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to "+rememberMessage)
                    print("You told me to "+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())
                    print("You told me to remember that" + remember.read())
                elif "i am bored" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3,4,5,6,7)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=UVWB9UHpXzY&list=RDUVWB9UHpXzY&start_radio=1")
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=WGXmDsOwW4k")
                    elif b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=YAOIbHBEvi0")
                    elif b==4:
                        webbrowser.open("https://www.youtube.com/watch?v=AOIeoPwpe6Ekk")
                    elif b==5:
                        webbrowser.open("https://www.jiosaavn.com/s/mix/440_volts/asuy3quCOlMo6PRmoLWZhHq6h3oRogZ9u6M6sBP,gotoJbb0GXzVsKLRnrwqfEJetlQH4fAas94_")
                    elif b==6:
                        webbrowser.open("https://www.jiosaavn.com/s/mix/neeke_padipoyaa/asuy3quCOlMo6PRmoLWZhHq6h3oRogZ9u6M6sBP,gotoJbb0GXzVsFa-OHSbMsGYfmRyCHtHwAE_")
                    elif b==7:
                        webbrowser.open("https://www.jiosaavn.com/s/mix/joy_joy_gaa/asuy3quCOlMo6PRmoLWZhHq6h3oRogZ9u6M6sBP,gotoJbb0GXzVsK3FkrL1nHPGfmRyCHtHwAE_")
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no): ")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password: \n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")
                elif "schedule my day" in query:
                    tasks = []
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    print("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("music.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 5
                        )
                elif "open" in query:  
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                elif "cricket live score" in query:
                    from plyer import notification  
                    import requests 
                    from bs4 import BeautifulSoup 
                    url = "https://www.cricbuzz.com/cricket-match/live-scores"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 10
                    )
                elif "screenshot" in query:
                     import pyautogui 
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                
