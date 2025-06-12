import requests

# API URL with your valid API key
url = "https://api.openweathermap.org/data/2.5/weather?q=Karachi&appid=68cc89c377246b951408f003645a1137&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    print(f"The current temperature in Karachi is {temp}°C")
else:
    print("Failed to fetch data. Status Code:", response.status_code)
