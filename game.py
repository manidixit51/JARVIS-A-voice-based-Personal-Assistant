import pyttsx3
import speech_recognition as sr
import random

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 178)


# Function to make Jarvis speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Function to take voice commands
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again, please.")
        return "None"
    return query.lower()


# Game function
def game_play():
    speak("Let's play Rock Paper Scissors!")
    print("LET'S PLAY!")

    Me_score = 0
    Com_score = 0
    rounds = 5

    for i in range(rounds):
        speak("Your turn! Say rock, paper, or scissors.")
        choose = ("rock", "paper", "scissors")  # Tuple of options
        com_choose = random.choice(choose)  # Computer's random choice

        query = takeCommand()

        # Validate user input
        if query not in choose:
            speak("That's not a valid choice. Please say rock, paper, or scissors.")
            continue

        # Determine the result
        print(f"Computer chose: {com_choose}")
        if query == com_choose:
            speak(com_choose)
            print(f"Tie! Current Score - You: {Me_score} | Computer: {Com_score}")

        elif (query == "rock" and com_choose == "scissors") or \
                (query == "paper" and com_choose == "rock") or \
                (query == "scissors" and com_choose == "paper"):
            Me_score += 1
            speak(com_choose)
            print(f"You win this round! Current Score - You: {Me_score} | Computer: {Com_score}")

        else:
            Com_score += 1
            speak(com_choose)
            print(f"Computer wins this round! Current Score - You: {Me_score} | Computer: {Com_score}")

    # Announce the final score and winner
    print(f"FINAL SCORE - You: {Me_score} | Computer: {Com_score}")
    if Me_score > Com_score:
        speak("Congratulations! You won the game.")
    elif Me_score < Com_score:
        speak("Computer wins the game. Better luck next time!")
    else:
        speak("It's a tie game! Well played.")


# Run the game
if __name__ == "__main__":
    game_play()
