# setup api key
from dotenv import load_dotenv
load_dotenv()
import os
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

#convert image required format
import base64
#image_path = "images/acne.jpg"
def encoded_image(image_path):
    image_file = open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode("utf-8")

#image_path = "images/acne.jpg"
#encoded_image_str = encoded_image(image_path)

# setup multimodel llm
from groq import Groq
client = Groq(api_key=GROQ_API_KEY)

query = "What skin condition does this patient have?"
model = "meta-llama/llama-4-scout-17b-16e-instruct"

def analyze_image_with_groq(query, encoded_image, model):
    message = [
        {
            "role":"user",
            "content":[
                {
                    "type":"text",
                    "text":query
                },
                {
                    "type":"image_url",
                    "image_url":{
                        "url":f"data:image/jpeg;base64,{encoded_image}"
                    }
                }
            ]
        }
    ]
    chat_completion = client.chat.completions.create(
        model=model, 
        messages=message)
    return chat_completion.choices[0].message.content

#print(analyze_image_with_groq(query, encoded_image_str, model))