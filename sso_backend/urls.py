from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/', include('sso.urls')),
]
