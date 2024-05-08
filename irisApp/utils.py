import joblib

def loadModel():
	model = joblib.load("irisApp\knn_model.pkl")
	return model