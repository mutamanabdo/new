from django.contrib.auth import views
from django.contrib import admin
from django.urls import path, include
from userprofile.views import singup , index

urlpatterns = [
    path('' , index, name='index'),
    path('admin/', admin.site.urls),
    path('signup/', singup, name="signup"),
    path('login/' , views.LoginView.as_view(template_name='registration/login.html' , redirect_field_name='index'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('dashboard/clients/', include('client.urls')),
    path('dashboard/' , include("dashboard.urls")),
    path('dashboard/leads/', include('lead.urls')),
]
