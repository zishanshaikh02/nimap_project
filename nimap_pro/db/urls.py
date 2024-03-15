from django.urls import path
from .views import ClientViewSet, ProjectViewSet ,AssignedProjectsListAPIView

urlpatterns = [
    path('clients/', ClientViewSet.as_view(actions={'get': 'list', 'post': 'create'}), name='clients'),
    path('clients/<int:pk>/', ClientViewSet.as_view(actions={'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='client-detail'),
    path('projects/', ProjectViewSet.as_view(actions={'get': 'list', 'post': 'create'}), name='projects'),
    path('projects/<int:pk>/', ProjectViewSet.as_view(actions={'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='project-detail'),
    path('projects/assigned/', AssignedProjectsListAPIView.as_view(), name='assigned-projects'),
    
 



]
