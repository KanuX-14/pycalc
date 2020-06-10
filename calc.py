import sys

numberA = float(sys.argv[1])
numberB = float(sys.argv[3])
math = str(sys.argv[2])

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:

	if math in ('+','-','x','/'):
		if math == '+':
			print(numberA, '+', numberB, '=', add(numberA, numberB))
		elif math == '-':
                	print(numberA, '-', numberB, '=', subtract(numberA, numberB))
		elif math == 'x':
        	        print(numberA, 'x', numberB, '=', multiply(numberA, numberB))
		elif math == '/':
        	        print(numberA, '/', numberB, '=', divide(numberA, numberB))
		break
	else:
		print('Invalid input!')
