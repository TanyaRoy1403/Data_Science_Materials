import pandas as pd 
import statistics
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns

#calculate z-score
data = [5, 2, 4.5, 4, 3, 2, 6, 20, 9, 2.5, 3.5, 4.75, 6.5, 2.5, 8, 1]
df = pd.DataFrame(data, columns=['Value'])
# print(df)

#first calculate mean
mean_val=np.mean(data)
print(f"mean{mean_val}")
#standar deviation
std_val=np.std(data)

for idx, value in enumerate(data):
    z_score=(value-mean_val)/std_val
    print(f"Index {idx}(Value:{value}):Z_Score= {z_score:.2f}")

#we can use direct 'zscore' class of library scipy.stats--> from scipy.stats import zscore

#calculate Inter Quatile range and box plot
# Q1--> 25 PERCENTILE
#Q3--> 75 PERCENTILE 

#lets find the data point(value) of Q1 and Q3
data=sorted(data)
print(f"data:{data}")
Q1=np.percentile(data,25)
print(f"Q1value {Q1}\n")
Q3=np.percentile(data,75)
print(f"Q3 value {Q3}\n")

Inter_quetile_rang= Q3-Q1
print(f"Inter Range{Inter_quetile_rang}\n")
# RANGE TO DETECT OUTLIER -->[lower_value,higher_value] -->all data points must lie in b/w this, otherwise that data point will be outlier

low_range=Q1-1.5*Inter_quetile_rang
print(f"low_range{low_range}\n")
high_range=Q3+1.5*Inter_quetile_rang
print(f"high range{high_range}")

#Detect outliers in the data
for i in data:
    if (not(i>=low_range and i<=high_range)):
        print(f"Outlier is: {i}")




# Set the style of the visualization
sns.set_style("whitegrid")

# Create the histogram and KDE plot
plt.figure(figsize=(10, 6)) # Adjusts the size of the plot
sns.histplot(data, kde=True, bins=10)

# Add titles and labels for clarity
plt.title('Distribution of Your Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show the plot
sns.boxplot(data)
plt.show()

int 