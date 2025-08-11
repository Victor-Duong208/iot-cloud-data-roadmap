from src.utils_math import mean, to_celsius, categorize_temp, moving_average, normalize

temps_f = [77, 80.6, 86, 95]
temps_c = [to_celsius(t) for t in temps_f]
print("Celsius:", [round(t, 2) for t in temps_c])
print("Mean C:", round(mean(temps_c), 2))
print("Tag:", categorize_temp(mean(temps_c)))

print("MA(3):", [round(x,2) for x in moving_average(temps_c, 3)])
print("Norm:", [round(x,2) for x in normalize(temps_c)])
