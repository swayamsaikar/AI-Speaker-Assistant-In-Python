# imported and used pyttsx3 module here
import pyttsx3

# Initialized the pyttsx3 module
engine = pyttsx3.init()

# get all the voices in the engine
voices = engine.getProperty('voices')

# print the voices array
# print(voices)

# This code will print the details of the Microsoft David (male voice)
# print(voices[0])

# This code will print the details of the Microsoft Zira (female voice)
# print(voices[1])

# we will be using the female voice here , so

# In this function(engine.setProperty()) we are setting value parameter as the female's voice id
engine.setProperty('voice',voices[1].id)

# defined a function which will take the user's input as an argument
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# put it inside a while loop to run endlessly
while True:
    # taken the user's input and stored it in userInput variable
    userInput = input('Enter something to speak! \n')

    # finally called the speak function and passed the userInput variable as an argument
    speak(userInput)

# This program will take some input and speak the entered text for you