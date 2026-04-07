import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

stock_parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}


response = requests.get(url=STOCK_ENDPOINT, params=stock_parameter)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_or_down = None
if difference > 0:
    up_or_down = "🔺"
else:
    up_or_down = "🔻"

diff_percentage = round((difference / float(yesterday_closing_price)) * 100)

if abs(diff_percentage) > 5:
    news_parameter = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
    articles = news_response.json()["articles"]
    three_article = articles[:3]

    formatted_articles = [f"{STOCK_NAME}: {up_or_down}{diff_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_article]
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=os.getenv("TWILIO_PHONE_NUMBER"),
            to=os.getenv("SEND_TO_PHONE_NUMBER")
        )


