import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Measures how far a set of numbers is spread out from their average
def variance(values, mean):
    return sum([(value - mean) ** 2 for value in values])

# Measure of the joint variability of two random variables
def covariance(x, mean_x, y , mean_y):
    covariance = 0.0
    for i in range(len(x)):
        covariance = covariance + (x[i] - mean_x) * (y[i] - mean_y)
    return covariance

def graph(data_set, x, y):
	plt.plot(data_set['km'], data_set['price'], 'o')
	plt.plot(x, y)
	plt.ylabel("Price")
	plt.xlabel("Km")
	plt.title('Value of cars depending on mileage')
	plt.show()

def main():
	data_set = pd.read_csv('data.csv')
	mean_mileage = sum(data_set['km']) / float(len(data_set['km']))
	mean_price = sum(data_set['price']) / float(len(data_set['price']))
	variance_mileage, variance_price = variance(data_set['km'], mean_mileage), variance(data_set['price'], mean_price)
	covariance_mileage_price = covariance(data_set['km'], mean_mileage, data_set['price'], mean_price)
	m = covariance_mileage_price / variance_mileage
	c = mean_price - m * mean_mileage
	theta = [c, m]
	np.savetxt("theta.csv", theta, delimiter = ',');
	x = data_set['km']
	y = m * x + c
	graph(data_set, x, y)

if __name__ == "__main__":
	main()