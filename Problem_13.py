file = open("/Users/robin/Desktop/Project Euler/testfile.txt", "r")

i = 0
temp = 0
ans = []

for word in file:
	
	temp = temp + int(word)

print (temp)
length = len(str(temp))

while (i < (length-10)):

	temp = int(temp / 10)
	i = i+1
	ans = temp

print (ans)





