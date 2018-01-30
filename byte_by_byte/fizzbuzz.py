print('importing fizz buzz')


def fizzbuzz(n):
	try:
		if n < 1 or not isinstance(n, int):
			raise ValueError

		for i in range(1, n+1):
			if i % 3 == 0 and i % 5 == 0:
				print("FizzBuzz")
			elif i % 3 == 0:
				print("Fizz")
			elif i % 5 == 0:
				print("Buzz")
			else:
				print(i)
	except ValueError:
		print('Only integers greater than 1')


if __name__ == "__main__":
    n = 15
    print(fizzbuzz(n))
