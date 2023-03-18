
import speech_recognition as recognizer
import pyttsx3
import pywhatkit
import datetime
import wikipedia


def talk(text):
    speech_ai.say(text)

def input_instruction():
    try:
        with recognizer.Microphone() as origin:
            print("Listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            print(instruction)
            instruction = instruction.lower()
            print(instruction)

            if "Bestz" in instruction:
                instruction = instruction.replace('Bestz', '')
                print(instruction)
    except:
        pass
    return instruction

def run_bestz():
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace('play', '')
        talk(f"playing {song}")
        pywhatkit.playonyt(song)
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk(f'The Current time is {time}')
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk(f"Today's date is {date}")
    elif 'how are you' in instruction:
        talk(f'I am fine, and you?')
    elif 'what is your name' in instruction:
        talk('I am bestz, what can i do for you?')
    elif 'who is' in instruction:
        human = instruction.replace('who is', " ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)

    else:
        talk("Please I can't process that instruction yet")

if __name__=="__main__":

    while True: 
        listener = recognizer.Recognizer()
        speech_ai = pyttsx3.init()  
        run_bestz()
        speech_ai.runAndWait()