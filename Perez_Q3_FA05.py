names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

daily_totals = []

for col in range(len(steps[0])):
    day_total = 0
    for row in range(len(steps)):
        day_total += steps[row][col]
    daily_totals.append(day_total)
    print(days[col], "total steps:", day_total)

most_active_day = days[daily_totals.index(max(daily_totals))]

print("\nMost active day overall:", most_active_day)
