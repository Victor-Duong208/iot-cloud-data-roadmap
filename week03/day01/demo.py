from src.utils_math import mean, to_celsius, categorize_temp

temps_f = [77, 80.6, 86, 95]
temps_c = [to_celsius(t) for t in temps_f]
print("Celsius:", [round(t, 2) for t in temps_c])
print("Mean C:", round(mean(temps_c), 2))
print("Tag:", categorize_temp(mean(temps_c)))
