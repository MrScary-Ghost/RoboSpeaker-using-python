import os

import pyttsx3
engine = pyttsx3.init()
try:
    if __name__ == '__main__':
        print("welcome to RoboSpeaker.... Developed by sougata ")
        while True:
            x= input("enter what you want me to speak : ")
            if x == ";":
                engine.say("bye bye friends hope you enjoyed using it ")
                engine.runAndWait()
                break
            engine.say(x)
            engine.runAndWait()
except Exception as d:
    print("there is a error occured",d)
