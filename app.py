import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap
from datetime import datetime

# Your OpenWeather API key
API_key = "e008fc2c8eb712b2f41097809c7b97f2"

# Global variables to store current weather and forecasts for switching units
current_weather_data = None
forecast_data = None
hourly_forecast_data = None

# Function to display information about the PM Accelerator
def show_info():
    info_text = ("PM Accelerator Description:\n\n"
                 "Hiring and getting hired for product management roles is hard. "
                 "In the short timeframe of an interview, it is difficult to precisely assess "
                 "and display the necessary, complex skills.\n\n"
                 "Product Managers play key roles in a company. Hiring for those positions "
                 "shouldn’t be a guessing game.\n\n"
                 "It is our vision, to make it simple and beneficial for Product Managers to "
                 "accurately display their skills and empower hiring companies to choose the right "
                 "Product Manager every time.")
    messagebox.showinfo("PM Accelerator", info_text)

# Function to get current weather information from Open Weather Map API by city name
def get_weather(city, unit):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None
    
    # Parse the response JSON to get weather information
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    
    # Convert temperature to Celsius or Fahrenheit based on the selected unit
    if unit == "Celsius":
        temperature = weather['main']['temp'] - 273.15
        temp_unit = "°C"
    else:
        temperature = (weather['main']['temp'] - 273.15) * 9/5 + 32
        temp_unit = "°F"
    
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']
    state = weather.get('state', '')  # Some APIs might return the state field, handle it here
    
    # Get the date and day name
    dt = weather['dt']
    date = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d')
    day_name = datetime.utcfromtimestamp(dt).strftime('%A')

    # Get the icon URL and return all the weather information
    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, temp_unit, description, city, state, country, date, day_name)

# Function to get current weather information from Open Weather Map API by coordinates
def get_weather_by_coords(lat, lon, unit):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "Location not found")
        return None
    
    # Parse the response JSON to get weather information
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    
    # Convert temperature to Celsius or Fahrenheit based on the selected unit
    if unit == "Celsius":
        temperature = weather['main']['temp'] - 273.15
        temp_unit = "°C"
    else:
        temperature = (weather['main']['temp'] - 273.15) * 9/5 + 32
        temp_unit = "°F"
    
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']
    state = weather.get('state', '')  # Handle the state field if available
    
    # Get the date and day name
    dt = weather['dt']
    date = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d')
    day_name = datetime.utcfromtimestamp(dt).strftime('%A')

    # Get the icon URL and return all the weather information
    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, temp_unit, description, city, state, country, date, day_name)

# Function to get the 5-day forecast from OpenWeather API by city name
def get_forecast(city, unit):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code != 200:
        messagebox.showerror("Error", "Unable to retrieve forecast")
        return None
    
    forecast = res.json()
    forecast_data = []
    days_seen = set()
    
    # Extract forecast data and ensure only one entry per day
    for entry in forecast['list']:
        timestamp = entry['dt_txt']
        date = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        day_name = date.strftime('%A')
        date_str = date.strftime('%Y-%m-%d')
        
        if date_str not in days_seen:
            days_seen.add(date_str)
            if len(forecast_data) < 5:  # Limit to 5 days
                if unit == "Celsius":
                    temp = entry['main']['temp'] - 273.15
                    temp_unit = "°C"
                else:
                    temp = (entry['main']['temp'] - 273.15) * 9/5 + 32
                    temp_unit = "°F"
                description = entry['weather'][0]['description']
                icon_id = entry['weather'][0]['icon']
                icon_url = f"https://openweathermap.org/img/wn/{icon_id}.png"
                forecast_data.append((day_name, date_str, temp, temp_unit, description, icon_url))
    
    return forecast_data

# Function to get the 5-day forecast from OpenWeather API by coordinates
def get_forecast_by_coords(lat, lon, unit):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}"
    res = requests.get(url)

    if res.status_code != 200:
        messagebox.showerror("Error", "Unable to retrieve forecast")
        return None
    
    forecast = res.json()
    forecast_data = []
    days_seen = set()
    
    # Extract forecast data and ensure only one entry per day
    for entry in forecast['list']:
        timestamp = entry['dt_txt']
        date = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        day_name = date.strftime('%A')
        date_str = date.strftime('%Y-%m-%d')
        
        if date_str not in days_seen:
            days_seen.add(date_str)
            if len(forecast_data) < 5:  # Limit to 5 days
                if unit == "Celsius":
                    temp = entry['main']['temp'] - 273.15
                    temp_unit = "°C"
                else:
                    temp = (entry['main']['temp'] - 273.15) * 9/5 + 32
                    temp_unit = "°F"
                description = entry['weather'][0]['description']
                icon_id = entry['weather'][0]['icon']
                icon_url = f"https://openweathermap.org/img/wn/{icon_id}.png"
                forecast_data.append((day_name, date_str, temp, temp_unit, description, icon_url))
    
    return forecast_data

