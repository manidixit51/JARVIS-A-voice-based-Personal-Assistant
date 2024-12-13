#
# import tkinter as tk
# import threading
# from itertools import cycle
# import speech_recognition as sr
# import os
# import webbrowser
# import datetime
# import pyjokes
# import wikipedia
# import re
# import pyautogui
# import time
#
# # Initialize Tkinter window for GUI
# root = tk.Tk()
# root.title("Jarvis Assistant")
# root.geometry("700x800")  # Adjusted to a smaller size for easier handling
# root.config(bg="black")
#
# # Canvas for animation
# canvas = tk.Canvas(root, width=300, height=300, bg="black", highlightthickness=0)
# canvas.pack(pady=20)
#
# # Animated circle that will pulse and change colors
# circle = canvas.create_oval(50, 50, 250, 250, fill="#4a90e2", outline="")
#
# # Label to display Jarvis's response
# response_label = tk.Label(root, text="Welcome! I'm Jarvis.", font=("Helvetica", 14), fg="white", bg="black", wraplength=300)
# response_label.pack(pady=20)
#
# # Function to create a "pulsing" and color-changing effect
# def animate_circle():
#     colors = cycle(["#FF5733", "#33FF57", "#3357FF", "#F333FF", "#33FFF3", "#FFC300"])
#     size_cycle = cycle([0, 10, 20, 10, 0])  # To make the circle "pulse"
#
#     while True:
#         color = next(colors)
#         size_change = next(size_cycle)
#         # Update color and size for the pulse effect
#         canvas.itemconfig(circle, fill=color)
#         canvas.coords(circle, 50 - size_change, 50 - size_change, 250 + size_change, 250 + size_change)
#         time.sleep(0.5)
#
# # Function to update text response in the GUI
# def display_response(text):
#     response_label.config(text=text)
#     root.update_idletasks()
#
# def say(text):
#     display_response(text)
#     os.system(f"say {text}")
#
# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.pause_threshold = 0.6
#         display_response("Listening...")
#         audio = r.listen(source)
#         try:
#             query = r.recognize_google(audio, language="en-in")
#             display_response(f"You said: {query}")
#             return query.lower()
#         except Exception:
#             display_response("Sorry, I didn't catch that.")
#             return None
#
# def search_wikipedia(query):
#     try:
#         results = wikipedia.summary(query, sentences=2)
#         say(f"According to Wikipedia, {results}")
#     except wikipedia.exceptions.DisambiguationError:
#         say("The topic is ambiguous, please be more specific.")
#     except wikipedia.exceptions.PageError:
#         say("Sorry, I couldn't find any results for your search.")
#     except Exception as e:
#         say(f"An error occurred: {e}")
#
# def open_wikipedia_page(query):
#     url = f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
#     webbrowser.open(url)
#     say(f"Opening the Wikipedia page for {query}.")
#
# def handle_wikipedia_query(query):
#     say("What would you like to search on Wikipedia?")
#     search_query = takeCommand()
#     if search_query:
#         if "search on wikipedia" in query:
#             open_wikipedia_page(search_query)
#         else:
#             search_wikipedia(search_query)
#     else:
#         say("Sorry, I couldn't understand what you wanted to search.")
#
# # Music playlist
# playlist = {
#     "shape of you": "/Users/purva/Documents/Gallery/music/ed_sheeran_shape_of_you_lyrics_mp3_42542.mp3",
#     "photograph": "/Users/purva/Documents/Gallery/music/ed_sheeran_photograph_lyrics_mp3_42449.mp3",
#     "let me down slowly": "/Users/purva/Documents/Gallery/music/alec_benjamin_let_me_down_slowly_lyrics_mp3_42666.mp3"
# }
#
# def play_music(song_name):
#     if song_name in playlist:
#         music_path = playlist[song_name]
#         os.system(f"open {music_path}")
#         say(f"Playing {song_name}. Enjoy your music!")
#     else:
#         say(f"Sorry, I could not find {song_name} in your playlist.")
#
# sites = [
#     ["youtube", "https://www.youtube.com"],
#     ["wikipedia", "https://www.wikipedia.org"],
#     ["google", "https://www.google.com"]
# ]
#
# def process_command():
#     query = takeCommand()
#     if query:
#         # Handle opening specific websites
#         for site in sites:
#             if f"open {site[0]}" in query:
#                 say(f"Okay, I am opening {site[0]}...")
#                 webbrowser.open(site[1])
#                 return
#
#         if "time" in query:
#             current_time = datetime.datetime.now().strftime("%I:%M %p")
#             say(f"The time is {current_time}")
#         elif "joke" in query:
#             joke = pyjokes.get_joke()
#             say(joke)
#         elif "play music" in query:
#             say("Which song would you like to play?")
#             song_query = takeCommand()
#             if song_query:
#                 play_music(song_query)
#         elif "find my phone" in query:
#             say("Opening Find My Device. Please log in to make your phone ring.")
#             webbrowser.open("https://www.google.com/android/find")
#         elif "screenshot" in query:
#             try:
#                 screenshot_path = f"ss_{time.strftime('%Y%m%d-%H%M%S')}.png"
#                 pyautogui.screenshot().save(screenshot_path)
#                 say("Screenshot taken and saved successfully.")
#             except Exception:
#                 say("An error occurred while taking the screenshot.")
#         elif "who is" in query or "search on wikipedia" in query:
#             handle_wikipedia_query(query)
#         elif "thank you" in query:
#             say("You're welcome! I'm here to help you!")
#
#         elif "exit" in query or "stop" in query:
#             say("Goodbye! Have a great day!")
#             root.quit()  # This closes the Tkinter GUI and exits the program
#             return  # Exit the function
#
#         else:
#             say("I'm not sure how to help with that.")
#
# # Personalized greeting function
# def personalized_greeting():
#     hour = datetime.datetime.now().hour
#     greeting = "Good morning" if hour < 12 else "Good afternoon" if hour < 18 else "Good evening"
#     say(f"{greeting}! I am Jarvis. How can I assist you today?")
#
# # Main function to handle commands
# def main():
#     personalized_greeting()
#     while True:
#         process_command()
#
# # Run animation and command-processing in separate threads
# animation_thread = threading.Thread(target=animate_circle, daemon=True)
# animation_thread.start()
#
# command_thread = threading.Thread(target=main, daemon=True)
# command_thread.start()
#
# root.mainloop()


