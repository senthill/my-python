import cowsay
import pyttsx3


engine = pyttsx3.init()
this = input("What would you like to say? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()