from django.test import TestCase
from .models import *
from .utils import loadModel

# Create your tests here.
class IrisTestCase(TestCase):
	
	def setUp(self) -> None:
		User.objects.create(username="axmed", email="axmed@m.com")
		
	def test_prediction_1(self):
		model = loadModel()
		predict = model.predict([[2,3,4,5]])
		user = User.objects.get(username="axmed")
		IrisModel.objects.create(user = user , sepal_length = 2, sepal_width = 3, petal_length = 4, petal_width = 5, prediction = "virginica")
		iris = IrisModel.objects.filter(user=user).first()
		print(iris.prediction, predict)
		self.assertEqual(str(iris.prediction), str(predict[0]))
		