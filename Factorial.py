def fact(x: int) -> int:
	if x == 1:
		return 1
	else:
		return fact(x-1) * x
	# ret = 1 if x == 1 else fact(x-1)
	# print(ret)
	# return ret

print(fact(5))
print(fact(10))