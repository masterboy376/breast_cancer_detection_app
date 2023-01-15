# -*- coding: utf-8 -*-
"""breast_cancer_detection_using_classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15mGgFmNQRrShYg-5uqjg6oeX8OBDSVNN

# **Breast Cancer Detection Machine Learning End to End Project**

## **Goal of the ML project**

We have extracted features of breast cancer patient cells and normal person cells. As a Machine learning engineer / Data Scientist has to create an ML model to classify malignant and benign tumor. To complete this ML project we are using the supervised machine learning classifier algorithm.

### **Import essential libraries**
"""

# import libraries
import pandas as pd # for data manupulation or analysis
import numpy as np # for numeric calculation
import matplotlib.pyplot as plt # for data visualization
import seaborn as sns # for data visualization

"""### **Load breast cancer dataset & explore**"""

#Load breast cancer dataset
from sklearn.datasets import load_breast_cancer
cancer_dataset = load_breast_cancer()

type(cancer_dataset)

# keys in dataset
cancer_dataset.keys()

#featurs of each cells in numeric format
cancer_dataset['data']

#malignant or benign value
cancer_dataset['target']

#target value name malignant or benign tumor
cancer_dataset['target_names']

"""0:- means malignant tumor, 1:- mean benign tumor"""

#description of data
print(cancer_dataset['DESCR'])

#name of features
print(cancer_dataset['feature_names'])

"""When we call load_breast_cancer() class it downloads breast_cancer.csv file and you can see file location."""

#location/path of data file
print(cancer_dataset['filename'])

"""### **Create DataFrame**"""

#create datafrmae
cancer_df = pd.DataFrame(np.c_[cancer_dataset['data'],cancer_dataset['target']],
             columns = np.append(cancer_dataset['feature_names'], ['target']))

#Head of cancer DataFrame
cancer_df.head(6)

#Tail of cancer DataFrame
cancer_df.tail(6)

#Information of cancer Dataframe
cancer_df.info()

"""We have a total of non-null 569 patients’ information with 31 features. All feature data types in the float. The size of the DataFrame is 137.9 KB.

Numerical distribution of data. We can know to mean, standard deviation, min, max, 25%,50% and 75% value of each feature.
"""

#Numerical distribution of data
cancer_df.describe()

"""We have clean and well formated DataFrame, so DtaFrame is ready to visualize.

### **Data Visualization**

### **Pair plot of breast cancer data** : Basically, the pair plot is used to show the numeric distribution in the scatter plot
"""

#dataframe
# sns.pairplot(cancer_df, hue = 'target')

