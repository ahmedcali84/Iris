from django.urls import path

from . import views


urlpatterns = [
	path("" , views.index , name="index"),
	path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

	# API Routes
	path("flowers",views.getClass ,name="getClass"),
	path("flowers/<int:flower_id>",views.getFlower ,name="getFlower"),
	path("flowers/<str:page>", views.getPage , name="getPage")

]