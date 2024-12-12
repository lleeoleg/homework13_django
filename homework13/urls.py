from django.contrib import admin
from django.urls import path, re_path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', view_all_tasks, name='view_all_tasks'),
    path('add_task/', add_task, name='add_task'),
    path('edit_task/<int:id>/', edit_task, name='edit_task'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
    re_path(r'^tasks/(?P<task_id>\d+)/$', view_one_task, name='view_one_task')
]
