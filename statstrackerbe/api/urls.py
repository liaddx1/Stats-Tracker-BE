from django.urls import path
from .views import *

urlpatterns = [
    path(
        "user/update-history/",
        UserUpdateHistoryAPIView.as_view(),
        name="user-update-history",
    ),
    path(
        "user/questionnaire/",
        UserQuestionnaireView.as_view(),
        name="user-questionnaire",
    ),
    path("contact-us/", ContactUsView.as_view(), name="contact-us"),
]
