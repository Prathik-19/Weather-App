import streamlit as st
import requests
from PIL import Image
from datetime import datetime
from io import BytesIO

# --------------------- Configuration ---------------------

# Your OpenWeather API key
API_KEY = "e008fc2c8eb712b2f41097809c7b97f2"

# --------------------- Helper Functions ---------------------

def get_weather(city, unit):
    """Fetch current weather data for a given city."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    res = requests.get(url)

    if res.status_code == 404:
        st.error("City not found")
        return None

    weather = res.json()
    icon_id = weather['weather'][0]['icon']

    if unit == "Celsius":
        temperature = weather['main']['temp'] - 273.15
        temp_unit = "°C"
    else:
        temperature = (weather['main']['temp'] - 273.15) * 9/5 + 32
        temp_unit = "°F"

    description = weather['weather'][0]['description'].capitalize()
    city = weather['name']
    country = weather['sys']['country']
    state = weather.get('state', '')  # Handle state if available

    dt = weather['dt']
    date = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d')
    day_name = datetime.utcfromtimestamp(dt).strftime('%A')

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return {
        "icon_url": icon_url,
        "temperature": temperature,
        "temp_unit": temp_unit,
        "description": description,
        "city": city,
        "state": state,
        "country": country,
        "date": date,
        "day_name": day_name
    }

def get_weather_by_coords(lat, lon, unit):
    """Fetch current weather data based on geographic coordinates."""
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    res = requests.get(url)

    if res.status_code == 404:
        st.error("Location not found")
        return None

    return get_weather_by_coords_helper(res.json(), unit)

def get_weather_by_coords_helper(weather, unit):
    """Helper function to parse weather data from coordinates."""
    icon_id = weather['weather'][0]['icon']

    if unit == "Celsius":
        temperature = weather['main']['temp'] - 273.15
        temp_unit = "°C"
    else:
        temperature = (weather['main']['temp'] - 273.15) * 9/5 + 32
        temp_unit = "°F"

    description = weather['weather'][0]['description'].capitalize()
    city = weather['name']
    country = weather['sys']['country']
    state = weather.get('state', '')  # Handle state if available

    dt = weather['dt']
    date = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d')
    day_name = datetime.utcfromtimestamp(dt).strftime('%A')

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return {
        "icon_url": icon_url,
        "temperature": temperature,
        "temp_unit": temp_unit,
        "description": description,
        "city": city,
        "state": state,
        "country": country,
        "date": date,
        "day_name": day_name
    }

def get_forecast(city, unit):
    """Fetch 5-day weather forecast for a given city."""
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    res = requests.get(url)

    if res.status_code != 200:
        st.error("Unable to retrieve forecast")
        return None

    forecast = res.json()
    forecast_data = []
    days_seen = set()

    for entry in forecast['list']:
        timestamp = entry['dt_txt']
        date = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        day_name = date.strftime('%A')
        date_str = date.strftime('%Y-%m-%d')

        if date_str not in days_seen:
            days_seen.add(date_str)
            if len(forecast_data) < 5:
                if unit == "Celsius":
                    temp = entry['main']['temp'] - 273.15
                    temp_unit = "°C"
                else:
                    temp = (entry['main']['temp'] - 273.15) * 9/5 + 32
                    temp_unit = "°F"
                description = entry['weather'][0]['description'].capitalize()
                icon_id = entry['weather'][0]['icon']
                icon_url = f"https://openweathermap.org/img/wn/{icon_id}.png"
                forecast_data.append({
                    "day_name": day_name,
                    "date_str": date_str,
                    "temp": temp,
                    "temp_unit": temp_unit,
                    "description": description,
                    "icon_url": icon_url
                })

    return forecast_data

def get_forecast_by_coords(lat, lon, unit):
    """Fetch 5-day weather forecast based on geographic coordinates."""
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"
    res = requests.get(url)

    if res.status_code != 200:
        st.error("Unable to retrieve forecast")
        return None

    return get_forecast_by_coords_helper(res.json(), unit)

def get_forecast_by_coords_helper(forecast, unit):
    """Helper function to parse forecast data from coordinates."""
    forecast_data = []
    days_seen = set()

    for entry in forecast['list']:
        timestamp = entry['dt_txt']
        date = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        day_name = date.strftime('%A')
        date_str = date.strftime('%Y-%m-%d')

        if date_str not in days_seen:
            days_seen.add(date_str)
            if len(forecast_data) < 5:
                if unit == "Celsius":
                    temp = entry['main']['temp'] - 273.15
                    temp_unit = "°C"
                else:
                    temp = (entry['main']['temp'] - 273.15) * 9/5 + 32
                    temp_unit = "°F"
                description = entry['weather'][0]['description'].capitalize()
                icon_id = entry['weather'][0]['icon']
                icon_url = f"https://openweathermap.org/img/wn/{icon_id}.png"
                forecast_data.append({
                    "day_name": day_name,
                    "date_str": date_str,
                    "temp": temp,
                    "temp_unit": temp_unit,
                    "description": description,
                    "icon_url": icon_url
                })

    return forecast_data

def get_hourly_forecast(city, unit):
    """Fetch hourly forecast data based on city name."""
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    res = requests.get(url)

    if res.status_code != 200:
        st.error("Unable to retrieve hourly forecast")
        return None

    return get_hourly_forecast_helper(res.json(), unit)

def get_hourly_forecast_by_coords(lat, lon, unit):
    """Fetch hourly forecast data based on geographic coordinates."""
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"
    res = requests.get(url)

    if res.status_code != 200:
        st.error("Unable to retrieve hourly forecast")
        return None

    return get_hourly_forecast_helper(res.json(), unit)

def get_hourly_forecast_helper(forecast, unit):
    """Helper function to parse hourly forecast data."""
    hourly_forecast = []
    current_time = datetime.utcnow()

    for entry in forecast['list']:
        timestamp = entry['dt_txt']
        forecast_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        if forecast_time > current_time and len(hourly_forecast) < 5:
            hour = forecast_time.strftime('%I %p')
            if unit == "Celsius":
                temp = entry['main']['temp'] - 273.15
                temp_unit = "°C"
            else:
                temp = (entry['main']['temp'] - 273.15) * 9/5 + 32
                temp_unit = "°F"

            description = entry['weather'][0]['description'].capitalize()
            icon_id = entry['weather'][0]['icon']
            icon_url = f"https://openweathermap.org/img/wn/{icon_id}.png"
            hourly_forecast.append({
                "hour": hour,
                "temp": temp,
                "temp_unit": temp_unit,
                "description": description,
                "icon_url": icon_url
            })

    return hourly_forecast

def get_location_by_ip():
    """Retrieve user's location based on IP address."""
    try:
        res = requests.get("https://ipinfo.io/json")
        data = res.json()
        loc = data['loc'].split(',')
        lat = loc[0]
        lon = loc[1]
        city = data.get('city', '')
        region = data.get('region', '')
        country = data.get('country', '')
        return lat, lon, city, region, country
    except Exception as e:
        st.error(f"Unable to retrieve location: {e}")
        return None, None, None, None, None

