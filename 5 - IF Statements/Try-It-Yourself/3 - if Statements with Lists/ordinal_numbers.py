digits = list(i for i in range(1, 10))

for digit in digits:
	if digit == 1:
		print(f"{digit}st")
	elif digit == 2:
		print(f"{digit}nd")
	elif digit == 3:
		print(f"{digit}rd")
	else:
		print(f"{digit}th")
