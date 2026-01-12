temperatures = [
[72, 75, 73, 74, 76],
[68, 70, 69, 71, 72]
]

print(temperatures)

print("City B temperature on Wednesday:", temperatures[1][2])


temperatures[0][3] = 78
print("Updated City A temperatures:", temperatures[0])


avg_city_b = sum(temperatures[1]) / len(temperatures[1])
print("Average temperature for City B:", avg_city_b)

# 2D array storing daily temperatures
temperatures = [
[72, 75, 73, 74, 76], # City A
[68, 70, 69, 71, 72] # City B
]
