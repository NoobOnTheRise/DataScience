""" Descriptive statistics refers to a branch of statistics that involves
       * summarizing, 
       * organizing, and 
       * presenting data meaningfully and concisely. 
    It focuses on describing and analyzing a dataset's main features and 
    characteristics without making any generalizations or inferences to a larger population.
"""
import numpy as np
from scipy import stats
import pandas as pd

data  = [100, 20, 5,20,45,-100,46]

mean_ = np.mean(data)
print("Mean of array: ", mean_)

median_ = np.median(data)
print("Median of array: ", median_)

mode_ = stats.mode(data)
print("Mode of array: ", mode_)

variance_ = np.var(data)
std = np.std(data)
print("Variance of array: ", variance_)
print("Std Deviation of array: ", std)

data_csv = pd.read_csv("./percent-bachelors-degrees-women-usa.csv")
print(data_csv)
print(data_csv.describe())
