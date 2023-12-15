#https://goheels.com/sports/mens-basketball/roster
import pandas as pd

player = {"Last Name": ["Bacot","Davis","Cadeau","High","Ryan","Trimble","Washington","Lebo","Landry","Farris","Ingram"],
          "First Name": ["Armando", "RJ", "Elliot","Zayden","Cormac","Seth","Jalen","Creighton","Rob","Duwe","Harrison"],
          "height": [83 ,72, 73, 81, 77, 75, 82, 73, 76, 79, 79],
          "weight": [240,180,180,225,195,195,230,180,190,210,235]
}

data = pd.DataFrame(player)

#bmi equals weight in kg/ height in meters squared
BMI = (data['weight']/2.205)/((data['height']/39.37)**2)
data["bmi"] = BMI.round(2)

print(data)

data.to_csv("bmi.csv")