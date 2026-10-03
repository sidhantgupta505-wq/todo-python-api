from django.urls import path
from .views import todo_list, todo_detail

urlpatterns = [
    path('todos/', todo_list),
    path('todos/<int:id>/', todo_detail),
]