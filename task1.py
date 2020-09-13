from math import sqrt

dim = int(input("Enter dim:"))
amicable = {}


def div_sum(numb):
	res = 0
	for i in range(2, int(sqrt(numb))+1):
		if numb % i == 0:
			if i == numb//i:
				res += i
			else:
				res += (i + numb//i)
	return res + 1


for i in range(1, dim+1):
	amic = div_sum(i)
	if i == div_sum(amic) and i != amic:
		if i and amic not in amicable:
			amicable[i] = amic

print(amicable)
