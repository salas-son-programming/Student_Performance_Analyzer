# Student Performance Analyzer 📚

## Introduction

This project analyzes student exam performance using Python and some of the most popular data science libraries: Pandas, NumPy, and Matplotlib.

The goal of this project was not only to learn how to work with datasets, but also to practice extracting useful information from data and presenting it through visualizations.

The dataset contains student scores in three subjects:

* Math
* Reading
* Writing

Using these scores, I performed statistical analysis, grade classification, correlation analysis, and data visualization.

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib

---

# Project Objectives

The main objectives of this project were:

* Analyze student performance in different subjects
* Calculate important statistics
* Convert numerical scores into letter grades
* Visualize student performance
* Discover relationships between subjects
* Practice real-world data analysis techniques

---

# Dataset Information

The dataset contains 1000 student records and includes:

* Gender
* Race/Ethnicity
* Parental level of education
* Lunch type
* Test preparation course
* Math score
* Reading score
* Writing score

For this project, I focused mainly on the three exam scores.

---

# Statistical Analysis

Using NumPy, I calculated the mean, median, and standard deviation for each subject.

## Results

### Math

* Mean: 66.09
* Median: 66
* Standard Deviation: 15.16

### Reading

* Mean: 69.17
* Median: 70
* Standard Deviation: 14.59

### Writing

* Mean: 68.05
* Median: 69
* Standard Deviation: 15.19

## Interpretation

Reading had the highest average score among the three subjects.

The standard deviations are similar, which suggests that student performance varied by a comparable amount across all subjects.

---

# Highest and Lowest Scores

The program identifies:

* Highest score in each subject
* Lowest score in each subject

This helps highlight the range of student performance and detect exceptional results.

---

# Grade Distribution

I created a grading system based on the students' math scores.

| Score Range | Grade |
| ----------- | ----- |
| 90 - 100    | A     |
| 80 - 89     | B     |
| 70 - 79     | C     |
| 60 - 69     | D     |
| Below 60    | F     |

The program calculates the percentage of students in each grade category and displays the results in a pie chart.

## Visualization

The pie chart uses colors that represent performance levels:

* A → Green
* B → Light Green
* C → Yellow
* D → Orange
* F → Red

This makes the distribution easy to understand at a glance.

---

# Correlation Analysis

One of the most interesting parts of this project was studying the relationship between subjects.

Using NumPy's correlation functions, I calculated:

* Math ↔ Reading
* Math ↔ Writing
* Reading ↔ Writing

## Findings

The strongest relationship was between Reading and Writing.

This suggests that students who perform well in reading tend to perform well in writing.

This was my first introduction to a concept that is widely used in Machine Learning and Data Science.

---

# Visualizations

The project includes several visualizations created with Matplotlib:

### Grade Distribution Pie Chart

Shows the percentage of students receiving each letter grade.

### Subject Score Distributions

Compares score distributions across:

* Math
* Reading
* Writing

### Correlation Analysis

Helps visualize the relationship between different subjects and understand how performance in one subject relates to another.

---

# Key Insights

After analyzing the dataset, I found that:

* Reading had the highest average score.
* Reading and Writing were strongly correlated.
* Student performance varied significantly across all subjects.
* A large percentage of students received grades D and F compared to grade A.

These findings demonstrate how data can be used to better understand academic performance.

---

# What I Learned

This project helped me improve my skills in:

* Data cleaning
* Data analysis
* Statistical calculations
* Data visualization
* Python programming
* Pandas
* NumPy
* Matplotlib
* Interpreting results and drawing conclusions from data

It also gave me experience working with a real dataset and turning raw numbers into meaningful insights.

---

# Future Improvements

Possible future improvements include:

* Interactive dashboards using Streamlit
* Machine Learning models to predict student performance
* Additional visualizations
* Analysis based on gender and parental education
* Predicting final grades from exam scores

---

# Author

Yaniss Bantse

Computer Engineering Student

This project is part of my journey toward becoming an AI Engineer and strengthening my skills in Data Science and Machine Learning.
