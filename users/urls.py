from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
   # path('',views.authors_list, name="list"),
    path('login/',views.login_view,name='login' ),
    path('register/',views.register,name='register'),
    path('logout/', views.logout_view,name ="logout"),
]