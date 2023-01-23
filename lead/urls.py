from django.urls import path
from .views import add_lead , lead_list , lead_detail, leads_delete , edit_lead , converte_to_client

urlpatterns = [
    path('', lead_list , name='lead_list'),
    path('<int:pk>/', lead_detail,name='lead_detail'),
    path('<int:pk>/edit/', edit_lead, name='edit_lead'),
    path('<int:pk>/convert/', converte_to_client, name='convert_to_client'),
    path('<int:pk>/delete/', leads_delete, name='lead_delete'),
    path('add-lead/', add_lead , name='add-lead'),
]

