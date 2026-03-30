import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()["iss_position"]
# longitude = data["longitude"]
# latitude = data["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

MY_LAT = 22.944101
MY_LNG = 88.433502

parameter = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted" : 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[1]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(data)
print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")

time_now = datetime.now()
print(time_now.hour)

