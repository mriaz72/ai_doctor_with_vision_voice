# voice bot UI with gradio
import os 
import gradio as gr

from src.brain_for_doctor import encoded_image, analyze_image_with_groq
from src.voice_of_user import record_audio, transcribe_audio_with_groq
from src.voice_of_doctor import text_to_speech_with_gtts_autoplay

system_prompt ="""You are a helpful and precise assistant for diagnosing skin conditions 
based on images and patient descriptions."""

def process_patient_input(audio_file, image_file):
    #Transcribe the audio input
    speech_to_text = transcribe_audio_with_groq(stt_model="whisper-large-v3",
                                                file_path=audio_file,
                                                GROQ_API_KEY=os.environ.get("GROQ_API_KEY"))
    
    # handle input image
    if image_file:
        doctor_response = analyze_image_with_groq(query=system_prompt+speech_to_text,
                                                  encoded_image=encoded_image(image_file),
                                                  model="meta-llama/llama-4-scout-17b-16e-instruct")
    else:
        doctor_response = "No image input provided. Please upload an image for diagnosis."

    voice_of_doctor = text_to_speech_with_gtts_autoplay(doctor_response, "doctor_response.mp3")
    return speech_to_text, doctor_response, voice_of_doctor

# Create Gradio User Interface
inface = gr.Interface(
    fn = process_patient_input,
    inputs = [
        gr.Audio(sources=["microphone"], type="filepath", label="Describe your symptoms and record your voice"),
        gr.Image(type="filepath", label="Upload an image of the affected area (optional)")
    ],
    outputs = [
        gr.Textbox(label="Transcribed Patient Description"),
        gr.Textbox(label="Doctor's Diagnosis"),
        gr.Audio("temp.mp3")
    ],
    title = "AI Doctor - Skin Condition Diagnosis",
    description = "Speak about your symptoms and optionally upload an image for diagnosis."

)

inface.launch(debug=True)
