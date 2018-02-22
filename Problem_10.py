def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

ans = 0
i = 2
while i < 2000000:
	if (isPrime(i)):
		ans = ans+i
		print (ans)
	i = i+1

print ("the answer is:")
print (ans)