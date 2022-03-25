from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = {
    path('', views.SnippetList.as_view()),
    path('<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserList.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)
