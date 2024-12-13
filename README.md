# **JARVIS - AI Voice based Assistant**

## **Project Overview**
Jarvis is an AI-powered voice assistant built in Python. It uses speech recognition to understand spoken commands and responds with appropriate actions through text-to-speech. The project aims to create a personalized assistant capable of handling various tasks through voice interaction.

## **Features**
- **Speech Recognition:** Converts spoken language into text using the `SpeechRecognition` library.
- **Command Processing:** Responds to user commands such as greetings, queries, and tasks.
- **Text-to-Speech (TTS):** Provides audio feedback using the `gtts` (Google Text-to-Speech) library.
- **Modular Design:** Easily extendable to add new features and commands.

## **Installation**
### **Prerequisites**
- Python 3.x
- `pip` (Python package installer)

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/manidixit51/JARVIS.git
   ```
2. Navigate to the project directory:
   ```bash
   cd jarvis
   ```
3. Create a virtual environment:
   ```bash
   python -m venv jarvis_env
   ```
4. Activate the virtual environment:
   - **Windows:** `.\jarvis_env\Scripts\activate`
   - **macOS/Linux:** `source jarvis_env/bin/activate`
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## **Usage**
1. Run the main script:
   ```bash
   python src/main.py
   ```
2. Speak into your microphone when prompted, and Jarvis will respond accordingly.

## **Project Structure**
```plaintext
├── src/
│   ├── main.py          # Entry point of the application
│   ├── speech_recognizer.py  # Handles speech recognition
│   ├── command_processor.py  # Processes recognized commands
│   ├── text_to_speech.py     # Handles text-to-speech conversion
├── tests/              # Unit tests
├── docs/               # Documentation
├── requirements.txt    # Project dependencies
└── README.md           # Project overview and setup instructions
```

## **Contributing**
Contributions are welcome! Please fork the repository and submit a pull request.

## **Acknowledgments**
- Inspiration from various AI assistants and Python open-source projects.
- Libraries used: `SpeechRecognition`, `gtts`, `playsound`, `PyAudio`.

---

