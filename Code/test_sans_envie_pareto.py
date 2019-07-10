import sys
def possible(n, x, m):
	test = True
	for i in range(1,101):
		for j in range (1,101):
			nx = (i*2*m + n) * (j*2*m + x)
			n_ = i*2*m + n
			q = nx//m
			r = nx%m
			sum_ci = 0
			for k in range (1, q + 1):
				sum_ci += k
			sum_ci *= m
			sum_ci += r * (q + 1)
			r_n = sum_ci % n_
			if r_n != 0:
				test = False
	return test

for m in range(2, 4):
	print("m =",m)
	for n in range(1, 2*m + 1):
		for x in range(1, 2*m + 1):
			print("n =",str(2*m)+"p +", n)
			print("x =",str(2*m)+"k +", x)
			print(possible(n, x, m))
			print()
			
