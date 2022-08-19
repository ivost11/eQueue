from django.urls import path
from .views import index, add_queue, get_queue


urlpatterns = [
    path('', index, name='index'),
    path('queue/<int:queue_id>/', get_queue, name='view_queue'),
    path('queue/add-queue/', add_queue, name='add_queue'),
]
