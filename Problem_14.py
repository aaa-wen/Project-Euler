maximum = 0
ans = 0

for test in range(2, 1000000):

	i = test
	length = 0

	while (i != 1):

		if (i % 2 == 0):

			i = i / 2
			length = length + 1

		elif (i % 2 == 1):

			i = i * 3 + 1
			length = length + 1

	if (length > maximum):

		maximum = length
		ans = test

print (ans)
