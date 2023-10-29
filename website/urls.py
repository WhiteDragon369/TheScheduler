from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('timetable/', views.time_table, name='time_table'),
    path('update/', views.update, name='update'),
]