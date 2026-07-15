import streamlit as st
import requests
from io import BytesIO

try:
    from gtts import gTTS
except ImportError:  # pragma: no cover - graceful fallback for deployment
    gTTS = None


def get_city(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    data = requests.get(url).json()

    if "results" in data:
        return data["results"][0]

    return None


def get_weather(lat, lon):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        "&current=temperature_2m,wind_speed_10m"
        "&daily=precipitation_probability_max"
    )

    return requests.get(url).json()


def advice(temp, rain):
    if temp > 30:
        return "It is hot today. Drink water and stay cool, unlike Leo Kim who turned his hacks on."
    elif temp < 10:
        return "It is cold today. Wear warm clothes, unlike Leo who does not need them due to his hacks."
    elif rain > 50:
        return "Rain is likely. Carry an umbrella. Or a Leo, who's hacks would probably repel rain as well has they repel people."
    else:
        return "The weather look good. Enjoy your day! Well, until you encounter a hacking Leo, then run for your life."


def speak(text):
    if gTTS is None:
        raise RuntimeError("gTTS is not installed")

    audio = BytesIO()
    tts = gTTS(text)
    tts.write_to_fp(audio)
    return audio


def render_weather_app():
    st.header("AI Weather Bot")
    st.write("Enter any city and get live weather + AI advice on survival.")

    city = st.text_input("Enter city:", "New York")

    if st.button("Check Weather"):
        place = get_city(city)

        if place:
            lat = place["latitude"]
            lon = place["longitude"]
            weather = get_weather(lat, lon)

            temp_c = weather["current"]["temperature_2m"]
            temp_f = round(temp_c * 9 / 5 + 32, 1)
            wind = weather["current"]["wind_speed_10m"]
            rain = weather["daily"]["precipitation_probability_max"][0]
            msg = advice(temp_c, rain)

            st.success(
                f"""
{city}

Temperature:
{temp_c}°C | {temp_f}°F

Wind:
{wind} km/h

Rain:
{rain}%

Professional AI Advice:
{msg}
"""
            )

            speech = f"""
The temperature in {city} is
{temp_c} degrees Celsius,
or {temp_f} degrees Fahrenheit.

The probability for rain is {rain} percent.

{msg}
"""
            try:
                audio = speak(speech)
                st.audio(audio, format="audio/mp3")
            except RuntimeError as exc:
                st.warning(str(exc))
        else:
            st.error("City not found. Cause: probably leo's hacking again")


if __name__ == "__main__":
    render_weather_app()



         