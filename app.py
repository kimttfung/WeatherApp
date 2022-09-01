from cProfile import label
import tkinter as tk
import requests

API_KEY = "<Enter Your OpenWeatherMap API Key>"

LARGE_FONT = ("Arial", 40, "bold")
MEDIUM_FONT = ("Arial", 20)
SMALL_FONT = ("Arial", 15)
BG_COLOR = "#9fd4f5"


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.search_bar = tk.Entry(font = MEDIUM_FONT, justify = "center")
        self.search_bar.pack(pady = 30)


        self.label_img = tk.Label(bg = BG_COLOR)
        self.label_img.pack()

        self.label1 = tk.Label(font = LARGE_FONT, text = "", bg = BG_COLOR)
        self.label1.pack()

        self.label2 = tk.Label(font = MEDIUM_FONT, text = "", bg = BG_COLOR)
        self.label2.pack()

        self.label3 = tk.Label(font = SMALL_FONT, text = "", bg = BG_COLOR)
        self.label3.pack(pady = 20)

        self.entry = tk.StringVar()
        self.entry.set("Enter Location")
        self.search_bar["textvariable"] = self.entry

        self.search_bar.bind('<Key-Return>', self.collect_data)

    def collect_data(self, event):
        location = (self.entry.get()).lower()
        response = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + API_KEY
        data = requests.get(response).json()
        condition = data["weather"][0]["description"].title()
        temperature = str(int(data["main"]["temp"] - 273.15))
        temp_min = str(int(data["main"]["temp_min"] - 273.15))
        temp_max = str(int(data["main"]["temp_max"] - 273.15))
        pressure = str(data["main"]["pressure"]) #hPA
        humidity = str(data["main"]["humidity"]) #%
        wind_speed = str(data["wind"]["speed"]) #m/s
        visibility = str(float(data["visibility"]/1000))[:4]

        icon = data["weather"][0]["icon"]
        asset = tk.PhotoImage(file = "./images/" + icon + "@2x.png")
        self.label_img.config(image = asset, bg = BG_COLOR)
        self.label_img.image = asset

        info1 = temperature + "°C"
        self.label1.config(text = info1, bg = BG_COLOR)

        info2 = condition
        self.label2.config(text = info2, bg = BG_COLOR)

        info3 = "temp range: " + temp_min + "°C - " + temp_max + "°C\n" + "pressure: " + pressure + " hPA\n" + "humidity: " + humidity + "%\n" + "wind: " + wind_speed + " m/s\n" + "visibility: " + visibility + " km"
        self.label3.config(text = info3, bg = BG_COLOR)

        pass

    def print_entry(self, event):
        print("The current location entry is:", self.entry.get())

root = tk.Tk()
root.geometry("350x450")
root.title("Weather App")
root.configure(bg = BG_COLOR)

weather_app = App(root)
weather_app.mainloop()