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


def logistic_model_1(age, gender, pclass, fare):
  
  # handle gender encoding
  male = 0
  female = 0
  if (gender == "male"):
    male = 1
  else:
    female = 1
  
  # handle class encoding
  pclass1 = 0
  pclass2 = 0
  pclass3 = 0
  if(pclass == 1):
    pclass1 = 1
  elif(pclass == 2):
    pclass2 = 1
  else:
    pclass3 = 1
  
  # handle fare encoding
  cheapest = 0
  cheap = 0
  medium = 0
  expensive = 0
  most_expensive = 0
  if(fare < 8.05):
    cheapest = 1
  elif(fare < 15.7417):
    cheap = 1
  elif(fare < 33.375):
    medium = 1
  elif(fare < 100):
    expensive = 1
  else:
    most_expensive = 1
  
  user_df = pd.DataFrame({
    "Age": age,
    "Sex_female": female,	
    "Sex_male": male,	
    "Pclass_1": pclass1,	
    "Pclass_2": pclass2,	
    "Pclass_3": pclass3,	
    "Fare cat._cheapest": cheapest,	
    "Fare cat._cheap": cheap,	
    "Fare cat._medium": medium,	
    "Fare cat._expensive": expensive,	
    "Fare cat._most expensive": most_expensive
  }, index=[0])

  return clf.predict(user_df)[0]
  
  
print(logistic_model_1(1,"male",3,7))


""" 
def logistic_regression_1()

Arguments:
Age == int 
Gender == string (male or female)
Class == int (1,2, or 3)
Fare == int 

Returns:
Survival_code == int (1 survived; 0 died)

"""