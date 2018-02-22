test_number = 600851475143
numbers = [x for x in range(1, int((test_number)**0.5))]
factor = []
ans = 0

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


for i in numbers:
	if (test_number % i == 0):
		factor.append(i)

for j in factor:
	if (prime(j)):
		ans = j

print (ans)

