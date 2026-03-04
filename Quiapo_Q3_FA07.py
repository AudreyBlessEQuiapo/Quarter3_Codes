step_data = [
    [4500, 5200, 4800, 5000, 5300], # Me
    [4000, 4100, 3900, 4200, 4600], # Lia
    [6000, 5800, 5900, 6100, 6200]  # Jake
]

names = ["Me", "Lia", "Jake"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

print("Weekly Fitness Summary")

overall_max = 0

for i in range(len(step_data)):
    person_steps = step_data[i]
    name = names[i]

    total = sum(person_steps)
    average = total / len(person_steps)

    row_max = max(person_steps)
    if row_max > overall_max:
        overall_max = row_max

    print(f"{name}'s Steps: {person_steps}")
    print(f"  > Total Steps: {total}")
    print(f"  > Daily Average: {average:.2f}")
    print("-" * 30)

print(f"Highest single-day step count recorded: {overall_max}")
