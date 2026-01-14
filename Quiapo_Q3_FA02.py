 step_counts = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]  
]

jake_wednesday = step_counts[2][2]
print(f"Jake's steps on Wednesday: {jake_wednesday}")

print(f"My steps... {step_counts[0]}")

print("Updating my Thursday steps to 5500.")
step_counts[0][3] = 5500

print(f"My updated steps: {step_counts[0]}")
