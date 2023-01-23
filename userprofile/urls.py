from django.urls import path
from .views import singup
from django.contrib.auth import views
app_name = 'users'
urlpatterns = [
    # path("signup/", singup , name='signup'),
    # path('login/', views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    # path('logout/', views.LogoutView.as_view(template_name='registration/logout.html'))
]