from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', view=auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', view=auth_views.LogoutView.as_view(), name='logout'),
    path('register/', view=views.register, name='register'),

]
