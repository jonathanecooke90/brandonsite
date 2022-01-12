from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('', views.HomePageView.as_view(), name='home'),
    path('reels/', views.ReelsView.as_view(), name='reels'),
    path('contact/', views.contactview, name='contact')
]
