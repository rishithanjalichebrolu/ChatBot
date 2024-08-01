# Chatbot Project Overview
**Project Description**

This project features a versatile chatbot that integrates multiple functionalities using various technologies. The chatbot leverages Google's Gemini API for generative responses, integrates with a text-to-speech engine, captures images, and provides weather updates. It serves as a demonstration of how to combine different APIs and tools to create a cohesive and interactive application.

**Features**

**Generative AI Responses:**
Utilizes the Gemini API for generating text-based responses, enabling the chatbot to engage in conversations and provide informative answers.

**Text-to-Speech:**
Implements the pyttsx3 library for converting text responses into spoken words, enhancing the interactivity of the chatbot.

**Image Capture:** 
Uses OpenCV to capture and save images from the webcam, offering users the ability to take pictures through the chatbot interface.

**Weather Information:**
Integrates with the OpenWeatherMap API to fetch and display current weather conditions based on user-specified cities.

**Technologies Used**

**Google Gemini API:**
For generating conversational responses and handling user interactions.

**pyttsx3:**
A text-to-speech library for converting text into audible speech.

**OpenCV:** 
For capturing and processing images from the webcam.

**OpenWeatherMap API:** 
For retrieving and presenting weather data.

**Key Components**

**Generative AI Configuration:** 
Configured the Gemini API with safety settings and generation parameters to ensure appropriate and engaging responses.

**Text-to-Speech Engine:**
Set up pyttsx3 to provide spoken feedback to the user, using the second voice option for varied auditory output.

**Image Capture Functionality:** 
Developed a function to capture and save images, including error handling and file management.

**Weather Information Retrieval:** 
Implemented functionality to parse user input for city names and fetch weather details using an external weather API.

**How It Works**

**User Input:** 
The chatbot processes user inputs to determine whether to generate a response, take a picture, or provide weather information.

**Response Generation:** 
For general queries, the chatbot uses the Gemini API to generate a response, which is then converted to speech using pyttsx3.

**Image Capture:** 
If the user requests to take a picture, the chatbot captures an image from the webcam and saves it with a timestamp.

**Weather Information:** 
When asked for weather updates, the chatbot extracts the city name from the user input, fetches weather data, and provides the information in response.

**Usage**

Run the script to start the chatbot and interact with it through the terminal. 
**You can:**

>>Ask the chatbot to take a picture.
>>Request weather updates by specifying a city.
>>Engage in general conversation to receive AI-generated responses.
>>Type exit to end the session.
