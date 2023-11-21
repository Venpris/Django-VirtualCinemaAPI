from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("movies/", views.MovieListView.as_view(), name="movie-list"),
    path("movies/<str:title>/tickets/", views.TicketListView.as_view(), name="ticket-list"),
    path("tickets/<int:pk>/", views.PurchaseTicketView.as_view(), name="ticket-purchase"),
    path("movies/post/", views.MovieCreateView.as_view(), name="movie-create"),
]

urlpatterns = format_suffix_patterns(urlpatterns)