#
# import tkinter as tk
# import threading  #to multiple funtions
# from curses.textpad import rectangle
# from itertools import cycle
# import speech_recognition as sr
# import os
# import webbrowser
# import datetime
# import pyjokes
# import wikipedia
# import re       #Text pattern matching in future commands.
# import pyautogui   #use to take a SS
# import time
# import random
#
# # Initialize Tkinter window for GUI
# root = tk.Tk()
# root.title("Jarvis Assistant")
# root.geometry("700x800")  # Adjusted to a smaller size for easier handling
# root.config(bg="black")
#
# # Canvas for animation
# canvas = tk.Canvas(root, width=300, height=300, bg="black", highlightthickness=0)
# canvas.pack(pady=20)
#
# # Animated circle that will pulse and change colors
# circle = canvas.create_oval(100, 1000, 250, 250, fill="#4a90e2", outline="")
#
# # Label to display Jarvis's response
# response_label = tk.Label(root, text="Welcome! I'm Jarvis.", font=("Helvetica", 14), fg="white", bg="black", wraplength=300)
# response_label.pack(pady=20)
#
# # Function to create a "pulsing" and color-changing effect
# def animate_circle():
#     colors = cycle(["#FF5733", "#33FF57", "#3357FF", "#F333FF", "#33FFF3", "#FFC300"])
#     size_cycle = cycle([20, 20, 20, 10])  # To make the circle "pulse"
#
#     while True:
#         color = next(colors)
#         size_change = next(size_cycle)
#         # Update color and size for the pulse effect
#         canvas.itemconfig(rectangle(), fill=color)
#         canvas.coords(rectangle(), 50 - size_change, 50 - size_change, 250 + size_change, 250 + size_change)
#         time.sleep(0.5)
#
# # Function to update text response in the GUI
# def display_response(text):
#     response_label.config(text=text)
#     root.update_idletasks()
#
# def say(text):
#     display_response(text)
#     os.system(f"say {text}")
#
# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.pause_threshold = 0.6
#         display_response("Listening...")
#         audio = r.listen(source)
#         try:
#             query = r.recognize_google(audio, language="en-in")
#             display_response(f"You said: {query}")
#             return query.lower()
#         except Exception:
#             display_response("Sorry, I didn't catch that.")
#             return None
#
# def search_wikipedia(query):
#     try:
#         results = wikipedia.summary(query, sentences=2)
#         say(f"According to Wikipedia, {results}")
#     except wikipedia.exceptions.DisambiguationError:
#         say("The topic is ambiguous, please be more specific.")
#     except wikipedia.exceptions.PageError:
#         say("Sorry, I couldn't find any results for your search.")
#     except Exception as e:
#         say(f"An error occurred: {e}")
#
# def open_wikipedia_page(query):
#     url = f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
#     webbrowser.open(url)
#     say(f"Opening the Wikipedia page for {query}.")
#
# def handle_wikipedia_query(query):
#     say("What would you like to search on Wikipedia?")
#     search_query = takeCommand()
#     if search_query:
#         if "search on wikipedia" in query:
#             open_wikipedia_page(search_query)
#         else:
#             search_wikipedia(search_query)
#     else:
#         say("Sorry, I couldn't understand what you wanted to search.")
#
# # Music playlist
# playlist = {
#     "shape of you": "/Users/purva/Documents/Gallery/music/ed_sheeran_shape_of_you_lyrics_mp3_42542.mp3",
#     "photograph": "/Users/purva/Documents/Gallery/music/ed_sheeran_photograph_lyrics_mp3_42449.mp3",
#     "let me down slowly": "/Users/purva/Documents/Gallery/music/alec_benjamin_let_me_down_slowly_lyrics_mp3_42666.mp3"
# }
#
# def play_music(song_name):
#     if song_name in playlist:
#         music_path = playlist[song_name]
#         os.system(f"open {music_path}")
#         say(f"Playing {song_name}. Enjoy your music!")
#     else:
#         say(f"Sorry, I could not find {song_name} in your playlist.")
#
# sites = [
#     ["youtube", "https://www.youtube.com"],
#     ["wikipedia", "https://www.wikipedia.org"],
#     ["google", "https://www.google.com"]
# ]
#
# def play_game():
#     say("Let's play a number guessing game! I have selected a number between 1 and 10. Try to guess it.")
#     number_to_guess = random.randint(1, 10)
#     attempts = 3  # Limit attempts to 3 guesses
#
#     for attempt in range(attempts):
#         say(f"You have {attempts - attempt} attempts left. What's your guess?")
#
import tkinter as tk
import threading
from itertools import cycle
import speech_recognition as sr
import os
import webbrowser
import datetime
import pyjokes
import wikipedia
import re
import pyautogui
import time
import random

