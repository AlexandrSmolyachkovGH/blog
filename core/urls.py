from django.urls import path
from core import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('<slug:post>', views.post_single, name='post_single'),

]
