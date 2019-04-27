from django.urls import include, path

from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.index), #?????
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('index/', views.index), #????
    path('profile/', TemplateView.as_view(template_name='registration/profile.html')),   
]