# Initialize Tkinter window for GUI
root = tk.Tk()
root.title("Jarvis Assistant")
root.geometry("700x800")  # Adjusted to a smaller size for easier handling
root.config(bg="black")

# Canvas for animation
canvas = tk.Canvas(root, width=300, height=300, bg="black", highlightthickness=0)
canvas.pack(pady=20)

# Animated circle that will pulse and change colors
circle = canvas.create_oval(50, 50, 250, 250, fill="#4a90e2", outline="")

# Label to display Jarvis's response
response_label = tk.Label(root, text="Welcome! I'm Jarvis.", font=("Helvetica", 14), fg="white", bg="black", wraplength=300)
response_label.pack(pady=20)

# Function to create a "pulsing" and color-changing effect
def animate_circle():
    colors = cycle(["#FF5733", "#33FF57", "#3357FF", "#F333FF", "#33FFF3", "#FFC300"])
    size_cycle = cycle([0, 10, 20, 10, 0])  # To make the circle "pulse"

    while True:
        color = next(colors)
        size_change = next(size_cycle)
        # Update color and size for the pulse effect
        canvas.itemconfig(circle, fill=color)
        canvas.coords(circle, 50 - size_change, 50 - size_change, 250 + size_change, 250 + size_change)
        time.sleep(0.5)

# Function to update text response in the GUI
def display_response(text):
    response_label.config(text=text)
    root.update_idletasks()

