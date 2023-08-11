from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('admin-login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('admin-dashboard/', index, name="index")
]
