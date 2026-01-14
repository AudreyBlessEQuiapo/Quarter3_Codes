names = ["Me", "Lia", "Jake"]
steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200] 
]

totals = [sum(person_steps) for person_steps in steps]

highest_total = max(totals)
lowest_total = min(totals)
top_person = names[totals.index(highest_total)]

print(f"The person with the highest total steps is {top_person} with {highest_total} steps.")
print(f"Difference between highest and lowest total: {highest_total - lowest_total}")
