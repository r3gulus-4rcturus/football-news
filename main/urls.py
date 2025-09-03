from django.urls import path
from main.views import show_main

# namespace unik sbg pembeda dengan aplikasi lain pada URL
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main')
]