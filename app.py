import os
import google.generativeai as genai
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# --- Configure the Google AI client ---
try:
    # Use the GOOGLE_API_KEY from the .env file
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # --- THIS IS THE FINAL CORRECTED LINE ---
    # Create the model instance using a model available to you
    model = genai.GenerativeModel('gemini-1.5-flash') 

except Exception as e:
    print(f"Error configuring Google AI client: {e}")
    model = None

@app.route('/', methods=['GET', 'POST'])
def home():
    generated_text = None
    if request.method == 'POST' and model:
        # Get the text from the form
        input_text = request.form['text_input']
        
        try:
            # Generate content with Gemini
            response = model.generate_content(input_text)
            generated_text = response.text
        except Exception as e:
            generated_text = f"An error occurred with the Google API: {e}"

    return render_template('index.html', generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)