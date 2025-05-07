
from django.contrib import admin
from django.urls import path, include
from tasks import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('auth/', include('accounts.urls')),
    path('tasks/', include('tasks.urls')),

    path('services/', views.services, name='services'),

    path("__reload__/", include("django_browser_reload.urls")),
]
