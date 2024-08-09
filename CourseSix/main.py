# Data Visualization 
import matplotlib.pyplot as plt
x_values = [1,2,3,4,5,6,7,8,9,10]
y_values = [1,4,6,8,10,12,14,16,18,20]

# line chart
plt.plot(x_values, y_values, color='green')
plt.xlabel("X-axis placeholder")
plt.ylabel("Y-axis placeholder")
plt.title("Title Placeholder")
plt.show()

# scatter plot
plt.scatter(x_values, y_values, color='green')
plt.xlabel("X-axis placeholder")
plt.ylabel("Y-axis placeholder")
plt.title("Title Placeholder")
plt.show()

 #bar chart
animals = ['cat','dog','horse', 'mouse']
animals_values = [10,20,30,5]
plt.bar(animals, animals_values, color='pink')
plt.xlabel("Animal")
plt.ylabel("Weight of an Animal")
plt.title("Weight of Animal")
plt.show()

# # histograms
import numpy as np
x_normal = np.random.normal(0,1,100)
plt.hist(x_normal, color = "skyblue")
plt.xlabel("X")
plt.ylabel("Frequency")
plt.title("Randomly Sampled Data from Standard Normal Distribution")
plt.legend()
plt.show()


from scipy.stats import norm
x_values = np.arange(-4,4,0.01)
y_values = norm.pdf(x_values)
counts, bins, ignored = plt.hist(x_normal, 30, density = True, color = "skyblue", label = "Sampling Distrubution")
plt.plot(x_values, y_values, color = 'y', linewidth = 2.5, label = "Population Distribution")
plt.xlabel("Randomly generating 1000 obs from Normal distribution mu =0 sigma = 1")
plt.ylabel("Probability")
plt.legend()
plt.show()