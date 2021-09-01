## Python File -- functionalized version of titanic_main.ipynb

# Dependencies
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle


# Create pandas Dataframe using S3 url

train_df = pd.read_csv("https://data-bootcamp-titanic.s3.us-east-2.amazonaws.com/train.csv")
test_df = pd.read_csv("https://data-bootcamp-titanic.s3.us-east-2.amazonaws.com/test.csv")

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
