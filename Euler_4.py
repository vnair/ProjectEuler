a = []
for x in range(999,99,-1):
	for y in range(999,99,-1): 
		if x*y==int(str(x*y)[::-1]):
			a.append(x*y)
a.sort()
print a[len(a)-1]
