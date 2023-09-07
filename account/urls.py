from django.urls import path, include

from account.views import SignUp

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("signup/", SignUp.as_view(), name='signup'),
]