# STAIML MINI PROJECT
import pandas as pd # for data manipulation, loading and handling dataset
import matplotlib.pyplot as plt # for visualization
import seaborn as sns # for visualization
from sklearn.preprocessing import StandardScaler, LabelEncoder # for preprocessing
# from sklearn.model_selection import train_test_split

# consistent stle for all plots with a clean bg
sns.set_theme(style="whitegrid", palette="muted")

# load the data
df = pd.read_csv("C:\\Users\\Trika\\VS code\\vs codes python\\bs140513_032310.csv")

# finds categorical col and applies Label Encoding to them
label_encoders = {} # storing in a dictionary for future use
for column in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# selects numeric columns and standardizes them
# using StandardScaler to normalize (mean=0, std=1) to bring all values to a similar scale
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# plotting histograms for first 5 numeric columns to get an initial idea of the data distributiom
plt.figure(figsize=(12, 10)) # sets a canvas for thr plots, width x height
df[numeric_cols[:5]].hist(
    bins=30, edgecolor='black', color="#00BFFF", layout=(3, 2), figsize=(12, 10)
) # shortcut to make histrograms, bins=no. of vertical bars used, edgecolor= color of bar edges, color=bar color, layout=arrangement of subplot, figsize= size of whole figure
plt.suptitle("Histograms of Selected Numeric Features", fontsize=18, fontweight='bold')
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # automatically adjusts spacing so the plot dont overlap
plt.show() # display thr plot

# correlation heatmap
# computes and visualizes the correlation matrix bw all numerical, used to see the strength of relationships bw features features
# coolwarm color map shows +ve (red) and -ve (blue) correlations
plt.figure(figsize=(14, 12))
corr_matrix = df.corr()
sns.heatmap( 
    corr_matrix, cmap="coolwarm", annot=True, fmt=".2f",
    square=True, linewidths=0.5, cbar_kws={"shrink": 0.75}
) # annot=shows no inside each cell, cmap=color scheme, linewidth=add spaces b/w cells
plt.title("Correlation Heatmap", fontsize=18, fontweight='bold')
plt.xticks(rotation=45, ha='right') # rotates x-axis label by 45 degrees, ha=aligns them to right for cleaner look
plt.yticks(rotation=0)
plt.tight_layout() # auto-adjusts spacinf of all elements so nothing overlaps
plt.show()

# target variable distribution (Fraud vs Non-Fraud)
# checks if col named fraud exists , uses countplot to show the fraud vs non-fraud
# 0=not fraud, 1=fraud
if 'fraud' in df.columns:
    plt.figure(figsize=(7, 5)) # blank canvas for the graphs
    ax = sns.countplot(x='fraud', data=df, palette=['#90EE90', '#FF6F61']) # makes a bar chart that counts how many times each value appears in fraud
    ax.set_title("Distribution of Fraud vs Non-Fraud", fontsize=16, fontweight='bold')
    ax.set_xticklabels(['Not Fraud', 'Fraud'], fontsize=12) # x-axis
    ax.set_ylabel("Count", fontsize=12) # labels the y-axis
    ax.set_xlabel("") # removes the x-axis label 
    
    for p in ax.patches: # loops thru each bar in chart
        ax.annotate(f'{p.get_height()}', (p.get_x() + 0.3, p.get_height() + 5), fontsize=11)
    # p.get_height()=how tall each bar is, adds the exact number on top of each bar

    # adjusts spacing so the chart doesn’t look squished
    plt.tight_layout()
    plt.show()
