# Oasis Infobyte Python Internship

A collection of Python projects completed during my **Oasis Infobyte Python Programming Internship**, focused on practical application development, GUI design, file handling, speech recognition, text-to-speech, and user input validation.

## 🚀 Projects

### 1. 🎙️ Voice Assistant

A Python voice assistant that captures microphone input, converts speech to text, processes commands, and responds using text-to-speech.

**Features**
- Speech recognition using Google Speech Recognition
- Text-to-speech responses with `pyttsx3`
- Voice-based time and date queries
- Web search from voice commands
- Opens Google and YouTube
- Basic conversational responses
- Graceful handling of unrecognized speech and service errors

**Technologies:** Python, SpeechRecognition, pyttsx3, sounddevice, SoundFile, NumPy

### 2. ⚖️ BMI Calculator

A desktop BMI calculator built with **Tkinter**, supporting both metric and imperial units and maintaining a local calculation history.

**Features**
- Metric and imperial unit support
- BMI calculation and health-category classification
- Input validation and error handling
- Color-coded results
- Health tips based on BMI category
- JSON-based history storage
- View and clear recent BMI records

**Technologies:** Python, Tkinter, JSON, File Handling

## 🧠 Skills Demonstrated

- Python application development
- Object-oriented programming
- GUI development with Tkinter
- Speech recognition and text-to-speech
- File and JSON handling
- Input validation and exception handling
- Working with external Python libraries
- Basic automation and browser integration

## 📂 Repository Structure

```text
oasis-infobyte-python/
├── bmi_calculator.py
├── voice_assistant.py
├── README.md
└── requirements.txt
```

## ⚙️ Setup

### Clone the repository

```bash
git clone https://github.com/tcnomithareddy28-cloud/oasis-infobyte-python.git
cd oasis-infobyte-python
```

### Install dependencies

For the Voice Assistant:

```bash
python -m pip install SpeechRecognition pyttsx3 sounddevice soundfile numpy
```

The BMI Calculator uses Tkinter, which is included with standard Python installations on most systems.

## ▶️ Run the Projects

**Voice Assistant**

```bash
python voice_assistant.py
```

**BMI Calculator**

```bash
python bmi_calculator.py
```

> The Voice Assistant requires a working microphone and internet access for Google speech recognition and web search functionality.

## 🎓 Internship Learning Outcomes

Through these projects, I strengthened my understanding of Python programming by building interactive applications rather than only working with isolated code exercises. The projects provided practical experience with GUI programming, APIs/services, audio input, persistent local data, and user-focused error handling.

## 👩‍💻 Author

**Nomitha Reddy**

Python Developer | AI & ML Enthusiast
