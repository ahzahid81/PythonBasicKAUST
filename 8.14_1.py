rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"

rainfall_mi2 = rainfall_mi.split(",")

num_rainy_months = 0


for item in rainfall_mi2:
    if float(item)>3.0:
        num_rainy_months +=1

print(num_rainy_months)