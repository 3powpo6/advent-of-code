input = open("input", "r")
total = 0
calories = []
for x in input:
	if len(x.strip()) != 0:
		total += int(x)
	else:
		calories.append(total)
		total = 0	
calories.sort(reverse = True)
print("Top Elf carries", calories[0], "calories")
print("Top 3 Elfs carry", sum(calories[0:3][:3]), "calories")