# Function to get the hourly forecast from OpenWeather API by coordinates
def get_hourly_forecast_by_coords(lat, lon, unit):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}"
    res = requests.get(url)

    if res.status_code != 200:
        messagebox.showerror("Error", "Unable to retrieve hourly forecast")
        return None
    
    forecast = res.json()
    hourly_forecast = []
    current_time = datetime.utcnow()  # Use UTC for alignment with API time

    # Extract the next 5 hourly forecasts based on the current time
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
            
            description = entry['weather'][0]['description']
            icon_id = entry['weather'][0]['icon']
            icon_url = f"https://openweathermap.org/img/wn/{icon_id}.png"
            hourly_forecast.append((hour, temp, temp_unit, description, icon_url))
    
    return hourly_forecast

# Function to get the user's current location using ipinfo.io
def get_location_by_ip():
    try:
        res = requests.get("https://ipinfo.io/json")
        data = res.json()
        loc = data['loc'].split(',')
        lat = loc[0]
        lon = loc[1]
        return lat, lon, data['city'], data['region'], data['country']
    except Exception as e:
        messagebox.showerror("Error", f"Unable to retrieve location: {e}")
        return None, None, None, None, None

# Function to display weather and forecast
def display_weather_and_forecast(city, current_weather, forecast, hourly_forecast, is_current_location=False):
    if current_weather is None or forecast is None or hourly_forecast is None:
        location_label.config(text="")
        forecast_frame.pack_forget()
        hourly_frame.pack_forget()
        return

    # Unpack the current weather information
    icon_url, temperature, temp_unit, description, city, state, country, date, day_name = current_weather
    location_text = f"{city}, {state}, {country}" if state else f"{city}, {country}"
    if is_current_location:
        location_text = f"My Location - {location_text}"
    location_label.configure(text=location_text)

    # Display the date and day of the week above the temperature
    date_label.configure(text=f"{day_name}, {date}")
    
    # Get the weather icon image from the url and update the icon label
    weather_image = Image.open(requests.get(icon_url, stream=True).raw)
    weather_icon = ImageTk.PhotoImage(weather_image)
    icon_label.configure(image=weather_icon)
    icon_label.image = weather_icon

    # Update the temperature and description labels
    temperature_label.configure(text=f"Temperature: {temperature:.2f}{temp_unit}")
    description_label.configure(text=f"Description: {description}")
    
    # Update the hourly forecast
    for widget in hourly_frame.winfo_children():
        widget.destroy()

    for i, entry in enumerate(hourly_forecast):
        hour, temp, temp_unit, desc, icon_url = entry
        
        # Hourly icon
        hourly_icon_image = Image.open(requests.get(icon_url, stream=True).raw)
        hourly_icon = ImageTk.PhotoImage(hourly_icon_image)
        hourly_icon_label = ttkbootstrap.Label(hourly_frame, image=hourly_icon)
        hourly_icon_label.image = hourly_icon  # Prevent garbage collection
        hourly_icon_label.grid(row=0, column=i, padx=3, pady=3)

        # Hourly time and temperature
        hour_label = ttkbootstrap.Label(hourly_frame, text=f"{hour}\n{temp:.2f}{temp_unit}", font="Helvetica, 9")
        hour_label.grid(row=1, column=i, padx=3, pady=3)

        # Hourly description
        desc_label = ttkbootstrap.Label(hourly_frame, text=desc, font="Helvetica, 9")
        desc_label.grid(row=2, column=i, padx=3, pady=3)

    # Update the 5-day forecast
    for widget in forecast_frame.winfo_children():
        widget.destroy()

    for i, entry in enumerate(forecast):
        day_name, date_str, temp, temp_unit, desc, icon_url = entry
        
        # Forecast icon
        forecast_icon_image = Image.open(requests.get(icon_url, stream=True).raw)
        forecast_icon = ImageTk.PhotoImage(forecast_icon_image)
        forecast_icon_label = ttkbootstrap.Label(forecast_frame, image=forecast_icon)
        forecast_icon_label.image = forecast_icon  # Prevent garbage collection
        forecast_icon_label.grid(row=i, column=0, padx=3, pady=3)

        # Date and day
        day_label = ttkbootstrap.Label(forecast_frame, text=f"{day_name}, {date_str}", font="Helvetica, 10")
        day_label.grid(row=i, column=1, padx=3, pady=3, sticky="w")

        # Temperature and description
        details = f"{temp:.2f}{temp_unit}, {desc}"
        details_label = ttkbootstrap.Label(forecast_frame, text=details, font="Helvetica, 10")
        details_label.grid(row=i, column=2, padx=3, pady=3, sticky="w")

    # Resize the window based on the content
    root.update_idletasks()  # Update the window's geometry before calculating the size
    window_width = max(root.winfo_width(), 400)  # Ensure a minimum width
    window_height = root.winfo_reqheight() + (i + 1) * 55  # Calculate height based on the forecast days
    root.geometry(f"{window_width}x{window_height}")

