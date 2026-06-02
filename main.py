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
best_subject = {
    "math score": math_mean,
    "reading score": read_mean,
    "writing score": wrt_mean,
}

best_mean = max(best_subject.values())

print(f"Best Subject: {best_subject}")
print(f"Best Mean: {best_mean}")

for subject in subjects:

    highest = df[subject].max()
    lowest = df[subject].min()

    print(f"\n{subject.upper()}")

    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")



def get_grade(score):

    if score >= 90:
        return "A"

    elif score >= 80:
        return "B"

    elif score >= 70:
        return "C"

    elif score >= 60:
        return "D"

    else:
        return "F"

df["Grade"] = df["math score"].apply(get_grade)

grade_counts = df["Grade"].value_counts()

print(grade_counts)

grade_percentages = (
    df["Grade"]
    .value_counts(normalize=True)
    * 100
)

for grade, percentage in grade_percentages.items():

    print(f"{grade}: {percentage:.1f}%")

math_reading = np.corrcoef(
    df["math score"],
    df["reading score"]
)[0, 1]

math_writing = np.corrcoef(
    df["math score"],
    df["writing score"]
)[0, 1]

reading_writing = np.corrcoef(
    df["reading score"],
    df["writing score"]
)[0, 1]

print("\nCORRELATION ANALYSIS")
print("--------------------")

print(f"Math ↔ Reading: {math_reading:.2f}")
print(f"Math ↔ Writing: {math_writing:.2f}")
print(f"Reading ↔ Writing: {reading_writing:.2f}")

print("\nINTERPRETATION")
print("--------------")

if reading_writing > 0.9:
    print("Students who read well usually write well.")

if math_reading > 0.7:
    print("Students who perform well in math often perform well in reading.")