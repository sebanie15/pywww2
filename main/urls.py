from django.urls import path
from .views import main_views

urlpatterns = [
    path('', main_views),

]
