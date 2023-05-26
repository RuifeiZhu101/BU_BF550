#File: chaos.py
#A simple program, printing chaos

def main(x):
	print("This program illustrates chaotic behavior.")
	a=[]
	for i in range(10):
		x = 3.9 * x * (1-x)
		#print(x)
		a.append(x)
	return a



