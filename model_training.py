## Python File -- functionalized version of titanic_main.ipynb

# Dependencies
import os
import boto3
import codecs
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Connect to training and test data in S3 bucket
client = boto3.client("s3")
s3 = boto3.client("s3")
train_data = client.get_object(Bucket="data-bootcamp-titanic", Key="train.csv")
test_data = client.get_object(Bucket="data-bootcamp-titanic", Key="test.csv")

# Create pandas Dataframe
train_df = pd.read_csv(train_data["Body"])
test_df = pd.read_csv(test_data["Body"])

############################
## Begin Machine Learning ##
############################

# Logistic Regression 

clf = LogisticRegression(solver='liblinear')

# Create X_train and y_train
X_train = train_df.drop(["PassengerId","Ticket","Cabin", "Name", "Embarked"], axis=1)
X_train = X_train.dropna()
y_train = X_train["Survived"]
X_train = X_train.drop(["Survived"], axis=1)

# Create X_test
X_test = test_df.drop(["PassengerId","Ticket","Cabin", "Name", "Embarked"], axis=1)
X_test = X_test.dropna()

# Encode Sex and Passenger Class
X_train = pd.get_dummies(X_train, columns=["Sex", "Pclass"])
X_test = pd.get_dummies(X_test, columns=["Sex", "Pclass"])

# Bin Fare for encoding
bins = [0, 8.05, 15.7417, 33.375, 100, 513]
labels = ["cheapest", "cheap", "medium", "expensive", "most expensive"]
X_train["Fare cat."] = pd.cut(X_train["Fare"], bins, labels=labels)
X_test["Fare cat."] = pd.cut(X_test["Fare"], bins, labels=labels)

# Encode Fare
X_train = pd.get_dummies(X_train, columns=["Fare cat."])
X_test = pd.get_dummies(X_test, columns=["Fare cat."])

# drop Fare columns
X_train = X_train.drop(columns=["Fare", "Parch", "SibSp"])
X_test = X_test.drop(columns=["Fare", "Parch", "SibSp"])

## fit the model
clf.fit(X_train,y_train)

filename = "model_ml.sav"
pickle.dump(clf, open(filename, 'wb'))

