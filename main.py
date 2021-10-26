class Calculator():
	def addition(self, a, b):
		return a + b

	def subtract(self, a, b):
		return a - b

	def mult(self, a, b):
		return a * b

	def division(self, a, b):
		return a / b


c = Calculator()

print(c.addition(1, 4))
print(c.subtract(6, 3))
print(c.mult(2, 3))
print(c.division(10, 5))

# end