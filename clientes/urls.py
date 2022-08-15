
from django.urls import path
from .views import persons_list
from .views import person_new

urlpatterns = [
    path('list/', persons_list, name='person_list'),
    path('new/', person_new, name='person_new'),
]