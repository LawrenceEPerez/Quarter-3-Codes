names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

print("Step Count Dataset (Monday–Friday):")
for i in range(len(steps)):
    print(names[i] + ":", steps[i])

totals = []

for i in range(len(steps)):
    total_steps = sum(steps[i])
    totals.append(total_steps)
    print(names[i], "total steps:", total_steps)

highest = max(totals)
lowest = min(totals)

top_person = names[totals.index(highest)]

print("Top performer:", top_person)
print("Highest total steps:", highest)
print("Difference between highest and lowest:", highest - lowest)
