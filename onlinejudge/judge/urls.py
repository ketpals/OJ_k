from django.urls import path

from . import views
app_name = 'judge'

urlpatterns = [
    path('judge/problem', views.view_problems, name='view_problems'),
    path('judge/problem/<int:problem_id>/', views.problem_detail, name='problem_detail'),

]