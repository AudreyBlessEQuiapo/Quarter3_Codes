steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200] 
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
daily_totals = []

for col in range(5):
    day_sum = 0

    for person_steps in steps:
        day_sum += person_steps[col]
    
    daily_totals.append(day_sum)
    print(f"{days[col]} Total: {day_sum}")

max_steps = max(daily_totals)
best_day = days[daily_totals.index(max_steps)]

print(f"\nThe most active day overall was {best_day} with {max_steps} total steps.")
