from django.urls import path
from . import views

# empty path string = root folder, index file...
# in this case, it is /Products
urlpatterns = [
    path('', views.index),
    path('new/', views.new)
]
