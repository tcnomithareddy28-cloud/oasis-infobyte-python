"""
Voice Assistant - Oasis Infobyte Python Internship
Project 1: Voice Assistant

NO pyaudio needed! Uses sounddevice instead.

Install with ONE command:
    python -m pip install SpeechRecognition pyttsx3 sounddevice soundfile numpy

Run:
    python voice_assistant.py
"""

import datetime
import webbrowser
import sys
import io

import pyttsx3
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import soundfile as sf


# ── TTS Engine ────────────────────────────────────────────────────────────────
engine = pyttsx3.init()
engine.setProperty("rate", 155)
engine.setProperty("volume", 1.0)
voices = engine.getProperty("voices")
if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)


def speak(text: str) -> None:
    print(f"\n🤖 Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


# ── Mic recording (sounddevice — no pyaudio needed) ───────────────────────────
SAMPLE_RATE = 16000
RECORD_SECONDS = 6


def record_audio() -> bytes:
    """Record from mic and return WAV bytes."""
    print("\n🎤 Listening... (speak now)")
    recording = sd.rec(
        int(RECORD_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )
    sd.wait()
    buf = io.BytesIO()
    sf.write(buf, recording, SAMPLE_RATE, format="WAV", subtype="PCM_16")
    buf.seek(0)
    return buf.read()


def listen() -> str:
    """Record voice and return recognized text in lowercase."""
    recognizer = sr.Recognizer()
    try:
        wav_data = record_audio()
        audio = sr.AudioData(wav_data, SAMPLE_RATE, 2)
        command = recognizer.recognize_google(audio)
        print(f"👤 You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please try again.")
        return ""
    except sr.RequestError:
        speak("Speech service unavailable. Check your internet.")
        return ""
    except Exception as e:
        print(f"[Error] {e}")
        return ""


# ── Helpers ───────────────────────────────────────────────────────────────────
def get_time() -> str:
    return datetime.datetime.now().strftime("It is %I:%M %p")


def get_date() -> str:
    return datetime.date.today().strftime("Today is %A, %B %d, %Y")


def search_web(query: str) -> None:
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(url)
    speak(f"Here are the search results for: {query}")


# ── Command processor ─────────────────────────────────────────────────────────
def process_command(command: str) -> bool:
    if not command:
        return True

    if any(w in command for w in ["hello", "hi", "hey", "howdy"]):
        speak("Hello! I'm your voice assistant. How can I help you?")

    elif any(p in command for p in ["what time", "current time", "tell me the time"]):
        speak(get_time())

    elif any(p in command for p in ["what date", "today's date", "what day", "current date"]):
        speak(get_date())

    elif "time and date" in command or "date and time" in command:
        speak(get_time() + ". And " + get_date())

    elif any(p in command for p in ["who are you", "your name", "what are you"]):
        speak("I am your personal voice assistant, built with Python for Oasis Infobyte!")

    elif "how are you" in command:
        speak("I'm doing great, thank you for asking!")

    elif any(w in command for w in ["thank you", "thanks"]):
        speak("You're welcome! Anything else?")

    elif "help" in command or "what can you do" in command:
        speak(
            "I can tell you the time, the date, "
            "search the web, open YouTube or Google, "
            "and have a basic conversation. "
            "Say search for followed by your topic to search the web."
        )

    elif any(kw in command for kw in ["search for", "look up", "search"]):
        query = ""
        for kw in ["search for", "look up", "search"]:
            if kw in command:
                query = command.split(kw, 1)[-1].strip()
                break
        if query:
            search_web(query)
        else:
            speak("What would you like me to search for?")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")

    elif any(w in command for w in ["exit", "quit", "bye", "goodbye", "stop"]):
        speak("Goodbye! Have a great day!")
        return False

    else:
        speak(f"I heard: {command}. I'm not sure about that. Say help for options.")

    return True


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("=" * 52)
    print("   🎙️  VOICE ASSISTANT  |  Oasis Infobyte")
    print("=" * 52)
    print("Say: time, date, search for <topic>,")
    print("     open youtube, open google, help, exit\n")

    speak("Hello! I'm your voice assistant. Say help to hear what I can do.")

    running = True
    while running:
        command = listen()
        running = process_command(command)

    sys.exit(0)


if __name__ == "__main__":
    main()
