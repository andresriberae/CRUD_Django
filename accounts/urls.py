from django.urls import path
from .views import signin, signout, signup


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='logout'),
    path('signin/', signin, name='signin'),

]