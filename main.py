#import necessary modules
from flask import Flask, render_template, request
import requests

app = Flask(__name__)  # Create Flask application instance

# Define the route for the home page


@app.route('/')
def index():
  return render_template('index.html')  # Render the index.html template


@app.route('/weather',
           methods=['POST'])  # Define route for weather information retrieval
def weather():
  city = request.form[
      'city']  # Get the city name from the form submitted by the user
  api_key = '35ffc974ff101f345b7aa0dea8dbf89e'  # API key for accessing OpenWeatherMap API
  url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
  response = requests.get(url)  # Send HTTP GET request to the API
  data = response.json()  # Convert API response to JSON format
  if response.status_code == 200:  # If the request was successful (status code 200)
    temperature = round(data['main']['temp'] - 273.15,
                        2)  # Convert temperature from Kelvin to Celsius
    description = data['weather'][0][
        'description']  # Extract weather description from API response
    return render_template('weather.html',
                           city=city,
                           temperature=temperature,
                           description=description)
  else:  # If the request was unsuccessful
    error_message = data['message']
    return render_template('error.html', error_message=error_message)
  # Render the error.html template with error message


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
# Run the Flask application on host '0.0.0.0' and port 8080
