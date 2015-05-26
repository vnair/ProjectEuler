# bring data from URL without copy and paste
import urllib2,re
page = urllib2.urlopen('https://projecteuler.net/problem=8')
data =  page.read()
exp = re.findall('([0-9]+)\\<br',data)
input = ''
for i in exp:
	input = input+i

# Now Solve the actual problem
# iterative solution

#initialize max

max_val = 0
max_array = ''

a_size = 13
for x in range(1,len(input)+1-a_size):
	y = input[x:x+a_size]
	s = 1
	for i in y:
		s = s*int(i)
	if s > max_val:
		max_array = y
		max_val = s
print max_val
