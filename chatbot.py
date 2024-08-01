import re
import google.generativeai as genai
import pyttsx3
import cv2
import requests
from datetime import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Configure the Google Generative AI
genai.configure(api_key="Geminiai_api")

# Define the generation configuration and safety settings
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 512,
    "response_mime_type": "text/plain",
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

# Create the generative model instance
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
)

# Start a chat session with the model
chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": ["hello"],
        },
        {
            "role": "model",
            "parts": ["Hello! What can I do for you today?"],
        },
    ]
)

# Function to get the response from Gemini AI
def get_response(user_input):
    response = chat_session.send_message(user_input)
    response_text = response.text

    # Limit the response to 50 words
    response_words = response_text.split()
    if len(response_words) > 50:
        response_text = ' '.join(response_words[:50]) + '...'

    return response_text

# Function to take a picture
def take_picture():
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            return {"error": "Could not open webcam."}

        # Capture the frame
        ret, frame = cap.read()
        if not ret:
            return {"error": "Failed to capture image."}

        # Save the frame as an image file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"picture_{timestamp}.jpg"
        cv2.imwrite(filename, frame)

        # Release the webcam
        cap.release()

        return {"success": True, "filename": filename, "description": f"Picture saved as {filename}"}
    except Exception as e:
        return {"error": str(e)}

# Function to get current weather
def get_weather(city):
    api_key = "weather_api"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("cod") != 200:
        return {"error": response.get("message", "Error fetching weather data.")}

    weather = response["weather"][0]["description"]
    temperature = response["main"]["temp"]
    humidity = response["main"]["humidity"]
    wind_speed = response["wind"]["speed"]

    weather_info = (f"Current weather in {city}: {weather}. "
                    f"Temperature: {temperature}°C, "
                    f"Humidity: {humidity}%, "
                    f"Wind Speed: {wind_speed} m/s.")

    return {"weather_info": weather_info}

# Function to handle API requests
def handle_api_request(module, parameters=None):
    if module == "TakePicture":
        engine.say("Sure, I'll take a wonderful picture of yours, keep smiling.")
        engine.runAndWait()
        response = take_picture()
        if response.get("success"):
            description = response["description"]
            return description
        else:
            error_message = response["error"]
            return error_message
    elif module == "Weather":
        city = parameters["city"]
        response = get_weather(city)
        if "error" in response:
            error_message = response["error"]
            return error_message
        else:
            weather_info = response["weather_info"]
            return weather_info
    else:
        return "Unknown module"

# Main loop to test the response system
while True:
    user_input = input('You: ')
    if "exit" in user_input.lower():
        print("Bot: Goodbye!")
        engine.say("Goodbye!")
        engine.runAndWait()
        break

    response_text = ""

    if "take a picture" in user_input.lower():
        response_text = handle_api_request("TakePicture")
    elif "weather" in user_input.lower():
        # Extract city name from the input
        match = re.search(r'weather\s+in\s+(.*)', user_input.lower())
        if match:
            city = match.group(1).strip()
            response_text = handle_api_request("Weather", {"city": city})
        else:
            response_text = "Please specify the city for which you want to know the weather."
    else:
        response_text = get_response(user_input)

    print("Bot:", response_text)
    engine.say(response_text)
    engine.runAndWait()
