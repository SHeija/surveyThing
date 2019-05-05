from django.urls import include, path

from . import views
from django.views.generic.base import TemplateView

#app_name='accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.index), #?????
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('index/', views.index), #????
    path('profile/', views.profile),   
]