#pair plot of sample feature
sns.pairplot(cancer_df, hue = 'target', 
             vars = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness'] )

"""The pair plot showing malignant and benign tumor data distributed in two classes. It is easy to differentiate in the pair plot.

### **Counterplot** : Showing the total count of malignant and benign tumor patients in counterplot
"""

#Count the target class
sns.countplot(cancer_df['target'])

"""In the below counterplot max samples mean radius is equal to 1."""

#counter plot of feature mean radius
plt.figure(figsize = (20,8))
sns.countplot(cancer_df['mean radius'])

"""### **Heatmap**

### **Heatmap of breast cancer DataFrame** : In the below heatmap we can see the variety of different feature’s value. The value of feature ‘mean area’ and ‘worst area’ are greater than other and ‘mean perimeter’, ‘area error’, and ‘worst perimeter’ value slightly less but greater than remaining features.
"""

#heatmap of DataFrame
plt.figure(figsize=(16,9))
sns.heatmap(cancer_df)

"""### **Heatmap of a correlation matrix** : To find a correlation between each feature and target we visualize heatmap using the correlation matrix."""

#Heatmap of Correlation matrix of breast cancer DataFrame
plt.figure(figsize=(20,20))
sns.heatmap(cancer_df.corr(), annot = True, cmap ='coolwarm', linewidths=2)

"""### **Correlation barplot** : Taking the correlation of each feature with the target and the visualize barplot."""

#create second DataFrame by droping target
cancer_df2 = cancer_df.drop(['target'], axis = 1)
print("The shape of 'cancer_df2' is : ", cancer_df2.shape)

#visualize correlation barplot
plt.figure(figsize = (16,5))
ax = sns.barplot(cancer_df2.corrwith(cancer_df.target).index, cancer_df2.corrwith(cancer_df.target))
ax.tick_params(labelrotation = 90)

"""In the above correlation barplot only feature ‘smoothness error’ is strongly positively correlated with the target than others. The features ‘mean factor dimension’, ‘texture error’, and ‘symmetry error’ are very less positive correlated and others remaining are strongly negatively correlated.

### **Data Preprocessing**

### **Split DataFrame in train and test**
"""

#input variable
X = cancer_df.drop(['target'], axis = 1)
X.head(6)

#output variable
y = cancer_df['target']
y.head(6)

# split dataset into train and test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state= 5)

"""### **Feature Scaling**

Converting different units and magnitude data in one unit.
"""

#Feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train_sc = sc.fit_transform(X_train)
X_test_sc = sc.transform(X_test)

"""### **Breast Cancer Detection Machine Learning Model Building**

We have clean data to build the Ml model. But which Machine learning algorithm is best for the data we have to find. The output is a categorical format so we will use supervised classification machine learning algorithms.

To build the best model, we have to train and test the dataset with multiple Machine Learning algorithms then we can find the best ML model. So let’s try.

First, we need to import the required packages.
"""

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

"""### **Support Vector Classifier**"""

# Support vector classifier
from sklearn.svm import SVC
svc_classifier = SVC()
svc_classifier.fit(X_train, y_train)
y_pred_scv = svc_classifier.predict(X_test)
accuracy_score(y_test, y_pred_scv)

# Train with Standard scaled Data
svc_classifier2 = SVC()
svc_classifier2.fit(X_train_sc, y_train)
y_pred_svc_sc = svc_classifier2.predict(X_test_sc)
accuracy_score(y_test, y_pred_svc_sc)

"""### **Logistic Regression**"""

# Logistic Regression
from sklearn.linear_model import LogisticRegression
lr_classifier = LogisticRegression(random_state = 51, penalty = 'l2')
lr_classifier.fit(X_train, y_train)
y_pred_lr = lr_classifier.predict(X_test)
accuracy_score(y_test, y_pred_lr)

# Train with Standard scaled Data
lr_classifier2 = LogisticRegression(random_state = 51, penalty = 'l2')
lr_classifier2.fit(X_train_sc, y_train)
y_pred_lr_sc = lr_classifier.predict(X_test_sc)
accuracy_score(y_test, y_pred_lr_sc)

"""### **K – Nearest Neighbor Classifier**"""

# K – Nearest Neighbor Classifier
from sklearn.neighbors import KNeighborsClassifier
knn_classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
knn_classifier.fit(X_train, y_train)
y_pred_knn = knn_classifier.predict(X_test)
accuracy_score(y_test, y_pred_knn)

# Train with Standard scaled Data
knn_classifier2 = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
knn_classifier2.fit(X_train_sc, y_train)
y_pred_knn_sc = knn_classifier.predict(X_test_sc)
accuracy_score(y_test, y_pred_knn_sc)

"""### **Naive Bayes Classifier**"""

# Naive Bayes Classifier
from sklearn.naive_bayes import GaussianNB
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)
y_pred_nb = nb_classifier.predict(X_test)
accuracy_score(y_test, y_pred_nb)

# Train with Standard scaled Data
nb_classifier2 = GaussianNB()
nb_classifier2.fit(X_train_sc, y_train)
y_pred_nb_sc = nb_classifier2.predict(X_test_sc)
accuracy_score(y_test, y_pred_nb_sc)

"""### **Decision Tree Classifier**"""

# Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
dt_classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 51)
dt_classifier.fit(X_train, y_train)
y_pred_dt = dt_classifier.predict(X_test)
accuracy_score(y_test, y_pred_dt)

# Train with Standard scaled Data
dt_classifier2 = DecisionTreeClassifier(criterion = 'entropy', random_state = 51)
dt_classifier2.fit(X_train_sc, y_train)
y_pred_dt_sc = dt_classifier.predict(X_test_sc)
accuracy_score(y_test, y_pred_dt_sc)

"""### **Random Forest Classifier**"""

# Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
rf_classifier = RandomForestClassifier(n_estimators = 20, criterion = 'entropy', random_state = 51)
rf_classifier.fit(X_train, y_train)
y_pred_rf = rf_classifier.predict(X_test)
accuracy_score(y_test, y_pred_rf)

# Train with Standard scaled Data
rf_classifier2 = RandomForestClassifier(n_estimators = 20, criterion = 'entropy', random_state = 51)
rf_classifier2.fit(X_train_sc, y_train)
y_pred_rf_sc = rf_classifier.predict(X_test_sc)
accuracy_score(y_test, y_pred_rf_sc)

"""### **Adaboost Classifier**"""

# Adaboost Classifier
from sklearn.ensemble import AdaBoostClassifier
adb_classifier = AdaBoostClassifier(DecisionTreeClassifier(criterion = 'entropy', random_state = 200),
                                    n_estimators=2000,
                                    learning_rate=0.1,
                                    algorithm='SAMME.R',
                                    random_state=1,)
adb_classifier.fit(X_train, y_train)
y_pred_adb = adb_classifier.predict(X_test)
accuracy_score(y_test, y_pred_adb)

