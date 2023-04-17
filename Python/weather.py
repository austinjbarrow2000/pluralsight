import requests


def get_weather(city):
    api_key = "yo"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")
    return description, temp_min, temp_max


def main():
    city = "Philadelphia"
    description, temp_min, temp_max = get_weather(city)
    print(f"Today's forecast in {city} is {description}")
    print(f"The minimum temperature is {temp_min} degrees")
    print(f"The maximum temperature is {temp_max} degrees")


main()
