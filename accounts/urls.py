from django.urls import include, path

from . import views
from django.views.generic.base import TemplateView

#app_name='accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.profile),   
    path('bye/', views.bye), #logout destination 

]