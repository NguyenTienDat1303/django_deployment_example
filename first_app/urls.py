from django.urls import path
from first_app import views

app_name = 'first_app'
urlpatterns = [
    # url(r'^&', views.indexLogin, name="index_login")
    # url(r'^&', views.indexLogin, name="index_login")
    path('', views.user_list, name="user"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('register/', views.register, name="register"),
    path('user_login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="logout"),
    path('special/', views.special, name="special")
]
