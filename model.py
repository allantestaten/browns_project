import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.metrics import classification_report, confusion_matrix, plot_confusion_matrix
from sklearn.linear_model import LogisticRegression
import sklearn.preprocessing

def model_columns(train,validate,test):
    '''This function will provide my models with the correct features to run for their x and y values'''
    # assigning features to be used for modeling  
    x_cols = ['rush_yards_gained','turnovers_forced']
    y_train = train['result']

    # assigning features to be used for modeling to train, validate and test data sets
    X_train = train[x_cols]
    X_validate = validate[x_cols]
    y_validate = validate['result']
    X_test = test[x_cols]
    y_test = test['result']

    # changing y validate into a dataframe to append the new column with predicted values 
    y_validate= pd.DataFrame(y_validate)

    # changing y validate into a dataframe to append the new column with predicted values
    y_test= pd.DataFrame(y_test)

    return X_train, X_validate, X_test, y_train, y_validate, y_test

def scaling(X_train,X_validate,X_test):
    '''function will scale features across data sets train, validate and test'''
    # applying scaling to all the data splits.
    scaler = sklearn.preprocessing.StandardScaler()
    scaler.fit(X_train)
    # transforming train, validate and test datasets
    X_train_scaled = scaler.transform(X_train)
    X_validate_scaled = scaler.transform(X_validate)
    X_test_scaled = scaler.transform(X_test)
  
    return X_train_scaled, X_validate_scaled, X_test_scaled

def baseline_model(y_train):
    '''this function will create the baseline model'''
    baseline = y_train.mode()
    #Produce a boolean array with True representing a match between the baseline prediction and reality
    matches_baseline_prediction = (y_train == 'L')
    baseline_accuracy = matches_baseline_prediction.mean()
    print(f"Baseline Accuracy: {round(baseline_accuracy, 2)}")

def decision_tree(X_train,y_train,x,y):
    '''this function will create decision tree model'''
    # Make the model
    tree1 = DecisionTreeClassifier(max_depth=1, random_state=100)

    # Fit the model (on train and only train)
    tree1 = tree1.fit(X_train, y_train)

    # Evaluating model on training sample
    y_predictions = tree1.predict(x)

    #printing accuracy
    print('Accuracy of Decision Tree classifier: {:.2f}'
      .format(tree1.score(x, y)))

def random_forrest_model(X_train,y_train,x,y):
    ''' this function will produce a knn model'''
    # creating Random Forrest classifier, algorithm
    rf = RandomForestClassifier(
    min_samples_leaf=2, 
    max_depth=3, 
    random_state=100)
    # Fit model to sample data
    rf.fit(X_train, y_train)
    #creating predictions from training sample 
    y_preds = rf.predict(x)
    # evaluating model
    rf.score(x, y)
    #printing accuracy
    print('Accuracy of Random Forrest classifier: {:.2f}'
      .format(rf.score(x, y)))

def knn_model(X_train,y_train,x,y):
    '''this function will produce a knn model'''
    # creating model
    knn = KNeighborsClassifier(n_neighbors=3)
    # fitting data to train data 
    knn.fit(X_train, y_train)
    # generating predictions for train data 
    y_preds = knn.predict(x)
    # Evaluating results of model, confusion matrix, and classification report.
    print('Accuracy of KNN classifier: {:.2f}'
     .format(knn.score(x, y)))   

def log_reg(X_train,y_train,x,y):
    # Define the logistic regression model
    logit = LogisticRegression(random_state=100)
    # Fit a model using only these specified features
    # logit.fit(X_train[["age", "pclass", "fare"]], y_train)
    logit.fit(X_train, y_train)
    # Since we .fit on a subset, we .predict on that same subset of features
    y_pred = logit.predict(x)
    print('Accuracy of Logistic Regression classifier: {:.2f}'
     .format(logit.score(x, y)))

def random_forrest_model_test(X_train,y_train,X_test_scaled,y_test):
    ''' this function will produce a knn model'''
    # creating Random Forrest classifier, algorithm
    rf = RandomForestClassifier(
    min_samples_leaf=2, 
    max_depth=3, 
    random_state=100)
    # Fit model to sample data
    rf.fit(X_train, y_train)
    #creating predictions from training sample 
    y_preds = rf.predict(X_test_scaled)
    # evaluating model
    rf.score(X_test_scaled, y_test)
    #printing accuracy
    print('Accuracy of Random Forrest classifier: {:.2f}'
      .format(rf.score(X_test_scaled, y_test)))