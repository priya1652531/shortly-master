from django.contrib import admin
from django.urls import path
from authentication.views import login, signup, logout
from urlhandler.views import dashboard, generate, home, deleteurl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  dashboard, name="dashboard"),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
    path('logout/', logout, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('generate/', generate, name="generate"),
    path('deleteurl/', deleteurl, name="deleteurl"),
    path('<str:query>/', home, name="home"),
]
