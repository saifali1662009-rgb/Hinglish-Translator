from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# Function to speak using gTTS
def speak(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    os.system("start output.mp3")   # For Windows
    # os.system("mpg123 output.mp3")  # For Linux
    # os.system("afplay output.mp3")  # For Mac

# Ask once for translation mode
print("Choose translation mode:")
print("1. English → Hinglish (Hindi in English letters)")
print("2. Hinglish → English")
choice = input("Enter choice (1 or 2): ")

while True:
    if choice == "1":
        text = input("\nEnter English text: ")
        if text.lower() == "exit":
            break
        translated = GoogleTranslator(source="en", target="hi").translate(text)
        print("Translated (Hinglish/Devanagari Hindi):", translated)
        speak(translated, lang="hi")  # Hindi speech

    elif choice == "2":
        text = input("\nEnter Hinglish text (in Hindi letters): ")
        if text.lower() == "exit":
            break
        translated = GoogleTranslator(source="hi", target="en").translate(text)
        print("Translated (English):", translated)
        speak(translated, lang="en")  # English speech

    else:
        print("Invalid choice!")
        break