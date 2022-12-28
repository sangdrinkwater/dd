import speech_recognition as sr
import wikipedia
wikipedia.set_lang('en')
language = 'en'
recognizer = sr.Recognizer()
from gtts import gTTS
import os

# ''' recording the sound '''
# from gtts import gTTS
# import os
# mytext = "ultr"
# audio = gTTS(text=mytext, lang="en", slow=False)
# audio.save("example.mp3")
# os.system("start example.mp3")

class Users:
    def setName():
        # Voice recognition user's name
        with sr.Microphone() as source:
            print("Adjusting noise ")
            recognizer.adjust_for_ambient_noise(source, duration = 1)
            print("What is your name?")
            recorded_audio = recognizer.listen(source, timeout = 110)
            print("Done recording")

        ''' Recognizing the Audio '''
        try:
            # print("Recognizing the text")
            name = recognizer.recognize_google(
                    recorded_audio, 
                    language="en"
                )
            print("Your name is {}".format(name))
            f = open("C:\\Users\\kenny\\Downloads\\cs3310_AI-main\\cs3310_AI-main\\AI folder\\master\\name.txt", "w")
            f.write(name)
            f.close()

        except Exception as ex:
            print(ex)
            
            
    def setAge():
        # Voice recognition user's age 
        with sr.Microphone() as source:
            print("Adjusting noise ")
            recognizer.adjust_for_ambient_noise(source, duration = 1)
            print("How old are you?")
            recorded_audio = recognizer.listen(source, timeout = 110)
            print("Done recording")

        ''' Recognizing the Audio '''
        try:
            # print("Recognizing the text")
            age = recognizer.recognize_google(
                    recorded_audio, 
                    language="en"
                )
            print("You are {} year(s) old".format(age))
            f = open("C:\\Users\\kenny\\Downloads\\cs3310_AI-main\\cs3310_AI-main\\AI folder\\master\\age.txt", "w")
            f.write(age)
            f.close()

        except Exception as ex:
            print(ex)
    def setWeight():
        # Voice recognition user's weight    
        with sr.Microphone() as source:
            print("Adjusting noise ")
            recognizer.adjust_for_ambient_noise(source, duration = 1)
            print("What is your weight? (in kilograms)")
            recorded_audio = recognizer.listen(source, timeout = 110)
            print("Done recording")

        ''' Recognizing the Audio '''
        try:
            # print("Recognizing the text")
            weight = recognizer.recognize_google(
                    recorded_audio, 
                    language="en"
                )
            print("You are {} kg(s)".format(weight))
            f = open("C:\\Users\\kenny\\Downloads\\cs3310_AI-main\\cs3310_AI-main\\AI folder\\master\\weight.txt", "w")
            f.write(weight)
            f.close()

        except Exception as ex:
            print(ex)
            
    def setHeight():
        # Voice recognition user's height    
        with sr.Microphone() as source:
            print("Adjusting noise ")
            recognizer.adjust_for_ambient_noise(source, duration = 1)
            print("What is your height? (in centimeters)")
            recorded_audio = recognizer.listen(source, timeout = 110)
            print("Done recording")

        ''' Recognizing the Audio '''
        try:
            # print("Recognizing the text")
            height = recognizer.recognize_google(
                    recorded_audio, 
                    language="en"
                )
            print("You are {} cm(s)".format(height))
            f = open("C:\\Users\\kenny\\Downloads\\cs3310_AI-main\\cs3310_AI-main\\AI folder\\master\\height.txt", "w")
            f.write(height)
            f.close()

        except Exception as ex:
            print(ex)
    def setGender():
        # Voice recognition user's gender   
        with sr.Microphone() as source:
            print("Adjusting noise ")
            recognizer.adjust_for_ambient_noise(source, duration = 1)
            print("What is your gender?")
            recorded_audio = recognizer.listen(source, timeout = 110)
            print("Done recording")

        ''' Recognizing the Audio '''
        try:
            # print("Recognizing the text")
            gender = recognizer.recognize_google(
                    recorded_audio, 
                    language="en"
                )
            print("You are {}".format(gender))
            f = open("C:\\Users\\kenny\\Downloads\\cs3310_AI-main\\cs3310_AI-main\\AI folder\\master\\gender.txt", "w")
            f.write(gender)
            f.close()

        except Exception as ex:
            print(ex)

    def setHobby():
        # Voice recognition user's hobby    
        with sr.Microphone() as source:
            print("Adjusting noise ")
            recognizer.adjust_for_ambient_noise(source, duration = 1)
            print("What food do you like?\n(Eg: meat, beef, egg,..)")
            recorded_audio = recognizer.listen(source, timeout = 110)
            print("Done recording")

        ''' Recognizing the Audio '''
        try:
            # print("Recognizing the text")
            hobby = recognizer.recognize_google(
                    recorded_audio, 
                    language="en"
                )
            print("You likes {}".format(hobby))
            f = open("C:\\Users\\kenny\\Downloads\\cs3310_AI-main\\cs3310_AI-main\\AI folder\\master\\hobby.txt", "a")
            f.write(hobby)
            f.write("\n")
            f.close()

        except Exception as ex:
            print(ex)
            
    def setChoice():
        # Voice recognition user's hobby    
        with sr.Microphone() as source:
            print("Adjusting noise ")
            recognizer.adjust_for_ambient_noise(source, duration = 1)
            print("Anything else? (yes/no)")
            recorded_audio = recognizer.listen(source, timeout = 7)
            print("Done recording")

        ''' Recognizing the Audio '''
        try:
            # print("Recognizing the text")
            choice = recognizer.recognize_google(
                    recorded_audio, 
                    language="en"
                )
            print(choice)
            return choice

        except Exception as ex:
            print(ex)
        