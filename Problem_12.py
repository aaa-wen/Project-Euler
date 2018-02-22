import math
i = 1
tri = 0

def factors(n):
    results = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            results.add(i)
            results.add(int(n/i))
    return results

while (1):
	tri = tri + i
	if (len(factors(tri)) >= 500):
		break
	i = i+1

print ("the first triangle number that has over 500 divisors:", tri)

