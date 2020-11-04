from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

# These still require trailing slashes or suffixes, e.g. .json
# or .api (for browsable api docs), this returns the html api view, but .html does not work,
# despite working if set as header?

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
