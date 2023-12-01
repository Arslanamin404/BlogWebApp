from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('add_post', views.add_post, name="add_post"),
    path('read_more/<int:post_id>/', views.read_more, name="read_more"),
    path('delete/<int:post_id>/', views.delete, name="delete"),
    path('update_post/<int:post_id>/', views.update_post, name="update_post"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]
