# -*- coding: utf-8 -*-
"""PPM - Bank Churn Dataset

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mXYkpWDe_PU6Z-T9gEps_Td7gVElmBNW

#Preprocess
"""

import pandas as pd
import numpy as np

!pip install kaggle

#Membaca dataset ini download dari kaggle yah
df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

#menampilkan 5 baris pertama dari DataFrame
df_train.head()

#mengecek jumlah missing values dari setiap dataset
df_train.isnull().sum()

df_test.isnull().sum()

df_train.describe(include=['O'])

#menghasilkan statistik deskriptif
df_train.describe()

#menghapus kolom surname dan customerId karena dua fitur itu tidak berpengaruh ke modelling nanti
columns_to_drop = ['Surname', 'CustomerId']
df_train.drop(columns=columns_to_drop, inplace=True)
df_test.drop(columns=columns_to_drop, inplace=True)

df_train.info()

"""##Numerical data"""

import seaborn as sns
import matplotlib.pyplot as plt

"""Numerical data terdiri dari age, tenure, balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, dan Exited"""

sns.histplot(data=df_train, x='Age')
plt.show()

df_train.isnull().sum()

"""##Categorical data"""

df_train['Geography'].unique()

df_train['Gender'].unique()

df_train = pd.get_dummies(df_train)
df_test = pd.get_dummies(df_test)
df_train

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

#data train
scaled = scaler.fit_transform(df_train)
df_train_scaled = pd.DataFrame(scaled, columns=df_train.columns)
df_train_scaled.head()

#data test
scaled = scaler.fit_transform(df_test)
df_test_scaled = pd.DataFrame(scaled, columns=df_test.columns)
df_test_scaled.head()

"""#Modelling"""

from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

X_train = df_train_scaled.drop(['Exited'], axis=1)
y_train = df_train_scaled['Exited']
X_test = df_test_scaled.copy()
X_train.shape, y_train.shape, X_test.shape

#SVC sama aja dengan SVM
svc = SVC()
svc.fit(X_train, y_train)
SVC_pred = svc.predict(X_test)
score_svc = svc.score(X_train, y_train)
score_svc

#KNN
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, y_train)
KNN_pred = knn.predict(X_test)
score_knn = knn.score(X_train, y_train)
score_knn

#Gaussian Naive Bayes
gaussian = GaussianNB()
gaussian.fit(X_train, y_train)
GNB_pred = gaussian.predict(X_test)
score_gaussian = gaussian.score(X_train, y_train)
score_gaussian

#Random Forest
random_forest = RandomForestClassifier()
random_forest.fit(X_train, y_train)
N_pred = random_forest.predict(X_test)
random_forest.score(X_train, y_train)
score_rf = random_forest.score(X_train, y_train)
score_rf

#Ada Boost
ada_boost = AdaBoostClassifier()
ada_boost.fit(X_train, y_train)
AB_pred = ada_boost.predict(X_test)
ada_boost.score(X_train, y_train)
score_ab = ada_boost.score(X_train, y_train)
score_ab

#Gradient Boosting
gb = GradientBoostingClassifier()
gb.fit(X_train,y_train)
GB_pred = gb.predict(X_test)
print(gb.score(X_train, y_train))

#Decision Tree (Paling bagus diantara yg lain, karena nilainya 1 sedangkan yg lain 0,8)
decision_tree = DecisionTreeClassifier()
decision_tree.fit(X_train, y_train)
Y_pred = decision_tree.predict(X_test)
score_dt = decision_tree.score(X_train, y_train)
score_dt

"""#Submit to Kaggle"""

submission_sample = pd.read_csv('sample_submission.csv')

submission_sample.head()

df_final['Exited'].value_counts()

df_final = pd.DataFrame({ "id": submission_sample["id"],"Exited": SVC_pred})
df_final

df_final.to_csv('prediction_result1.csv', index=False)