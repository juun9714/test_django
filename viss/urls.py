from django.urls import path
from . import views

app_name='viss'

urlpatterns = [
    # ex: /viss/
    path('<int:result_id>/', views.result, name='result'),
]