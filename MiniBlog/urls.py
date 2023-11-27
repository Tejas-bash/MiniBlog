"""MiniBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Blog import views
from rest_framework import routers
from Blog import views

router = routers.DefaultRouter()
router.register(r"users", views.Userviewset)
router.register(r"posts", views.Postviewset)
router.register(r"groups", views.GroupViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="Home"),
    path("About/", views.about, name="About"),
    path("Contact/", views.contact, name="Contact"),
    path("Singup/", views.user_singup, name="Singup"),
    path("login/", views.user_login, name="Login"),
    path("Userlogout/", views.user_logout, name="Userlogout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("admin/", views.Aadmin, name="admin"),
    path("addpost/", views.Add_post, name="addpost"),
    path("updatepost/<int:id>/", views.update_post, name="updatepost"),
    path("delete/<int:id>/", views.delete_post, name="deletepost"),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
