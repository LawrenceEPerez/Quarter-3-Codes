temperatures = [
[72, 75, 73, 74, 76],
[68, 70, 69, 71, 72]
]


for i in range(len(temperatures)):
    print(f"City {i + 1} temperatures:", temperatures[i])
    total = sum(temperatures[i])
    average = total / len(temperatures[i])
    print("Total:", total)
    print("Average:", average)
    print()


max_temp = max(max(row) for row in temperatures)
min_temp = min(min(row) for row in temperatures)


print("Maximum temperature in dataset:", max_temp)
print("Minimum temperature in dataset:", min_temp)

# 2D array storing daily temperatures
temperatures = [
[72, 75, 73, 74, 76], # City A
[68, 70, 69, 71, 72] # City B
]
