from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.exhibition_home, name='home'),
    path('signup/', views.register_curator, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.curator_profile, name='profile'),
    path('artwork/<int:artwork_id>/', views.artwork_detail, name='artwork_detail'),
    path('artwork/<int:artwork_id>/like/', views.toggle_like, name='toggle_like'),
]