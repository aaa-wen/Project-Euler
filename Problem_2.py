x1 = 1
x2 = 2
Fibonacci = [x1, x2]
ans = 0 
while x2 < 4000000:
	temp = x2
	x2 = x1 + x2
	x1 = temp
	Fibonacci.append(x2)

for i in Fibonacci:
	if (i % 2 == 0):
		ans += i

print (ans)