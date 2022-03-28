from django.urls import path, include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from snippets.views import SnippetViewSet, UserViewSet

# snippet_list = SnippetViewSet.as_view(actions={
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view(actions={
#     'get': 'retreive',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view(actions={
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view(actions={
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view(actions={
#     'get': 'retreive'
# })
#
#
# urlpatterns = format_suffix_patterns({
#     path('',
#          views.api_root),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#
#     path('users/', user_list, name='user-list'),
#     path('user/<int:pk>/', user_detail, name='user-detail'),
# })


# Create a router and register our viesets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename="snippets")
router.register(r'users', views.UserViewSet, basename="users")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

