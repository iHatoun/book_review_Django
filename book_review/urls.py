from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')),
    path('', include('users.urls')),  # ربط المسارات الخاصة بالمصادقة

]