# Train with Standard scaled Data
adb_classifier2 = AdaBoostClassifier(DecisionTreeClassifier(criterion = 'entropy', random_state = 200),
                                    n_estimators=2000,
                                    learning_rate=0.1,
                                    algorithm='SAMME.R',
                                    random_state=1,)
adb_classifier2.fit(X_train_sc, y_train)
y_pred_adb_sc = adb_classifier2.predict(X_test_sc)
accuracy_score(y_test, y_pred_adb_sc)

"""### **XGBoost Classifier**"""

# XGBoost Classifier
from xgboost import XGBClassifier
xgb_classifier = XGBClassifier()
xgb_classifier.fit(X_train, y_train)
y_pred_xgb = xgb_classifier.predict(X_test)
accuracy_score(y_test, y_pred_xgb)

# Train with Standard scaled Data
xgb_classifier2 = XGBClassifier()
xgb_classifier2.fit(X_train_sc, y_train)
y_pred_xgb_sc = xgb_classifier2.predict(X_test_sc)
accuracy_score(y_test, y_pred_xgb_sc)

"""### **XGBoost Parameter Tuning : Randomized Search**"""

# XGBoost classifier most required parameters
params={
 "learning_rate"    : [0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ] ,
 "max_depth"        : [ 3, 4, 5, 6, 8, 10, 12, 15],
 "min_child_weight" : [ 1, 3, 5, 7 ],
 "gamma"            : [ 0.0, 0.1, 0.2 , 0.3, 0.4 ],
 "colsample_bytree" : [ 0.3, 0.4, 0.5 , 0.7 ] 
}

# Randomized Search
from sklearn.model_selection import RandomizedSearchCV
random_search = RandomizedSearchCV(xgb_classifier, param_distributions=params, scoring= 'roc_auc', n_jobs= -1, verbose= 3)
random_search.fit(X_train, y_train)

random_search.best_params_

random_search.best_estimator_

random_search.best_score_

# training XGBoost classifier with best parameters
xgb_classifier_pt = XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
       colsample_bynode=1, colsample_bytree=0.4, gamma=0.2,
       learning_rate=0.1, max_delta_step=0, max_depth=15,
       min_child_weight=1, missing=None, n_estimators=100, n_jobs=1,
       nthread=None, objective='binary:logistic', random_state=0,
       reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
       silent=None, subsample=1, verbosity=1)
 
xgb_classifier_pt.fit(X_train, y_train)
y_pred_xgb_pt = xgb_classifier_pt.predict(X_test)

accuracy_score(y_test, y_pred_xgb_pt)

"""### **Confusion Matrix**"""

cm = confusion_matrix(y_test, y_pred_xgb_pt)
plt.title('Heatmap of Confusion Matrix', fontsize = 15)
sns.heatmap(cm, annot = True)
plt.show()

"""The model is giving 0% type II error and it is best.

### **Classification Report of Model**
"""

print(classification_report(y_test, y_pred_xgb_pt))

"""### **Cross-validation of the ML model**

To find the ML model is overfitted, under fitted or generalize doing cross-validation.
"""

# Cross validation
# from sklearn.model_selection import cross_val_score
# cross_validation = cross_val_score(estimator = xgb_model_pt2, X = X_train_sc, y = y_train, cv = 10)
# print("Cross validation of XGBoost model = ",cross_validation)
# print("Cross validation of XGBoost model (in mean) = ",cross_validation.mean())
from sklearn.model_selection import cross_val_score
cross_validation = cross_val_score(estimator = xgb_classifier_pt, X = X_train_sc,y = y_train, cv = 10)
print("Cross validation accuracy of XGBoost model = ", cross_validation)
print("\nCross validation mean accuracy of XGBoost model = ", cross_validation.mean())

"""The mean accuracy value of cross-validation is 96.24% and XGBoost model accuracy is 98.24%. It showing XGBoost is slightly overfitted but when training data will more it will generalized model.

### **Save the Machine Learning model**

After completion of the Machine Learning project or building the ML model need to deploy in an application. To deploy the ML model need to save it first. To save the Machine Learning project we can use the pickle or joblib package.

Here, we will use pickle, Use anyone which is better for you.
"""

## Pickle
import pickle
 
# save model
pickle.dump(xgb_classifier_pt, open('model.pkl', 'wb'))
 
# load model
breast_cancer_detector_model = pickle.load(open('model.pkl', 'rb'))
 
# predict the output
y_pred = breast_cancer_detector_model.predict(X_test)
 
# confusion matrix
print('Confusion matrix of XGBoost model: \n',confusion_matrix(y_test, y_pred),'\n')
 
# show the accuracy
print('Accuracy of XGBoost model = ',accuracy_score(y_test, y_pred))

"""Congratulation!!!!!!!

Now this Machine learning Project successfully completed with 98.24% accuracy which is great for ‘Breast Cancer Detection using Machine learning’ project. Now, it is ready to be deployed our ML model in the healthcare project.
"""