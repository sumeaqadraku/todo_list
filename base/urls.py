# Importing the necessary Django modules
from django.urls import path
from . import views  # Importing views from the current directory (base app)

# Defining the URL patterns for the base app
urlpatterns = [
    path('', views.taskList, name='tasks'),  # Root URL (home page) points to the `taskList` view
]
