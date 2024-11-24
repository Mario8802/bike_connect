from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),         # Login view
    path('register/', views.register_view, name='register'), # Registration view
    path('logout/', views.logout_view, name='logout'),      # Logout view
    path('profile/', views.profile_view, name='profile'),   # Profile view
]
