def prime(x):
	if (x == 1):
		return False
	i = 2
	while i < x:
		if (x % i == 0):
			return False
		i = i+1
	else:
		return True

x = 2
count = 0
while count < 10001:
	print (x)
	if (prime(x) == True):
		x += 1 
		print (x)
		count += 1
		print (count)
	else:
		x += 1

print (x)