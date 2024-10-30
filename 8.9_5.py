percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps = []

for num in percent_rain:
    if num>90:
        resps.append("Bring an umbrella.")
    elif num>80:
        resps.append("Good for the flowers?")
    elif num>50:
        resps.append("Watch out for clouds!")
    else:
        resps.append("Nice day!")
        
print(resps)

