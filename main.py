import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')

df=df.fillna({"math score":0})
df=df.fillna({"writing score":0})
df=df.fillna({"reading score":0})

math_mean = np.mean(df["math score"])
math_median = np.median(df["math score"])
math_std = np.std(df["math score"])
print("MATH SCORE")
print(f"Mean: {math_mean}")
print(f"Median: {math_median}")
print(f"Standard Deviation: {math_std}\n")

read_mean = np.mean(df["reading score"])
read_median = np.median(df["reading score"])
read_std = np.std(df["reading score"])
print("READING SCORE")
print(f"Mean: {read_mean}")
print(f"Median: {read_median}")
print(f"Standard Deviation: {read_std}\n")

wrt_mean = np.mean(df["writing score"])
wrt_median = np.median(df["writing score"])
wrt_std = np.std(df["writing score"])
print("WRITING SCORE")
print(f"Mean: {wrt_mean}")
print(f"Median: {wrt_median}")
print(f"Standard Deviation: {wrt_std}\n")

subjects = [
    "math score",
    "reading score",
    "writing score"
]

for subject in subjects:

    highest = df[subject].max()
    lowest = df[subject].min()

    print(f"\n{subject.upper()}")

    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")

