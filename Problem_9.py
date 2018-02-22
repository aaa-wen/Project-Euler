a = 1
b = 1
ans = []

while a < 1000:
	for i in range(1, 1000):
		if ((a**2 + i**2) == (1000-(a+i))**2):
			ans.append(a)
			ans.append(i)
			ans.append(1000-a-i)
	if (len(ans)):
		break
	else:
		a = a+1

print (ans)
print (ans[0]*ans[1]*ans[2])

