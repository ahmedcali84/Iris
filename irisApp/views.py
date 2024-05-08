from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect , JsonResponse , HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
import numpy as np
from .utils import loadModel
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from .models import *

def index(request):
	return render(request , "irisApp/index.html")

@login_required
@csrf_exempt
def getClass(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            sepal_length = float(data.get("sepal_length" , ""))
            sepal_width = float(data.get("sepal_width" , ""))
            petal_length = float(data.get("petal_length" , ""))
            petal_width = float(data.get("petal_width" , ""))

            model = loadModel()
            prediction = model.predict(np.array([[sepal_length, sepal_width, petal_length, petal_width]]))[0]

			

            new_flower = IrisModel( 
                user = request.user,
                sepal_length=sepal_length, 
                sepal_width=sepal_width,
                petal_length=petal_length,
                petal_width=petal_width,
                prediction=prediction
            )
            
            new_flower.save()  # Save the new_flower instance with the prediction
            return JsonResponse({"message": "Posted successfully."}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=501)
    
    else:
        return JsonResponse({"Error": "POST request Required"})

@login_required
@csrf_exempt
def getFlower(request , flower_id):
	try:
		flower = IrisModel.objects.get(pk=flower_id)
	except IrisModel.DoesNotExist:
		return JsonResponse({"error": "Flower Does Not Exist"})
	
	if request.method == "GET":
		return JsonResponse([f.serialize() for f in flower], safe=False)
	
	else:
		return JsonResponse({"error": "Method Must Be Through GET"})
     
@login_required
@csrf_exempt
def getPage(request , page):
	if page == 'Iris Flowers':
		flowers = IrisModel.objects.all().order_by("-id")
		return JsonResponse([flower.serialize() for flower in flowers] , safe=False)
	else:
		return JsonResponse({"error": "invalid Page"} , status=400)
	

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "irisApp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "irisApp/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "irisApp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "irisApp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "irisApp/register.html")
