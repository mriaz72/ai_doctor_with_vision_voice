# setup api key
from dotenv import load_dotenv
load_dotenv()
import os
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

#convert image required format
import base64
image_path = "images/acne.jpg"

image_file = open(image_path, "rb")
encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

# setup multimodel llm
from groq import Groq
client = Groq(api_key=GROQ_API_KEY)
query = "What skin condition does this patient have?"
model = "meta-llama/llama-4-scout-17b-16e-instruct"
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
print(chat_completion.choices[0].message.content)