#! /usr/bin/env python

def gcd_euclid_algorithm(m,n):
	if n > m:
		n, m = m, n
	r = None

	while True:
		r = m % n
		if r == 0:
			return n
		m = n
		n = r

	return 1

def main():
	m = 119
	n = 544
	gcd = gcd_euclid_algorithm(m,n)
	print(gcd)

	m = 11
	n = 5
	gcd = gcd_euclid_algorithm(m,n)
	print(gcd)
	
	return 0

if __name__ == '__main__':
	main()
