import pyowm
from config import BOT_TOKEN, OWM_TOKEN

owm = pyowm.OWM(OWM_TOKEN)
mgr = owm.weather_manager()


def get_forecast(city):
    observation = mgr.weather_at_place(city)
    # forecast = mgr.forecast_at_place(city, country)
    weather = observation.weather
    temperature = weather.temperature('celsius')["temp"]
    wind = weather.wind()['speed']
    clouds = weather.clouds
    humidity = weather.humidity
    forecast = f"🏙 In {city} city is currently\n🌡️ {temperature}°C \n💨 {wind} m/s \n🌫️ {clouds} % \n💦 {humidity} %"
    return forecast
