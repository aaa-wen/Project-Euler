def factorial(x):
	if (x == 1):
		return 1
	else:
		return x*factorial(x-1)

test = factorial(100)
test = str(test)

ans = sum([int(i) for i in test])
print (ans)