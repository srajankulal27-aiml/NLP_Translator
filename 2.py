import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Iris dataset (offline)
iris = load_iris(as_frame=True)

# Create DataFrame
d = iris.frame

# Rename columns
d.columns = ['sepal_length', 'sepal_width',
             'petal_length', 'petal_width', 'species']

# Correlation
print("Pearson Correlation:\n")
print(d[['sepal_length', 'petal_length']].corr())

# Covariance
print("\nCovariance Matrix:\n")
print(d[['sepal_length', 'petal_length']].cov())

# Scatter Plot
plt.figure(figsize=(6, 4))
plt.scatter(d['sepal_length'], d['petal_length'])
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Scatter Plot")
plt.show()

# Full Correlation Matrix
c = d.iloc[:, :-1].corr()

print("\nCorrelation Matrix:\n")
print(c)

# Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(c, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()