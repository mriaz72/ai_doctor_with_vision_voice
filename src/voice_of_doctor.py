#setup text to speech model TTS(with gTTS)

import os
from gtts import gTTS

def text_to_speech_with_gtts(input_text, output_file):
    """Convert text to speech and save as an mp3 file.
    
    Args:
    text (str): The text to be converted to speech.
    output_file (str): The path where the generated audio will be saved.
    """
    language = 'en'
    audioobj = gTTS(text=input_text,
                    lang = language,
                    slow=False)
    audioobj.save(output_file)

#input_text = "Hello, I am Riaz, your virtual doctor. How can I assist you today?"
#text_to_speech_with_gtts(input_text, "doctor_voice.mp3")

#setup text to speech model TTS(with ElevenLabs)
import elevenlabs
from elevenlabs.client import ElevenLabs

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

def text_to_speech_with_elevenlabs(input_text, output_file):
    """Convert text to speech using ElevenLabs API and save as an mp3 file.
    
    Args:
    text (str): The text to be converted to speech.
    output_file (str): The path where the generated audio will be saved.
    """


    try:
        audio = elevenlabs.text_to_speech.convert(
            voice_id="NOpBlnGInO9m6vDvFkFC",
            text=input_text,
            model_id="eleven_v3",
            language_code="en",
            output_format="mp3_22050_32",
        )

        # `convert()` yields audio chunks; write them to the output file.
        with open(output_file, "wb") as f:
            for chunk in audio:
                f.write(chunk)
    except Exception as e:
        # EleventLabs raises an ApiError with status_code==402 for paid-voice access.
        if getattr(e, "status_code", None) == 402 or "payment_required" in str(e):
            print("ElevenLabs paid voice not available; falling back to gTTS.")
            text_to_speech_with_gtts(input_text, output_file)
        else:
            raise





#input_text = "Hello, I am Riaz, your virtual doctor. How can I assist you today?"
#text_to_speech_with_elevenlabs(input_text, "doctor_voice_elevenlabs.mp3")

# function to autoplay the generated audio file (cross-platform)

import platform
import subprocess

def text_to_speech_with_gtts_autoplay(input_text, output_file):
    """Convert text to speech and save as an mp3 file.
    
    Args:
    text (str): The text to be converted to speech.
    output_file (str): The path where the generated audio will be saved.
    """
    language = 'en'
    audioobj = gTTS(text=input_text,
                    lang = language,
                    slow=False)
    audioobj.save(output_file)

    # Autoplay the generated audio file
    system = platform.system()
    if system == "Windows":
        subprocess.run(["start", output_file], shell=True)
    elif system == "Darwin":  # macOS
        subprocess.run(["open", output_file])
    else:  # Linux
        subprocess.run(["xdg-open", output_file])

#input_text = "Hello, I am Riaz, your virtual doctor. How can I assist you today?"
#text_to_speech_with_gtts_autoplay(input_text, "doctor_voice_autoplay2.mp3")