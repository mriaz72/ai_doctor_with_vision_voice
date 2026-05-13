# AI Doctor 2.0

> A voice-first, image-aware medical assistant for skin-condition triage built with Gradio, Groq, and Python.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-Interface-F97316?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-AI-111827?style=for-the-badge)

## What It Does

AI Doctor 2.0 lets a user describe symptoms by voice, optionally upload an image of the affected area, and receive:

- a transcription of the spoken description
- an AI-generated diagnosis-style response
- an audio reply that speaks the result back

It is designed as a fast, approachable demo for multimodal healthcare workflows.

## Features

- Voice input through the microphone
- Image upload for visual analysis
- Transcription powered by Groq Whisper
- Vision reasoning through a Groq-hosted LLM
- Text-to-speech response for a more natural interaction loop
- Simple Gradio UI for quick local launch

## Preview

If you have a sample image such as [images/acne.jpg](images/acne.jpg), you can use it to test the app locally.

## Project Structure

- [main.py](main.py) - simple entry point
- [gradio_app.py](gradio_app.py) - main Gradio application
- [src/brain_for_doctor.py](src/brain_for_doctor.py) - image analysis helpers
- [src/voice_of_user.py](src/voice_of_user.py) - speech-to-text helpers
- [src/voice_of_doctor.py](src/voice_of_doctor.py) - text-to-speech helpers

## Requirements

- Python 3.10 or newer
- A valid `GROQ_API_KEY`
- Microphone access for voice input
- Optional: a webcam or local image file to test image analysis

## Installation

```bash
git clone <your-repo-url>
cd ai_doctor_2.0
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

If you use PowerShell and the virtual environment activation script is blocked, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

## Configuration

Set your Groq API key before launching the app:

```powershell
$env:GROQ_API_KEY = "your_groq_api_key"
```

For a persistent setup, add the variable to your system environment or a local `.env` workflow if you prefer.

## Run the App

```bash
python gradio_app.py
```

The Gradio interface will open in your browser. Speak your symptoms, upload an image if available, and wait for the diagnosis-style response.

## How It Works

1. The user records a short voice description.
2. The app transcribes speech into text.
3. If an image is provided, the image and transcript are sent to the analysis model.
4. The model returns a response tailored to the symptom description and visual input.
5. The response is converted into speech and played back in the interface.

## Notes

- This project is a prototype and should not be used as a substitute for professional medical advice.
- The quality of the output depends on the clarity of the image, the audio input, and the model response.
- For best results, use a well-lit image and a short, clear symptom description.

## Future Improvements

- Add a proper patient-history form
- Support chat-style follow-up questions
- Improve the UI with richer layouts and visual feedback
- Add caching and error handling for network/API failures
- Include example prompts and sample outputs in the README

## License

No license file is currently included. Add one before publishing the repository publicly.
