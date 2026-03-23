import smtplib
import datetime as dt
import random


# ---------- DATE & TIME ---------- #
now = dt.datetime.now()
date = now.date()
time = now.time()
weekday = now.weekday()

# ---------- FILE ---------- #
with open("quotes.txt") as file:
    data = file.readlines()

# ---------- RANDOM QUOTE ---------- #
random_quote = random.choice(data)

# ---------- EMAIL SENDER ---------- #
sender_email = "ethicszero015@gmail.com"
sender_pass = "wvlp xppf dhul tptm"
if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_pass)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs="sharmashubhajit025@gmail.com",
            msg=f"Subject:Daily Motivational Quote.\n\n{random_quote}"
        )
