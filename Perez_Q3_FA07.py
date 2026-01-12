temperatures = [
    [68, 70, 72, 71, 69, 67, 66],
    [75, 76, 77, 78, 77, 76, 75]
]

cities = ["New York", "Los Angeles"]

max_temp = temperatures[0][0]

for i in range(len(temperatures)):
    print(cities[i], temperatures[i])
    total = sum(temperatures[i])
    average = total / len(temperatures[i])
    print("Total:", total, "Average:", average)
    for temp in temperatures[i]:
        if temp > max_temp:
            max_temp = temp

print("Highest temperature recorded:", max_temp)
