import kagglehub
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

path = kagglehub.dataset_download("hopesb/student-depression-dataset")
#print("Path to dataset files:", path)

csv_file = f"{path}/Student Depression Dataset.csv" 
data = pd.read_csv(csv_file)
#print(data.head())

#1)
# Calculate percentages
group_counts = data.groupby(['Gender', 'Depression']).size().reset_index(name='Count')
total_counts = group_counts.groupby('Gender')['Count'].transform('sum')
group_counts['Percentage'] = (group_counts['Count'] / total_counts * 100).round(1)
# Plot Gender Distribution with Depression Factor
plt.figure(figsize=(8, 6))
ax = sns.barplot(data=group_counts, x='Gender', y='Count', hue='Depression', palette='Set2')
# Annotate percentages on the bars
for container in ax.containers:
    for bar, label in zip(container, container.datavalues):
        height = bar.get_height()
        percentage = group_counts.loc[group_counts['Count'] == label, 'Percentage'].values[0]
        ax.text(
            bar.get_x() + bar.get_width() / 2, height, f'{percentage}%', ha='center', va='bottom', fontsize=10
        )
# Customize legend
handles, labels = ax.get_legend_handles_labels()
custom_labels = ['No Depression', 'Depression']
ax.legend(handles=handles, labels=custom_labels, title='Depression')

plt.title('Gender Distribution with Depression Factor')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Create age groups
bins = [15, 20, 25, 30, 100]
labels = ['15-20', '21-25', '26-30', '31+']

data['Age Group'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

# Group data by Age Group and Depression
grouped_data = data.groupby(['Age Group', 'Depression']).size().reset_index(name='Count')

# Plot Age Distribution with Depression Factor
plt.figure(figsize=(10, 6))
ax = sns.barplot(data=grouped_data, x='Age Group', y='Count', hue='Depression', palette='Set2')

# Customize legend
handles, labels = ax.get_legend_handles_labels()
custom_labels = ['No Depression', 'Depression']
ax.legend(handles=handles, labels=custom_labels, title='Depression')

# Add title and labels
plt.title('Age Distribution by Depression Factor')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.show()
















#sleep duration and depression
sns.countplot(x='Sleep Duration', hue='Depression', data=data, palette='viridis')
plt.title("Sleep Duration and Depression")
plt.xlabel("Sleep Duration")
plt.ylabel("Count")
plt.legend(title="Depression")
plt.show()

#family history of mental illness and depression
sns.countplot(x='Family History of Mental Illness', hue='Depression', data=data, palette='Set2')
plt.title("Family History of Mental Illness and Depression")
plt.xlabel("Family History of Mental Illness")
plt.ylabel("Count")
plt.legend(title="Depression")
plt.show()

#are higher academic pressure, lower sleep duration, lower study satisfaction, higher financial stress, and yes in family history of mental illness connected to depression?
# Boxplot for Academic Pressure
sns.boxplot(x='Depression', y='Academic Pressure', data=data, palette='coolwarm')
plt.title("Academic Pressure by Depression")
plt.show()

# Boxplot for Study Satisfaction
sns.boxplot(x='Depression', y='Study Satisfaction', data=data, palette='coolwarm')
plt.title("Study Satisfaction by Depression")
plt.show()

# Boxplot for Financial Stress
sns.boxplot(x='Depression', y='Financial Stress', data=data, palette='coolwarm')
plt.title("Financial Stress by Depression")
plt.show()

#academic pressure + study satisfaction and depression
sns.scatterplot(
    x='Academic Pressure', 
    y='Study Satisfaction', 
    hue='Depression',  # Add this to color points by Depression
    data=data, 
    palette='coolwarm'
)
plt.title("Academic Pressure vs Study Satisfaction by Depression")
plt.xlabel("Academic Pressure")
plt.ylabel("Study Satisfaction")
plt.legend(title="Depression")
plt.show()