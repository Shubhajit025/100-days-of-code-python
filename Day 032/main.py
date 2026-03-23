# import smtplib
#
# my_email = "mail@gmail.com"
# password = "password"
#
# # Without 'with' keyword :
# # connection = smtplib.SMTP("smtp.gmail.com", port=587)
# # connection.starttls() # -> Securing the connection or encrypt the message
# # connection.login(user=my_email, password=password)
# # connection.sendmail(
# #     from_addr=my_email,
# #     to_addrs="mymail@yahoo.com",
# #     msg="Subject:Hello\n\nThis is the body of my email."
# # )
# # connection.close()
#
# # With 'with' - keyword:
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls() # -> Securing the connection or encrypt the message
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="mymail@yahoo.com",
#         msg="Subject:Hello Test 1\n\nThis is the body of my email for testing."
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()
if year == 2026:
    print("The AI Era.")

if month == 3:
    print("March")
print(now)
print(month)
print(day_of_the_week)

date_of_birth = dt.datetime(year=2002, month=02, day=10)
print(date_of_birth)
