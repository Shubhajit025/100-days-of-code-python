# with open("weather_data.csv") as data_file:
#     file = data_file.readlines()
#     print(file)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         row_2 = row[1] #🟢
#         if row_2 != "temp":
#             a = int(row_2)
#             temperature.append(a)
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# avg = sum(temp_list) / len(temp_list)
# print(avg)
# Calculate avg temp
# avg_of_temp = data["temp"].mean()
# print(avg_of_temp)

# find out max value in temp list or column, by using method
# done by me. may be this nlargest use for something else need to go through
# largest_num = data["temp"].nlargest(n=1)
# print(largest_num)

# by class
# largest_num = data["temp"].max()
# print(largest_num)

# get data in columns
# remember the data inside dara or csv file, should match exact same during calling it to.
# print(data["condition"])
# also we can use like this
# print(data.condition)

# Get data from row
# print(data[data.day == "Monday"])

# finding the Highest temp row in which day it happened
# high_temp = data.temp.max()
# highest_row =  data[data.temp == high_temp]
# print(highest_row)

# monday = data[data.day == "Monday"]
# temp_c = monday.temp[0]
# temp_f = (temp_c * 9/5) + 32
# print(temp_f)
# cel_to_frnht = (monday.temp * 9/5) + 32
# print(cel_to_frnht)

# '''Create a dataframe from scratch'''
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }
# # creating the dataframe from the data_dict 👇
# data = pandas.DataFrame(data_dict)
# # print(data)
# #creating a new csv file 👇
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260308.csv")
# data_new = pandas.DataFrame(data)
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
