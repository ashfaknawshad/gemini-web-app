# Gemini Retro Web App

A simple, retro-themed web chat application built with Python and Flask that connects to the Google Gemini API. This project serves as a basic template for integrating Google's generative AI into a web front-end.

![Demo Screenshot](https://i.imgur.com/example-image.png)
*(You can take a screenshot of your app and upload it to a site like imgur.com to add a preview here!)*

---

## Features

-   **Chat Interface:** A persistent chat that remembers conversation history for contextual responses.
-   **Retro Terminal Theme:** Styled with a pixelated font and a CRT monitor vibe.
-   **Dark/Light Mode:** Includes a toggle to switch between a light theme and a terminal-green dark theme.
-   **Flask Backend:** A lightweight Python server to handle API requests.

## Built With

-   [Flask](https://flask.palletsprojects.com/) - The web framework used.
-   [Google Gemini API](https://ai.google.dev/) - The generative AI model.
-   [Python-dotenv](https://github.com/theskumar/python-dotenv) - For managing environment variables.

---

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

You need to have Python 3 and pip installed on your system.
- [Python 3](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/gemini-retro-webapp.git
    cd gemini-retro-webapp
    ```

2.  **Install Python packages:**
    ```sh
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file first. See step 3.)*

3.  **Create a `requirements.txt` file:**
    To make installation easier for others, create this file by running:
    ```sh
    pip freeze > requirements.txt
    ```
    This will automatically list all the libraries your project needs.

4.  **Set up your Environment Variables:**
    Create a file named `.env` in the root of your project folder. You will need to get an API key from Google AI Studio.
    ```
    GOOGLE_API_KEY="YOUR_GEMINI_API_KEY_HERE"
    SECRET_KEY="ANY_RANDOM_STRING_FOR_FLASK_SESSION"
    ```

5.  **Run the application:**
    ```sh
    python app.py
    ```
    Open your web browser and go to `http://127.0.0.1:5000`.