def show_info():
    """Display information about the PM Accelerator."""
    st.sidebar.markdown(
        """
        ## PM Accelerator

        **PM Accelerator Description:**

        Hiring and getting hired for product management roles is hard. 
        In the short timeframe of an interview, it is difficult to precisely assess 
        and display the necessary, complex skills.

        Product Managers play key roles in a company. Hiring for those positions 
        shouldn’t be a guessing game.

        It is our vision to make it simple and beneficial for Product Managers to 
        accurately display their skills and empower hiring companies to choose the right 
        Product Manager every time.
        """
    )

def display_weather_and_forecast(current_weather, forecast_data, hourly_forecast, location_text):
    """Display current weather, 5-day forecast, and hourly forecast."""
    st.markdown(f"### {location_text}")
    st.markdown(f"**{current_weather['day_name']}, {current_weather['date']}**")

    # Display Current Weather
    col_icon, col_temp_desc = st.columns([1, 3])
    with col_icon:
        response = requests.get(current_weather['icon_url'])
        img = Image.open(BytesIO(response.content))
        st.image(img)
    with col_temp_desc:
        st.write(f"**Temperature:** {current_weather['temperature']:.2f}{current_weather['temp_unit']}")
        st.write(f"**Description:** {current_weather['description']}")

    # Display Hourly Forecast
    st.markdown("#### Hourly Forecast")
    hourly_cols = st.columns(5)
    for i, forecast in enumerate(hourly_forecast):
        with hourly_cols[i]:
            response = requests.get(forecast['icon_url'])
            img = Image.open(BytesIO(response.content))
            st.image(img, width=50)
            st.write(forecast['hour'])
            st.write(f"{forecast['temp']:.2f}{forecast['temp_unit']}")
            st.write(forecast['description'])

    # Display 5-Day Forecast
    st.markdown("#### 5-Day Forecast")
    forecast_cols = st.columns(5)
    for i, forecast in enumerate(forecast_data):
        with forecast_cols[i]:
            response = requests.get(forecast['icon_url'])
            img = Image.open(BytesIO(response.content))
            st.image(img, width=50)
            st.write(forecast['day_name'])
            st.write(forecast['date_str'])
            st.write(f"{forecast['temp']:.2f}{forecast['temp_unit']}")
            st.write(forecast['description'])

