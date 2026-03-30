import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "ethicszero015@gmail.com"
MY_PASSWORD = "wvlp xppf dhul tptm"
MY_LAT = 22.975084 # Your latitude
MY_LONG = 88.434509 # Your longitude
MSG = "Hey, it's night time & I'm over your head. Look at me, you can see me now.❤ from ISS."

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

def mail_sender():
    if (iss_latitude <= (MY_LAT + 5) or iss_latitude >= (MY_LAT - 5)
            and iss_longitude <= (MY_LONG + 5) or iss_longitude >= (MY_LONG - 5)
            and time_now.hour > sunset or time_now.hour < sunrise):
        while True:
            time.sleep(60)
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="noobxpro025@gmail.com",
                    msg=f"Subject:ISS Overhead Notify!\n\n{MSG}")
    else:
        print("ISS: Coming soon!")


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

mail_sender()


