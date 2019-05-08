#top-level urls

from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('surveys/', include('surveys.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url="accounts/login", permanent=False))
]
