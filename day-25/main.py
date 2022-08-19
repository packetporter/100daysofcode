import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# temp_max = data[data.temp == data.temp.max()]
# monday = data[data.day == "Monday"]
# monday_temp_fah = (int(monday.temp) * 9/5) + 32
# print(monday_temp_fah)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_Data.csv")
# gray_squirrel = data[data["Primary Fur Color"] == "Gray"].count()
colors = data["Primary Fur Color"].value_counts()
new_data = pandas.DataFrame(colors)

new_data.to_csv("squirrel_color_count.csv")