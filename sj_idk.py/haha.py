import kagglehub  #načítání datasetu z kaggle
import matplotlib.pyplot as plt  #knihovna pro tvorbu grafů
import pandas as pd  #knihovna pro práci s tabulkami a daty
import seaborn as sns  #knihovna pro vizualizace s porkočilými grafy

#stažení datasetu z kaggle a načtení cesty k souboru
path = kagglehub.dataset_download("hopesb/student-depression-dataset")
#print("path to dataset:", path)

#načtení csv souboru s daty
csv_file = f"{path}/Student Depression Dataset.csv" 
data = pd.read_csv(csv_file)
#print(data.head())

#1) DISTRIBUCE PODLE POHLAVÍ + DEPRESE
#výpočet počtů a procentuálního zastoupení deprese pro jednotlivá pohlaví v datasetu
group_counts = data.groupby(['Gender', 'Depression']).size().reset_index(name='Count')
total_counts = group_counts.groupby('Gender')['Count'].transform('sum')
group_counts['Percentage'] = (group_counts['Count'] / total_counts * 100).round(1)

#sloupcový graf s daty
plt.figure(figsize=(8, 6))
ax = sns.barplot(data=group_counts, x='Gender', y='Count', hue='Depression', palette='Set2')

#přiřazení procentuálních hodnot nad sloupce
for container in ax.containers:
    for bar, label in zip(container, container.datavalues):
        height = bar.get_height()
        percentage = group_counts.loc[group_counts['Count'] == label, 'Percentage'].values[0]
        ax.text(
            bar.get_x() + bar.get_width() / 2, height, f'{percentage}%', ha='center', va='bottom', fontsize=10
        )
#upravení legendy a popisků v legendě
handles, labels = ax.get_legend_handles_labels()
custom_labels = ['No Depression', 'Depression']
ax.legend(handles=handles, labels=custom_labels, title='Depression')
plt.title('Gender Distribution with Depression Factor')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

#2) DISTRIBUCE PODLE VĚKU + DEPRESE
#vytvoření skupin a jejich rozdělení podle věku
bins = [15, 20, 25, 30, 100] #intrvaly skupin
labels = ['15-20', '21-25', '26-30', '31+'] #názvy skupin
data['Age Group'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

#rozdělení dat (takový jako přiřazení) dle věkových karegorií a deprese 
grouped_data = data.groupby(['Age Group', 'Depression']).size().reset_index(name='Count')

#sloupcový graf, úprava legendy a popisků grafu
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
#odstranění chybějících hodnot u sleep duration
data = data.dropna(subset=['Sleep Duration'])

#sloupcový graf a úprava pořadí názvů sloupců
sns.countplot(x='Sleep Duration', hue='Depression', data=data, palette='viridis', order=[
    "Less than 5 hours", "5-6 hours", "7-8 hours", "More than 8 hours"
])
plt.title("Sleep Duration and Depression")
plt.xlabel("Sleep Duration")
plt.ylabel("Count")
plt.legend(title="Depression")
plt.show()

#4) HISTORIE MENTAL ILLNESS V RODINĚ + DEPRESE
#zase tvorba grafu
sns.countplot(x='Family History of Mental Illness', hue='Depression', data=data, palette='Set2')
plt.title("Family History of Mental Illness and Depression")
plt.xlabel("Family History of Mental Illness")
plt.ylabel("Count")
plt.legend(title="Depression")
plt.show()

#5) BOXPLOT NA ACADEMIC PRESSURE V ZÁVISLOSTI NA DEPRESI
sns.boxplot(x='Depression', y='Academic Pressure', data=data, palette='coolwarm')
plt.title("Academic Pressure by Depression")
plt.show()

#6) BOXPLOT NA FINANCIAL STRESS  V ZÁVISLOSTI NA DEPRESI
sns.boxplot(x='Depression', y='Financial Stress', data=data, palette='coolwarm')
plt.title("Financial Stress by Depression")
plt.show()

#7) ACADEMIC PRESSURE, STUDY SATISFACTION VS DEPRESE
sns.scatterplot(
    x='Academic Pressure', 
    y='Study Satisfaction', 
    hue='Depression',
    data=data, 
    palette='coolwarm'
)
plt.title("Academic Pressure vs Study Satisfaction by Depression")
plt.xlabel("Academic Pressure")
plt.ylabel("Study Satisfaction")
plt.legend(title="Depression")
plt.show()