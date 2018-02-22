def Fibonacci(x):

	if (x == 1):
		return 1

	elif (x == 2):
		return 1

	else:
		return Fibonacci(x-1) + Fibonacci(x-2)

i = 3
length = 0

length = len(str(Fibonacci(100)))

print (length)



