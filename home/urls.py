from django.urls import path
from home import views

app_name="home"

urlpatterns = [
    path("", views.loginuser, name="login"),
    path("login/",views.loginuser, name="login"),
    path("register/", views.register, name="register"),
    path("index/", views.index, name="index"),
    path("Template-1",views.template, name="Template-1"),
    path("Template-2",views.template, name="Template-2"),
    path("Template-3",views.template, name="Template-3"),
    path("create-portfolio/", views.portfolio_det, name="create-portfolio"),
    path("portfolio/<slug:portfolio_url>/", views.portfolio, name="portfolio"),
    path("portfolio/", views.portfolio, name="userportfolio"),
    path("logout/",views.logoutuser, name="logout"),
]