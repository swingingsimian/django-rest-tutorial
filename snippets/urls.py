from django.urls import path  # , include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

# These still require trailing slashes or suffixes, e.g. .json
# or .api (for browsable api docs), this returns the html api view, but .html does not work,
# despite working if set as header?

urlpatterns = [
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight')
]

urlpatterns = format_suffix_patterns(urlpatterns)
