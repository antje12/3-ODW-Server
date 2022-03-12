from datetime import datetime

# Function for nth Fibonacci number
def Fibonacci(n):
	if n<=0:
		print("Incorrect input")
	# First Fibonacci number is 0
	elif n==1:
		return 0
	# Second Fibonacci number is 1
	elif n==2:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program
startTime = datetime.now()
print("Fibonacci nr: " + str(Fibonacci(35)))
endTime = datetime.now()
print("Time taken: " + str(endTime - startTime))
