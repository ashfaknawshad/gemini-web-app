import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    print("Successfully configured API key. Finding available models...")
    
    for m in genai.list_models():
      # Check if 'generateContent' is a supported method for the model
      if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")

except Exception as e:
    print(f"An error occurred: {e}")