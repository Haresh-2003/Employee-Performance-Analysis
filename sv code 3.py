import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv(r"C:\Users\HARESH PS\Downloads\Extended_Employee_Performance_and_Productivity_Data.csv")

print("Initial shape of the dataset:", df.shape)
df = df.drop_duplicates()
df = df.dropna()
print("Shape after removing duplicates and missing values:", df.shape)


df_encoded = pd.get_dummies(df, drop_first=True)
print("Columns after one-hot encoding:", df_encoded.columns)

correlation_matrix = df_encoded.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

sns.pairplot(df_encoded)
plt.show()


trained_group = df[df['training_program'] == 'attended']['productivity_score']
non_trained_group = df[df['training_program'] == 'not_attended']['productivity_score']


print("Number of employees who attended training:", len(trained_group))
print("Number of employees who did not attend training:", len(non_trained_group))

t_stat, p_val = stats.ttest_ind(trained_group, non_trained_group)
print(f'T-statistic: {t_stat}, P-value: {p_val}')
if p_val < 0.05:
    print('There is a significant difference in performance between trained and non-trained employees.')
else:
    print('There is no significant difference in performance between trained and non-trained employees.')


plt.figure(figsize=(10, 6))
sns.boxplot(x='training_program', y='productivity_score', data=df)
plt.title('Productivity Score by Training Program')
plt.show()
