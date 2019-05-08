from django.urls import include, path

from . import views
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url="login/", permanent=False)),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.profile),   
    path('bye/', views.bye), #logout destination 
]