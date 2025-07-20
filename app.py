import os
import google.generativeai as genai
from flask import Flask, render_template, request, session
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)
# Set the secret key from the .env file for session management
app.secret_key = os.getenv("SECRET_KEY")

# --- Configure the Google AI client ---
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-2.0-flash-lite') 
except Exception as e:
    print(f"Error configuring Google AI client: {e}")
    model = None

@app.route('/', methods=['GET', 'POST'])
def home():
    # On the first visit (GET request), initialize chat history in the session
    if 'chat_history' not in session:
        session['chat_history'] = []

    if request.method == 'POST' and model:
        # Get user input from the form
        input_text = request.form['text_input']
        
        # Add the user's message to the session history
        session['chat_history'].append({'role': 'user', 'text': input_text})
        
        try:
            # Start a chat session with the model using the existing history
            # The google-generativeai library handles the conversion of roles automatically
            chat_session = model.start_chat(
                history=[
                    {"role": "user" if msg['role'] == 'user' else "model", "parts": [msg['text']]}
                    for msg in session['chat_history'][:-1] # All history except the last user message
                ]
            )
            
            # Send the new message to the model
            response = chat_session.send_message(input_text)
            
            # Add the model's response to the session history
            session['chat_history'].append({'role': 'model', 'text': response.text})

        except Exception as e:
            # If an error occurs, add an error message to the chat
            error_message = f"An error occurred: {e}"
            session['chat_history'].append({'role': 'model', 'text': error_message})

        # Mark the session as modified to ensure it's saved
        session.modified = True
            
    # Always render the template with the current chat history
    return render_template('index.html', chat_history=session.get('chat_history', []))

if __name__ == '__main__':
    app.run(debug=True)