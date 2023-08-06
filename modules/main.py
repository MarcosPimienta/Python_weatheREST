from get_info import get_weather


def main():

    api_key = input("Enter your OpenWeatherMap API key: ")
    city_name = input("Enter the city name you want the weather info: ")

    get_weather(api_key, city_name)


if __name__ == "__main__":
    main()
