step_counts = [
    [4500, 5200, 4800, 5500, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200] 
]

for i, steps in enumerate(step_counts):

    total = sum(steps)
    avg = total / len(steps)
    min_steps = min(steps)
    max_steps = max(steps)

    print(f"Friend {i+1} - Total Steps: {total} Average: {avg} Min: {min_steps} Max: {max_steps}")
