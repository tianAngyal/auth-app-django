from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('signup/', views.signup_user, name="signup"),
    path('logout/', views.logout_user, name="logout"),
    path('get-csrf-token/', views.get_csrf_token, name="get_csrf_token"),
    path('get-user-info/', views.get_user_info, name='get_user_info')
]
