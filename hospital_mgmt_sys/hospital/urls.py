from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('admin-login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('admin-dashboard/', index, name="index"),
    path('view-doctor/', view_doctor, name="view_doctor"),
    path('add-doctor/', add_doctor, name="add_doctor"),
    path('delete-doctor/<int:pk>/', delete_doctor, name="delete_doctor"),
    path('add-patient/', add_patient, name="add_patient"),
    path('view-patient/', view_patient, name="view_patient"),
    path('delete-patient/<int:pk>/', delete_patient, name="delete_patient"),

]
