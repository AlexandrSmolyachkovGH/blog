from django.urls import path
from core import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', views.HomeView.as_view(), name='registration'),
    path('search/', views.PostSearch.as_view(), name='post_search'),
    path('<slug:post>/', views.post_single, name='post_single'),
    path('tag/<slug:tag>/', views.TagListView.as_view(), name='tag_post'),

]
