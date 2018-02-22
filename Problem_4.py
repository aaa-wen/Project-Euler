# determine if the number is palindrome
def palindrome(x):
	leng = len(str(x))
	x = str(x)
	i = 0
	while i < leng:
		if (x[i] != x[leng-1-i]):
			return False
		i += 1
	else:
		return True

j = 999
k = 999
ans = []

while j > 100:
	while k > 100:
		if (palindrome(j*k) == True):
			break
		k = k-1
	if(palindrome(j*k) == True):
		ans.append(j*k)
	j = j-1
	k = 999

ans.sort()
print (ans)