def say(text):
    display_response(text)
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        display_response("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            display_response(f"You said: {query}")
            return query.lower()
        except Exception:
            display_response("Sorry, I didn't catch that.")
            return None

def search_wikipedia(query):
    try:
        results = wikipedia.summary(query, sentences=2)
        say(f"According to Wikipedia, {results}")
    except wikipedia.exceptions.DisambiguationError:
        say("The topic is ambiguous, please be more specific.")
    except wikipedia.exceptions.PageError:
        say("Sorry, I couldn't find any results for your search.")
    except Exception as e:
        say(f"An error occurred: {e}")

def open_wikipedia_page(query):
    url = f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
    webbrowser.open(url)
    say(f"Opening the Wikipedia page for {query}.")

def handle_wikipedia_query(query):
    say("What would you like to search on Wikipedia?")
    search_query = takeCommand()
    if search_query:
        if "search on wikipedia" in query:
            open_wikipedia_page(search_query)
        else:
            search_wikipedia(search_query)
    else:
        say("Sorry, I couldn't understand what you wanted to search.")

# Music playlist
playlist = {
    "shape of you": "/Users/purva/Documents/Gallery/music/ed_sheeran_shape_of_you_lyrics_mp3_42542.mp3",
    "photograph": "/Users/purva/Documents/Gallery/music/ed_sheeran_photograph_lyrics_mp3_42449.mp3",
    "let me down slowly": "/Users/purva/Documents/Gallery/music/alec_benjamin_let_me_down_slowly_lyrics_mp3_42666.mp3"
}

def play_music(song_name):
    if song_name in playlist:
        music_path = playlist[song_name]
        os.system(f"open {music_path}")
        say(f"Playing {song_name}. Enjoy your music!")
    else:
        say(f"Sorry, I could not find {song_name} in your playlist.")

sites = [
    ["youtube", "https://www.youtube.com"],
    ["wikipedia", "https://www.wikipedia.org"],
    ["google", "https://www.google.com"]
]

def play_game():
    say("Let's play a number guessing game! I have selected a number between 1 and 10. Try to guess it.")
    number_to_guess = random.randint(1, 10)
    attempts = 3  # Limit attempts to 3 guesses

    for attempt in range(attempts):
        say(f"You have {attempts - attempt} attempts left. What's your guess?")
        guess = takeCommand()

        if not guess:
            say("I didn't hear your guess. Please try again.")
            continue

        if not guess.isdigit():
            say("Please guess a number between 1 and 10.")
            continue

        guess = int(guess)
        if guess == number_to_guess:
            say("Congratulations! You guessed it correctly!")
            return
        elif guess < number_to_guess:
            say("The number is higher.")
        else:
            say("The number is lower.")

    say(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}. Better luck next time!")

def process_command():
    query = takeCommand()
    if query:
        # Handle opening specific websites
        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Okay, I am opening {site[0]}...")
                webbrowser.open(site[1])
                return

        if "time" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            say(f"The time is {current_time}")
        elif "joke" in query:
            joke = pyjokes.get_joke()
            say(joke)
        elif "play music" in query:
            say("Which song would you like to play?")
            song_query = takeCommand()
            if song_query:
                play_music(song_query)
        elif "find my phone" in query:
            say("Opening Find My Device. Please log in to make your phone ring.")
            webbrowser.open("https://www.google.com/android/find")
        elif "screenshot" in query:
            try:
                screenshot_path = f"ss_{time.strftime('%Y%m%d-%H%M%S')}.png"
                pyautogui.screenshot().save(screenshot_path)
                say("Screenshot taken and saved successfully.")
            except Exception:
                say("An error occurred while taking the screenshot.")
        elif "who is" in query or "search on wikipedia" in query:
            handle_wikipedia_query(query)
        elif "play game" in query or "game" in query:
            play_game()
        elif "thank you" in query:
            say("You're welcome! I'm here to help you!")
        elif "exit" in query or "stop" in query:
            say("Goodbye! Have a great day!")
            root.quit()  # This closes the Tkinter GUI and exits the program
            return
        else:
            say("I'm not sure how to help with that.")

# Personalized greeting function
def personalized_greeting():
    hour = datetime.datetime.now().hour
    greeting = "Good morning" if hour < 12 else "Good afternoon" if hour < 18 else "Good evening"
    say(f"{greeting}! I am Jarvis. How can I assist you today?")

# Main function to handle commands
def main():
    personalized_greeting()
    while True:
        process_command()

# Run animation and command-processing in separate threads
animation_thread = threading.Thread(target=animate_circle, daemon=True)
animation_thread.start()

command_thread = threading.Thread(target=main, daemon=True)
command_thread.start()

root.mainloop()
