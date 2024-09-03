# Weather App with PM Accelerator Info

## Overview

This is a Streamlit-based web application that allows users to check the current weather, hourly forecast, and 5-day forecast for a specific city or their current location.

## Features

### 1. Current Weather
- Users can input a city name to retrieve the current weather conditions.
- The application displays the temperature, weather description, and an icon representing the current weather conditions.
- The temperature can be displayed in either Celsius or Fahrenheit.

### 2. 12-Hour Forecast
- The app provides a 12-hour forecast with temperature, weather description, and weather icons for each hour.

### 3. 5-Day Forecast
- Users can view a 5-day forecast, which includes the day’s name, date, temperature, and weather description.
- Icons corresponding to the weather conditions are displayed for each day.

### 4. Location-Based Weather
- The app can automatically detect the user's location based on their IP address.
- Users can click a button to get the weather for their current location, which includes all the features mentioned above (current weather, hourly forecast, 5-day forecast).

## How to Run

### Prerequisites
- Python 3.x installed on your machine.
- The following Python libraries should be installed:
  - `streamlit`
  - `requests`
  - `Pillow`

### Running the App

1. **Install the Required Packages:**
   ```bash
   pip install streamlit requests Pillow
   ```
   
2. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

3. **Access the Application:**
   - The app will open in your default web browser.
   - You can enter a city name to get the weather data or click the button to get weather data based on your current location.

## Code Breakdown

### API Integration
- **OpenWeather API** is used to fetch current weather data, hourly forecast, and 5-day forecast.
- The API responses are parsed and displayed using Streamlit’s UI components.

### Image Handling
- Weather icons are fetched from the OpenWeather API and displayed using the `Pillow` library to handle images.

### Location Services
- The app can retrieve the user's location based on their IP address using the `ipinfo.io` API.

## Conclusion
This Weather App provides a comprehensive way for users to check the weather for any city or their current location. 
