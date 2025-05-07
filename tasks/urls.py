from django.urls import path
from .views import tasks, delete_task, task_detail, complete_task

urlpatterns = [
    path('', tasks, name='tasks'),
    path('<int:task_id>/', task_detail, name='task_detail'),
    path('<int:task_id>/complete', complete_task, name='complete_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),

]