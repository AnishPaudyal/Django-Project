from django.urls import path
from . import views


app_name = "main"


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("profile", views.profile, name="profile"),
    path("sell", views.sell, name="sell"),
    path("allproduct", views.allproduct, name="allproduct"),
    path("brand/<slug:slug>",views.brands,name="brands"),
    path("categories/<slug:slug>",views.categories,name="categories"),
    path("detail/<int:id>",views.productdetail,name="productdetail")
]