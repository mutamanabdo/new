from django.urls import path
from .views import client_list, client_detail , client_add , client_delete , client_edit
urlpatterns = [
    path('', client_list,name='client_list'),
    path('<int:pk>/', client_detail,name="client_detail"),
    path('add-client/', client_add,name="client_add"),
    path('<int:pk>/delete/', client_delete,name='client_delete'),
    path('<int:pk>/edit/',client_edit,name='client_edit'),
]
