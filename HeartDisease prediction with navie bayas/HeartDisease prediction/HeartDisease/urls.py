from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HeartDiseaseApp.urls')),  # delegate root URLs to the app
]
