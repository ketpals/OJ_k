"""onlinejudge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from judge import views as jv
from users import views as uv

urlpatterns = [
    path('', uv.index),
    path('judge/', jv.intro),
    path('judge/problem', jv.view_problems),
    path('judge/<int:problem_id>/', jv.problem_detail),
    path('judge/add-problem/', jv.add_problem),
    path('judge/<int:problem_id>/judge/submit/', jv.submit),
    path('login', uv.loginuser),
    path('logout', uv.logoutuser),
    path('admin/', admin.site.urls),
]
