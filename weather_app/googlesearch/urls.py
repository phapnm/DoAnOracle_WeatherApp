from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    # path('search', SearchView.as_view(), name="google-search-view")
]
