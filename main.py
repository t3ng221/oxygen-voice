import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
oxygen = pyttsx3.init()
voices = oxygen.getProperty('voices')
oxygen.setProperty('voice', voices[1].id)


def talk(text):
    oxygen.say(text)
    oxygen.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'oxygen' in command:
                command = command.replace('oxygen', '')
    except:
        pass
    return command

def run_oxygen():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'what is your name' in command:
        talk('My name is Oxygen')
    elif 'how are you' in command:
        talk('I am fine  and you?')
    elif 'fine' in command:
        talk('What can i do for you?')
    elif 'capital of bangladesh' in command:
        talk('Capital of bangladesh is Dhaka')
    elif 'who are you' in command:
        talk('I am your personal voice assistant.')


    elif 'date' in command:
        date = datetime.datetime.now().strftime("%b-%d-%Y")
        print(date)
        talk('Today is' + date)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 3)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('I can search it for you. I am searching the web.')
        pywhatkit.search(command)

while True:

    run_oxygen()