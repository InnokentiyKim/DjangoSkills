from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import login_view, get_cookie_view, set_cookie_view, set_session_view, get_session_view, AboutMeView, \
    RegisterView, logout_view, FooBarView

app_name = "myauth"

urlpatterns = [
    path("login/", LoginView.as_view(
        template_name="myauth/login.html",
        redirect_authenticated_user=True,
    ), name="login"),
    # path("logout", logout_view, name="logout"),
    path("logout/", logout_view, name="logout"),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path("register/", RegisterView.as_view(), name="register"),
    path('cookie/get/', get_cookie_view, name="cookie-get"),
    path('cookie/set/', set_cookie_view, name="cookie-set"),
    path('session/set/', set_session_view, name="session-set"),
    path('session/get/', get_session_view, name="session-get"),
    path('foo-bar/', FooBarView.as_view(), name="foo-bar"),
]