
from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    
    path('',views.index),
    path('signup/',views.signUp),
    path('after_signup/',views.after_signup),
    path('afterlogin/',views.afterlogin),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path("API/",views.UserAPI.as_view()),
    path('logout/',views.logout),
    path('afterlogin/update/<int:pk>',views.Update_data.as_view(),name="update_view"),
    path('afterlogin/delete/<int:pk>',views.Delete_data.as_view(),name="delete_view"),
    
]
