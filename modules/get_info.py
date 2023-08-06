import requests


def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # If the request was not successful

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
        return None

    data = response.json()

    # Now you can extract and use the data from the response
    # For example, print the name of the city and the current temperature:
    city_name = data["name"]
    temperature = data["main"]["temp"] - 273.15
    print(f"The current temperature in {city_name} is {temperature:.2f}°C")
