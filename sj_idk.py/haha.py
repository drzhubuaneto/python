import kagglehub  #načítání data setu z kaggle
import matplotlib.pyplot as plt  #knihovna pro tvorbu grafů
import pandas as pd  #práce s tabulkami
import seaborn as sns

path = kagglehub.dataset_download("hopesb/student-depression-dataset")
#print("Path to dataset files:", path)
#kontrola path

csv_file = f"{path}/Student Depression Dataset.csv" 
data = pd.read_csv(csv_file)
#print(data.head())
#kontrola, že to načítá soubor

#1) DISTRIBUCE PODLE POHLAVÍ A DEPRESE
#výpočet procentuálního zastoupení deprese u žen a u mužů v datasetu
group_counts = data.groupby(['Gender', 'Depression']).size().reset_index(name='Count')
total_counts = group_counts.groupby('Gender')['Count'].transform('sum')
group_counts['Percentage'] = (group_counts['Count'] / total_counts * 100).round(1)

plt.figure(figsize=(8, 6))
ax = sns.barplot(data=group_counts, x='Gender', y='Count', hue='Depression', palette='Set2')
#procenta přiřadit ke grafu
for container in ax.containers:
    for bar, label in zip(container, container.datavalues):
        height = bar.get_height()
        percentage = group_counts.loc[group_counts['Count'] == label, 'Percentage'].values[0]
        ax.text(
            bar.get_x() + bar.get_width() / 2, height, f'{percentage}%', ha='center', va='bottom', fontsize=10
        )
#legenda
handles, labels = ax.get_legend_handles_labels()
custom_labels = ['No Depression', 'Depression']
ax.legend(handles=handles, labels=custom_labels, title='Depression')

#popisky grafu
plt.title('Gender Distribution with Depression Factor')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

#2) DISTRIBUCE PODLE VĚKU A DEPRESE
#vytvoření skupin dle věku
bins = [15, 20, 25, 30, 100]
labels = ['15-20', '21-25', '26-30', '31+']
data['Age Group'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

#rozdělení dat 
grouped_data = data.groupby(['Age Group', 'Depression']).size().reset_index(name='Count')

plt.figure(figsize=(10, 6))
ax = sns.barplot(data=grouped_data, x='Age Group', y='Count', hue='Depression', palette='Set2')

handles, labels = ax.get_legend_handles_labels()
custom_labels = ['No Depression', 'Depression']
ax.legend(handles=handles, labels=custom_labels, title='Depression')

plt.title('Age Distribution by Depression Factor')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.show()

#3) SPÁNEK A DEPRESE
data = data.dropna(subset=['Sleep Duration'])

#plots
sns.countplot(x='Sleep Duration', hue='Depression', data=data, palette='viridis', order=[
    "Less than 5 hours", "5-6 hours", "7-8 hours", "More than 8 hours"
])
plt.title("Sleep Duration and Depression")
plt.xlabel("Sleep Duration")
plt.ylabel("Count")
plt.legend(title="Depression")
plt.show()


#4) HISTORIE MENTAL ILLNESS V RODINĚ A DEPRESE
sns.countplot(x='Family History of Mental Illness', hue='Depression', data=data, palette='Set2')
plt.title("Family History of Mental Illness and Depression")
plt.xlabel("Family History of Mental Illness")
plt.ylabel("Count")
plt.legend(title="Depression")
plt.show()

#5) BOXPLOT NA ACADEMIC PRESSURE A DEPRESI
sns.boxplot(x='Depression', y='Academic Pressure', data=data, palette='coolwarm')
plt.title("Academic Pressure by Depression")
plt.show()

#6) BOXPLOT NA FINANCIAL STRESS A DEPRESI
sns.boxplot(x='Depression', y='Financial Stress', data=data, palette='coolwarm')
plt.title("Financial Stress by Depression")
plt.show()


#7) academic pressure + study satisfaction and depression
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