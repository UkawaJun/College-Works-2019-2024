def sum(n):
	sums  = 0
	for a  in range(1,n+1):
		sums += a
	return sums
sum0 = 0
for i in range(1,31):
	sum0 += sum(i)
print(sum0)