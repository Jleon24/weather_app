import requests # library to make HTTP requests
import tkinter as tk # library for GUI
from tkinter import messagebox # for pop up box

def get_weather():
    # retrieve the city name entered by user
    city = city_entry.get()
    if city:
        # api key from openweathermap
        api_key = "a6cefb191645af45f5d20a5cf3685080"  
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"  # Changed to 'metric' for Celsius
        
        try:
            # send a GET request to the openweathermap api
            response = requests.get(url)
            # parse JSON response
            data = response.json()
            
            #check if the response is successful
            if data["cod"] == 200:
                # get data from the response
                city_name = data["name"]
                temp = data["main"]["temp"]
                weather_desc = data["weather"][0]["description"]
                humidity = data["main"]["humidity"]
                wind_speed = data["wind"]["speed"]
                
                # formate the information to display
                result = f"City: {city_name}\nTemperature: {temp}°C\nWeather: {weather_desc}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
                weather_label.config(text=result)
            else:
                # error message if the city not found
                messagebox.showerror("Error", f"City '{city}' not found!")
        except Exception as e:
            # error message if there is an issue with the request
            messagebox.showerror("Error", "Failed to retrieve data. Please check your connection.")
    else:
        # warning if the user entered non city name
        messagebox.showwarning("Input Required", "Please enter a city name.")

# GUI setup using tkinter
root = tk.Tk()
root.title("Weather App")

# create city label
city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=10)

#create city entry field
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

# Button to get weather
get_weather_btn = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_btn.pack(pady=10)

# Label for weather result
weather_label = tk.Label(root, text="", font=("Courier New", 12))
weather_label.pack(pady=20)

# Run
root.mainloop()
