from django.urls import path
from mindtree import views
urlpatterns = [
    
    path('',views.get_jobs,name='job list'),
]