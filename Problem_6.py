numbers = [x for x in range(1,101)]
total1 = 0
total2 = 0
temp = 0

for i in numbers:
	total1 = total1 + i**2

for j in numbers:
	temp = temp + j
total2 = temp**2

ans = total2 - total1
print (ans)