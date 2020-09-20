  
from django.contrib import admin
from django.urls import path, include
from .views import HomePageView, SearchResultsView

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('search/', SearchResultsView.as_view(), name='search_results'),     
    path('', HomePageView.as_view(), name='home'),
]