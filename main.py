import pandas

data_file = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240217.csv")

print(data_file["Primary Fur Color"])

squirrel_dict = {
    "Color": ["Gray", "Cinnamon", "Black"],
    "Count": [0,0,0]

}

gray_squirrels = data_file[data_file["Primary Fur Color"] == "Gray"]
gray_count = len(gray_squirrels)
squirrel_dict["Count"][0] = gray_count

cinnamon_squirrels = data_file[data_file["Primary Fur Color"] == "Cinnamon"]
cinnamon_count = len(cinnamon_squirrels)
squirrel_dict["Count"][1] = cinnamon_count

black_squirrels = data_file[data_file["Primary Fur Color"] == "Black"]
black_count = len(black_squirrels)
squirrel_dict["Count"][2] = black_count



df = pandas.DataFrame(squirrel_dict)
df.to_csv("Fur_Color_Squirrel_Count")