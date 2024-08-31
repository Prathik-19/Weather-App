# Weather App

## Overview

This is a Python-based desktop application that provides weather information for any city or the user's current location. The app is built using the Tkinter and Ttkbootstrap libraries for the GUI, and it leverages the OpenWeather API to fetch weather data. The application can display the current weather, a 5-day weather forecast, and a 5-hour hourly forecast. It also allows users to switch between Celsius and Fahrenheit units dynamically.

## Features

- **Current Weather:** Displays the current weather for a user-specified city or the user's current location.
- **5-Day Forecast:** Provides a 5-day weather forecast for the selected city or location.
- **Hourly Forecast:** Shows the weather forecast for the next 5 hours based on the current time.
- **Temperature Unit Switching:** Users can switch between Celsius and Fahrenheit units, and the weather information updates automatically without the need for additional searches.
- **Dynamic Location Detection:** Automatically detects the user's location using their IP address and provides accurate weather information for that location.
- **Responsive Design:** The app adjusts its layout based on the content, ensuring a clean and organized display.

## Requirements

To run this application, you need the following:

- Python 3.x
- Required Python libraries:
  - `requests`
  - `PIL` (Python Imaging Library, also known as `Pillow`)
  - `ttkbootstrap`
  - `tkinter`

### Installation of Required Libraries

You can install the required libraries using pip:

```bash
pip install requests Pillow ttkbootstrap
```

## How to Run the Application

1. **Clone the Repository or Download the Code:**
   - Clone this repository or download the code files to your local machine.

2. **Set Up OpenWeather API Key:**
   - Ensure you have a valid OpenWeather API key. You can sign up for a free API key at [OpenWeather](https://home.openweathermap.org/users/sign_up).
   - Replace the placeholder `API_key` in the code with your actual API key.

3. **Run the Application:**
   - Open a terminal or command prompt.
   - Navigate to the directory where the `weather_app.py` (or your chosen filename) is located.
   - Run the application using Python:

   ```bash
   python weather_app.py
   ```

4. **Using the Application:**
   - **Search for a City:** Enter a city name in the input box and press "Enter" or click the "Search" button to display the weather information for that city.
   - **Get Weather for Current Location:** Click the "Get Weather for My Location" button to automatically detect your location and display the weather information.
   - **Switch Temperature Units:** Use the radio buttons to switch between Celsius and Fahrenheit units. The app will automatically update the displayed weather information based on the selected unit.

## Code Explanation

### Key Components

- **Tkinter and Ttkbootstrap GUI:** 
  - The application uses Tkinter for the graphical user interface, with Ttkbootstrap enhancing the appearance and providing modern widget themes.

- **OpenWeather API Integration:**
  - The app fetches weather data from the OpenWeather API. It supports fetching current weather, a 5-day forecast, and a 5-hour hourly forecast.
  - The `get_weather`, `get_forecast`, and `get_hourly_forecast_by_coords` functions interact with the OpenWeather API to retrieve weather data.

- **Location Detection:**
  - The app detects the user's current location using the IP address via the `ipinfo.io` service. The function `get_location_by_ip` is responsible for this task.

- **Dynamic Unit Switching:**
  - The app allows users to switch between Celsius and Fahrenheit. The `switch_units` function ensures that the displayed weather information updates automatically when the user selects a different temperature unit.

### Main Functions

- **get_weather(city, unit):** Fetches the current weather for the specified city.
- **get_weather_by_coords(lat, lon, unit):** Fetches the current weather based on geographical coordinates.
- **get_forecast(city, unit):** Fetches a 5-day weather forecast for the specified city.
- **get_forecast_by_coords(lat, lon, unit):** Fetches a 5-day weather forecast based on geographical coordinates.
- **get_hourly_forecast_by_coords(lat, lon, unit):** Fetches a 5-hour weather forecast based on geographical coordinates.
- **get_location_by_ip():** Retrieves the user's current location using their IP address.
- **display_weather_and_forecast(city, current_weather, forecast, hourly_forecast, is_current_location=False):** Displays the weather information, including the current weather, 5-day forecast, and hourly forecast.
- **search_by_location():** Fetches and displays the weather information for the user's current location.
- **search(event=None):** Fetches and displays the weather information for the city entered by the user.
- **switch_units():** Updates the weather information when the user switches between Celsius and Fahrenheit.

## Notes

- **Accuracy:** The accuracy of location detection via IP address may vary, especially in smaller cities or regions. This app relies on the data provided by the `ipinfo.io` service, which may not always be perfectly accurate.
- **OpenWeather API:** Ensure your API key is active and has not exceeded its usage limits, especially if you're on a free tier.

## Troubleshooting

- **City Not Found Error:** If you receive a "City not found" error, double-check the spelling of the city name. The OpenWeather API may not recognize misspelled or non-standard city names.
- **API Key Issues:** If you encounter issues with fetching data, ensure that your API key is correctly set and that it has not exceeded its usage limits.
