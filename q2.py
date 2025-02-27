def in_fib(num):
	"""Checks whether a number is in Fibonacci sequence."""
	if num <= 0:
		return False
	if num <= 2:
		return True
	a0 = a1 = 1
	curr = 2
	while curr < num:
		a0 = a1
		a1 = curr
		curr = a0 + a1
	return curr == num

# Check all numbers from 0 to 99.
for i in range(100):
	if in_fib(i):
		print(i, end=' ')

# Output:
# 1 2 3 5 8 13 21 34 55 89