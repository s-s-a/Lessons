def hex_output():
	decnum = 0
	hexnum = input('Введите шестнадцатеричное число для преобразования: ')
	for power, digit in enumerate(reversed(hexnum)):
		decnum += int(digit, 16) * (16 ** power)
		print(decnum)

hex_output()
