import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import datetime
import os

# Initialize the recognizer and the TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice command and recognize it
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}\n")
        except Exception as e:
            print("Sorry, I did not understand that. Can you please repeat?")
            return "None"
        return command.lower()

# Function to greet the user based on time of day
def greet_user():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your voice assistant. How can I help you today?")

# Core function to process commands and perform actions
def process_command(command):
    if "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    
    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}.")
    
    elif "search wikipedia" in command:
        speak("What do you want to search on Wikipedia?")
        query = take_command()
        if query != "None":
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(result)
    
    elif "play music" in command:
        music_dir = "C:/Users/YourMusicFolder"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    
    elif "stop" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that command.")

# Main function that runs the assistant
if __name__ == "__main__":
    greet_user()
    while True:
        user_command = take_command()
        if user_command != "None":
            process_command(user_command)
