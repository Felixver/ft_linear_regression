import numpy as np
import os.path
from termcolor import colored

def main():
	if (os.path.exists("theta.csv") == True):
		theta = np.loadtxt("theta.csv", dtype = np.longdouble, delimiter = ',')
		try:
			x = np.longdouble(input("What's the mileage of your car: "))
		except:
			print ("Error, please fill in a correct number")
			exit()
		if (theta.any):
			estimate = theta[0] + theta[1] * x
			print (estimate)
	else:
		print (colored("No theta.csv file. You have to run the computation before making predictions.", "red"))

if __name__ == "__main__":
	main()
