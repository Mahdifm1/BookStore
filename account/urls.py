from django.urls import path, include

from account.views import SignUp, Dashboard

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("signup/", SignUp.as_view(), name='signup'),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
]