# --------------------- Streamlit Layout ---------------------

st.set_page_config(page_title="Weather App", layout="wide")
st.title("🌤️ Weather App")

# Sidebar for PM Accelerator Info
with st.sidebar:
    st.header("About")
    st.write("Website Developed by Prathik Kallepalli")
    st.write("Click the button below to see information about PM Accelerator.")
    if st.button("Show PM Accelerator Info"):
        show_info()

# Main Inputs
col1, col2, col3 = st.columns([3, 1, 3])

# City Input in col1
with col1:
    city_input = st.text_input("Enter City Name:", "")

# Temperature Unit selection in col2
with col2:
    unit = st.radio("Temperature Unit:", ["Celsius", "Fahrenheit"], horizontal=True)

# Search Weather based on city input
with col3:
    if st.button("Search Weather"):
        st.session_state['search'] = True
        st.session_state['unit'] = unit
        st.session_state['current_weather'] = None  # Reset weather to avoid auto update
        st.session_state['current_location'] = None

# Initialize session state if not already done
if 'search' not in st.session_state:
    st.session_state['search'] = False

if 'unit' not in st.session_state:
    st.session_state['unit'] = unit

if 'first_load' not in st.session_state:
    st.session_state['first_load'] = True

# Get Weather for Current Location button
if st.button("Get Weather for My Location"):
    st.session_state['unit'] = unit  # Capture the unit selected when the button is clicked
    st.session_state['search'] = False  # Ensure no search-related data is used
    st.session_state['current_location'] = None  # Clear previous location
    st.session_state['current_weather'] = None  # Clear previous weather data

    lat, lon, city, region, country = get_location_by_ip()
    if lat and lon:
        current_weather = get_weather_by_coords(lat, lon, st.session_state['unit'])
        forecast_data = get_forecast_by_coords(lat, lon, st.session_state['unit'])
        hourly_forecast = get_hourly_forecast_by_coords(lat, lon, st.session_state['unit'])

        if current_weather and forecast_data and hourly_forecast:
            location_text = f"My Location - {current_weather['city']}, {current_weather['country']}"
            display_weather_and_forecast(current_weather, forecast_data, hourly_forecast, location_text)
            st.session_state['current_location'] = f"{city}, {country}"
            st.session_state['current_weather'] = current_weather
            st.session_state['forecast_data'] = forecast_data
            st.session_state['hourly_forecast'] = hourly_forecast
            st.session_state['first_load'] = False

# Automatically get the weather for the user's current location when the app opens
if st.session_state['first_load']:
    lat, lon, city, region, country = get_location_by_ip()
    if lat and lon:
        current_weather = get_weather_by_coords(lat, lon, st.session_state['unit'])
        forecast_data = get_forecast_by_coords(lat, lon, st.session_state['unit'])
        hourly_forecast = get_hourly_forecast_by_coords(lat, lon, st.session_state['unit'])

        if current_weather and forecast_data and hourly_forecast:
            location_text = f"My Location - {current_weather['city']}, {current_weather['country']}"
            display_weather_and_forecast(current_weather, forecast_data, hourly_forecast, location_text)
            st.session_state['current_location'] = f"{city}, {country}"
            st.session_state['current_weather'] = current_weather
            st.session_state['forecast_data'] = forecast_data
            st.session_state['hourly_forecast'] = hourly_forecast
    
    st.session_state['first_load'] = False

# If the user searches for a city
if st.session_state['search']:
    if city_input:
        current_weather = get_weather(city_input, st.session_state['unit'])
        forecast_data = get_forecast(city_input, st.session_state['unit'])
        hourly_forecast = get_hourly_forecast(city_input, st.session_state['unit'])

        if current_weather and forecast_data and hourly_forecast:
            location_text = f"{current_weather['city']}, {current_weather['country']}"
            display_weather_and_forecast(current_weather, forecast_data, hourly_forecast, location_text)
            st.session_state['current_location'] = f"{city_input}, {current_weather['country']}"
            st.session_state['current_weather'] = current_weather
            st.session_state['forecast_data'] = forecast_data
            st.session_state['hourly_forecast'] = hourly_forecast
    else:
        st.error("Please enter a city name to search.")

