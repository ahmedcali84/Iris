# Load the Usual Suspects
from sklearn.metrics import accuracy_score , classification_report
from sklearn.model_selection import train_test_split , cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import  pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import joblib

# load the data into variables
data = load_iris()
target = data['target']
columns = data['feature_names']

# Present it in Pandas DataFrame for Data Science Classification
df = pd.DataFrame(data = data.data , columns=columns)
df['target'] = target

# flower class and its target code
# {"setosa: 0", "versicolor: 1" , "virginica: 2"}

def applyTypes(row):
	if row['target'] == 0:
		return 'setosa'
	elif row['target'] == 1:
		return 'versicolor'
	else:
		return "virginica"
	
df['type'] = df.apply(applyTypes, axis=1)
print(df.head())

# Dependent Variables
X = pd.DataFrame(data = df[[x for x in data['feature_names']]], columns=columns)
print(X.info())

# independent Variables
y = df['type']
print(y.info())

# Split the Data into Train/Test 
X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=0.25 , random_state=42)

# Shapes of Our data
print(f"X_train shape = {X_train.shape}\n\
		X_test shape = {X_test.shape}\n\
		y_train shape = {y_train.shape}\n\
		y_test shape = {y_test.shape}\n")

# Modelling
knn = KNeighborsClassifier()

# Fit the Training Data
model = knn.fit(X_train,y_train)

# Predict the Classes for Test data
predictions = model.predict(X_test)

# Evaluate the Model Accuracy Performance 
accuracyScore = accuracy_score(predictions, y_test)

# print the Accuracy Score
print(f"Accuracy Score: {accuracyScore}")

# Evaluate the Model on Classification Report
classReport = classification_report(y_test,predictions)

# Print The Classification Report
print(f"Classification Report: \n{classReport}")


""" Just to be sure if we didn't overfit 
the model lets do Cross-Validation"""

knnCrossVal = KNeighborsClassifier()
model2 = cross_val_score(knnCrossVal, X , y , cv=6)

print(f"Scores: {model2}")
print("Mean Accuracy:", model2.mean())

"""
Scores: [0.96 1.   0.92 0.92 1.   1.  ]
Mean Accuracy: 0.9666666666666667

the scores accross the folds and the mean accuracy 
indicate the model is not overfitting on the train data
so we will go ahead and save our previous model.

"""

joblib.dump(model, 'knn_model.pkl')
print("Model saved successfully as knn_model.pkl")