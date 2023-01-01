from django.urls import path
from . import views

urlpatterns = [
    path('', views.toLogin_view),
    # path('signout/', views.signout),
    # path('index/', views.Login_view),
    # path('department/', views.department),
]
