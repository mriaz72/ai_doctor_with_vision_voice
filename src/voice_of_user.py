# setup audio recorder (ffmpeg & portaudio)
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout = 20, phrase_time_limit = None):
    """Simplified function to record audio using the microphone and save as mp3 file.
    
    Args:
    file_path (str):the path where the recorded audio will be saved.
    timeout (int): Maximum time to wait for a phrase to start (in seconds).
    phrase_time_limit (int): Maximum duration of a single phrase (in seconds).
    """
    recoganizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recoganizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking...")

            #record the audio
            audio_data = recoganizer.listen(source, timeout=timeout, 
                                            phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete, processing audio...")

            # Convert the audio data to an mp3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate = "128k")
            
            logging.info(f"Audio saved to {file_path}")
        
    except Exception as e:
        logging.error(f"An error occurred while recording audio: {e}")

#file_path = "user_voice.mp3"
#record_audio(file_path)

# setup speech to text model for transcribing the recorded audio
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
import os
stt_model = "whisper-large-v3"
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

def transcribe_audio_with_groq(stt_model, file_path, GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)


    audio_file=open(file_path, "rb")
    transcription=client.audio.transcriptions.create(
                                            model=stt_model,
                                            file=audio_file,
                                            language="en"
                                             )

    return transcription.text

#print(transcribe_audio_with_groq(stt_model, file_path, GROQ_API_KEY))



