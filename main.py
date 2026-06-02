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

# plt.bar(df["math score"].value_counts().index, df["math score"].value_counts().values)
# plt.grid(axis="y",linestyle="dotted",linewidth=1)
# plt.grid(axis="x",linestyle="dotted",linewidth=1)
# plt.title("Math Scores Distribution",fontsize=15,fontweight="bold")
# plt.xticks(np.arange(0,101,5), rotation="vertical", fontsize=8)
# plt.yticks(np.arange(0,41,5), rotation="vertical", fontsize=8)
# plt.xlabel("Students Scores", fontweight="bold")
# plt.ylabel("Amount of Student", fontweight="bold")
# plt.subplots_adjust(bottom=0.05,right=0.95,top=0.95,left=0.05)
# print(df["math score"].value_counts())

read_mean = np.mean(df["reading score"])
read_median = np.median(df["reading score"])
read_std = np.std(df["reading score"])
print("READING SCORE")
print(f"Mean: {read_mean}")
print(f"Median: {read_median}")
print(f"Standard Deviation: {read_std}\n")

# plt.bar(df["reading score"].value_counts().index, df["reading score"].value_counts().values)
# plt.grid(axis="y",linestyle="dotted",linewidth=1)
# plt.grid(axis="x",linestyle="dotted",linewidth=1)
# plt.title("Reading Scores Distribution",fontsize=15,fontweight="bold")
# plt.xticks(np.arange(0,101,5), rotation="vertical", fontsize=8)
# plt.yticks(np.arange(0,41,5), rotation="vertical", fontsize=8)
# plt.xlabel("Students Scores", fontweight="bold")
# plt.ylabel("Amount of Student", fontweight="bold")
# plt.subplots_adjust(bottom=0.08,right=0.95,top=0.95,left=0.05)
# print(df["reading score"].value_counts())

wrt_mean = np.mean(df["writing score"])
wrt_median = np.median(df["writing score"])
wrt_std = np.std(df["writing score"])
print("WRITING SCORE")
print(f"Mean: {wrt_mean}")
print(f"Median: {wrt_median}")
print(f"Standard Deviation: {wrt_std}\n")

# plt.bar(df["writing score"].value_counts().index, df["writing score"].value_counts().values)
# plt.grid(axis="y",linestyle="dotted",linewidth=1)
# plt.grid(axis="x",linestyle="dotted",linewidth=1)
# plt.title("Writing Scores Distribution",fontsize=15,fontweight="bold")
# plt.xticks(np.arange(0,101,5), rotation="vertical", fontsize=8)
# plt.yticks(np.arange(0,41,5), rotation="vertical", fontsize=8)
# plt.xlabel("Students Scores", fontweight="bold")
# plt.ylabel("Amount of Student", fontweight="bold")
# plt.subplots_adjust(bottom=0.08,right=0.95,top=0.95,left=0.05)
# print(df["writing score"].value_counts())

subjects = [
    "math score",
    "reading score",
    "writing score"
]
best_subject = {
    "math": math_mean,
    "reading": read_mean,
    "writing": wrt_mean,
}



best_mean = max(best_subject.values())

print(f"Best Subject: {[k for k,v in best_subject.items() if v==best_mean]}")
print(f"Best Mean: {best_mean}")

# math_counts = df["math score"].value_counts().sort_index()
# reading_counts = df["reading score"].value_counts().sort_index()
# writing_counts = df["writing score"].value_counts().sort_index()
#
# plt.figure(figsize=(12,6))
#
# plt.plot(
#     math_counts.index,
#     math_counts.values,
#     marker="o",
#     label="Math"
# )
#
# plt.plot(
#     reading_counts.index,
#     reading_counts.values,
#     marker="o",
#     label="Reading"
# )
#
# plt.plot(
#     writing_counts.index,
#     writing_counts.values,
#     marker="o",
#     label="Writing"
# )
# plt.subplots_adjust(bottom=0.08,right=0.95,top=0.95,left=0.05)
#
# plt.title("Score Distribution by Subject", fontweight="bold", fontsize=12)
# plt.legend()
# plt.xlabel("Score")
# plt.ylabel("Number of Students")
#
# plt.legend()
# plt.grid(True)


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

# colors = [
# "#E57373" ,  # F - Soft Red
# "#FFB74D",  # D - Orange
# "#FFD54F",  # C - Yellow
# "#66BB6A",  # B - Light Green
# "#2E8B57",  # A - Sea Green
# ]
# plt.pie(grade_counts.values, labels=grade_counts.index, autopct='%1.1f%%', colors=colors)
# plt.title(
#     "Grade Distribution of Students",
#     fontsize=16,
#     fontweight="bold"
# )
#
# plt.legend(
#     title="Grades",
#     loc="upper right"
# )


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

plt.show()