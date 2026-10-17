#This program uses matplot library

import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 15, 25, 30])

# Create a figure with 5 subplots
plt.figure(figsize=(12, 8))

# 1. Line Plot
plt.subplot(2, 3, 1)
plt.plot(x, y, color='blue', marker='o', linestyle='-')
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

# 2. Scatter Plot
plt.subplot(2, 3, 2)
plt.scatter(x, y, color='red', marker='o')
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

# 3. Box Plot
plt.subplot(2, 3, 3)
data = [12, 15, 14, 10, 18, 20, 15, 16, 14, 13]
plt.boxplot(data)
plt.title("Box Plot")
plt.ylabel("Values")
plt.grid(True, axis='y')

# 4. Bar Chart
plt.subplot(2, 3, 4)
subjects = ['Math', 'Science', 'English', 'Computer']
marks = [85, 90, 78, 95]
plt.bar(subjects, marks, color='green')
plt.title("Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.xticks(rotation=15)

# 5. Pie Chart
plt.subplot(2, 3, 5)
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 25, 20, 15]
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        startangle=90)
plt.title("Pie Chart")

# Adjust spacing and display all graphs
plt.tight_layout()
plt.show()
