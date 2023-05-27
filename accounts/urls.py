from django.urls import path

from accounts import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('homepage', views.homepage, name='homepage'),
    path('logout', views.logout, name='logout'),
    path('Search', views.Search, name='Search'),
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('playlist', views.playlist, name='playlist'),
    path('remove', views.remove, name='playlist'),
    path('changePassword',views.changePassword, name="change"),
    path('changePasswordForm',views.changePasswordForm, name="changeForm"),
path('Recommendation', views.recommendation, name='recommendation'),
]
