#File: chaos.py
#A simple program, printing chaos

def main():
	print("This program illustrates chaotic behavior.")
	x = eval(input("Enter a number betweek 0 and 1: "))
	for i in range(10):
		x = 3.9 * x * (1-x)
		print(x)

main()

