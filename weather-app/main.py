# e2bd649246994ab988155022231211

# Import the necessary libraries
import requests
import json

# Display a welcome message
print("Welcome to the Weather Information App!")

# Ask the user to input the name of the city
city = input("Enter the name of the city: ")

# Construct the URL for the weather API using the user-input city and an API key
url = f"https://api.weatherapi.com/v1/current.json?key=e2bd649246994ab988155022231211&q={city}"

# Make a GET request to the weather API using the constructed URL
try:
    r = requests.get(url)
    r.raise_for_status()  # Raise an HTTPError for bad responses
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    exit()

# Check if the request was successful
if r.status_code == 200:
    # Parse the JSON response text into a Python dictionary
    weather_dictionary = json.loads(r.text)

    # Display the current weather information
    print("\nWeather Information for", city)
    print("Condition:", weather_dictionary["current"]["condition"]["text"])
    print("Temperature (Celsius):", weather_dictionary["current"]["temp_c"])
    print("Humidity:", weather_dictionary["current"]["humidity"])
else:

    print(f"Failed to retrieve weather information. Status Code: {r.status_code}")
