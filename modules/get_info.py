import requests


def get_weather(api_key, city):

    if not api_key or not city:
        print("API key and city name must not be empty.")
        return

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        city_name = data["name"]
        temperature = data["main"]["temp"] - 273.15
        print(f"The current temperature in {city_name} is {temperature:.2f}°C")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    except ValueError:
        print("Decoding JSON has failed")
    except KeyError:
        print("Invalid city name. Please check your spelling and try again.")
