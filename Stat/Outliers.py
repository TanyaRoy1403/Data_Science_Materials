import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

def detect_outlier_Zscore(data):
    threshold = 1        
    mean_val = np.mean(data)
    std_val = np.std(data)
    outliers = []  # reset on each function call
    
    for i in data:
        z_score = (i - mean_val) / std_val
        if np.abs(z_score) > threshold:
            outliers.append(i)
    return outliers

dataset = [5, 2, 4.5, 4, 3, 2, 6, 20, 9, 2.5, 3.5, 4.75, 6.5, 2.5, 8, 18, 30, 1]
ans = detect_outlier_Zscore(dataset)
print(ans)











