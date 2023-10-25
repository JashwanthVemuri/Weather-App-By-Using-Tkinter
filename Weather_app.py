import tkinter as tk
import requests

def weather():
    city_name = user_inp.get()
    Api_Key = "2606f769271b8d545fe3458b2b72ed9f"
    final_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city_name, Api_Key)
    try:
        result = requests.get(final_URL)
        data = result.json()
        if data.get("main"):
            temperature = str(data['main']['temp'])
            weather_condition = data['weather'][0]['main']
            pressure = data['main']['pressure']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
        
            result_label.config(text=f"Weather in {city_name}:\n"
                                      f"Temperature: {temperature}°C\n"
                                      f"Humidity: {humidity}%\n"
                                      f"Pressure: {pressure} hPa\n"
                                      f"Condition: {weather_condition}\n"
                                      f"Wind Speed: {wind_speed} m/s")
        else:
            result_label.config(text="City not found. Please enter a valid city name.")

    except requests.exceptions.RequestException:
        result_label.config(text="Network error. Please check your internet connection.")


root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")  


user_label = tk.Label(text="City Name:")
user_inp = tk.Entry()
submit = tk.Button(text="Get Weather", command=weather)
Heading = tk.Label(root, text=" Weather Report", font=("Helvetica 16 underline"))

user_label.grid(row=0, column=1, padx=10, pady=10)
user_inp.grid(row=0, column=2, padx=10, pady=10)
submit.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
Heading.grid(row=3, column=0, columnspan=2)


result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)


root.mainloop()
