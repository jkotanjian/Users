from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('new/', views.new, name="new"),
	path('new/create/', views.new_create, name="new_create"),
	path('<id>/edit/', views.edit, name="edit"),
	path('<id>/update/', views.update, name="update"),
	path('<id>/', views.show, name="show"),
	path('<id>/delete/', views.delete, name="delete"),
]