# Function to search weather for the user's location
def search_by_location():
    global current_weather_data, forecast_data, hourly_forecast_data
    lat, lon, city, region, country = get_location_by_ip()
    if lat and lon:
        unit = temp_unit_var.get()
        current_weather_data = get_weather_by_coords(lat, lon, unit)
        forecast_data = get_forecast_by_coords(lat, lon, unit)
        hourly_forecast_data = get_hourly_forecast_by_coords(lat, lon, unit)
        display_weather_and_forecast(f"{city}, {region}", current_weather_data, forecast_data, hourly_forecast_data, is_current_location=True)

# Function to search weather and forecast for a city
def search(event=None):  # event parameter added to handle the Enter key event
    global current_weather_data, forecast_data, hourly_forecast_data
    city = city_entry.get()
    unit = temp_unit_var.get()
    current_weather_data = get_weather(city, unit)
    forecast_data = get_forecast(city, unit)
    lat, lon = get_location_by_ip()[:2]
    hourly_forecast_data = get_hourly_forecast_by_coords(lat, lon, unit)
    display_weather_and_forecast(city, current_weather_data, forecast_data, hourly_forecast_data)

# Function to switch units automatically when the radio buttons are changed
def switch_units():
    global current_weather_data, forecast_data, hourly_forecast_data
    if current_weather_data and forecast_data and hourly_forecast_data:
        unit = temp_unit_var.get()
        # Recalculate the temperatures in the selected unit
        current_weather_data = get_weather(current_weather_data[4], unit)
        forecast_data = get_forecast(current_weather_data[4], unit)
        lat, lon = get_location_by_ip()[:2]
        hourly_forecast_data = get_hourly_forecast_by_coords(lat, lon, unit)
        display_weather_and_forecast(current_weather_data[4], current_weather_data, forecast_data, hourly_forecast_data)

root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")

# Entry widget -> to enter the city name
city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=5)
city_entry.bind("<Return>", search)  # Bind the Enter key to trigger the search

# Radio buttons for Celsius vs Fahrenheit
temp_unit_var = tk.StringVar(value="Celsius")
celsius_radio = ttkbootstrap.Radiobutton(root, text="Celsius", variable=temp_unit_var, value="Celsius", bootstyle="success", command=switch_units)
celsius_radio.pack(pady=3)
fahrenheit_radio = ttkbootstrap.Radiobutton(root, text="Fahrenheit", variable=temp_unit_var, value="Fahrenheit", bootstyle="info", command=switch_units)
fahrenheit_radio.pack(pady=3)

# Button widget -> to search weather manually
search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=5)

# Button widget -> to search weather for user's location
location_button = ttkbootstrap.Button(root, text="Get Weather for My Location", command=search_by_location, bootstyle="primary")
location_button.pack(pady=5)

# Button widget -> Info button to show PM Accelerator description
info_button = ttkbootstrap.Button(root, text="Info", command=show_info, bootstyle="secondary")
info_button.place(relx=0.95, rely=0.05, anchor="ne")  # Place at the top right corner

# Label widget -> to show the city/country name 
location_label = tk.Label(root, font="Helvetica, 22")
location_label.pack(pady=5)

# Label widget -> to show the date and day of the week
date_label = tk.Label(root, font="Helvetica, 16")
date_label.pack(pady=3)

# Label widget -> to show weather icon
icon_label = tk.Label(root)
icon_label.pack(pady=3)

# Label widget -> to show the temperature 
temperature_label = tk.Label(root, font="Helvetica, 18")
temperature_label.pack(pady=3)

# Label widget -> to show the weather description 
description_label = tk.Label(root, font="Helvetica, 16")
description_label.pack(pady=3)

# Frame to hold the hourly forecast information
hourly_frame = ttkbootstrap.Frame(root)
hourly_frame.pack(pady=5)

# Frame to hold the 5-day forecast information
forecast_frame = ttkbootstrap.Frame(root)
forecast_frame.pack(pady=5)

# Automatically get the weather for the user's current location when the app opens
search_by_location()

root.mainloop()
