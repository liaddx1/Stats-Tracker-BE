from django.contrib import admin
from django.urls import path, include
from api.views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Admin Endpoints
    path("admin/", admin.site.urls),
    # Auth Endpoints
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", CustomTokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "api/token/user/",
        CurrentUserView.as_view(),
        name="get-user-by-toekn",
    ),
    # User Endpoints
    path("api/user/profile/<user_id>/", UserProfileView.as_view(), name="user_profile"),
    # API Endpoints
    path("api/", include("api.urls")),
]
