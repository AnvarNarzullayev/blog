from django.urls import path
from .views import user_login, signup, user_update, userprofile

urlpatterns = [
    path('', user_login, name="login"),
    path('signup', signup, name = "signup"),
    path('settings/<slug:slug_name>', user_update, name="settings"),
    path('accounts/<slug:slug_name>',userprofile,name = 'profil')
]