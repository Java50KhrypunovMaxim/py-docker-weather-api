import requests


def get_weather():
    api_key = "e366acb630e94d158a1132018251102"

    url = f"https://api.openweathermap.org/data/2.5/weather?q=Paris&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()

        if weather_data.get("cod") == 200:
            main = weather_data.get("main", {})
            weather = weather_data.get("weather", [{}])[0]

            temperature = main.get("temp")
            description = weather.get("description")

            print(f"Weather in Paris: {temperature}°C, {description}.")
        else:
            print(f"Error: {weather_data.get('message')}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")


if __name__ == "__main__":
    get_weather()
