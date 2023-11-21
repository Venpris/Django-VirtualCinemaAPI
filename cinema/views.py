from rest_framework.views import APIView 
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Movie, Ticket
from .serializers import MovieSerializer, TicketSerializer
from django.utils import timezone

# #GET REQUESTS
# class MovieListView(APIView):
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
# class TicketListView(APIView):
#     def get(self, request, title):
#         movie = Movie.objects.get(title=title)
#         tickets = Ticket.objects.filter(movie=movie, is_available=True)
#         serializer = TicketSerializer(tickets, many=True)
#         return Response(serializer.data)
    
# #POST REQUESTS
# class MovieCreateView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():   
#             movie_showing = serializer.save()
#             self.create_tickets_for_movie(movie_showing)
#         return Response(serializer.data)
    
#     def create_tickets_for_movie(self, movie_showing):
#         for i in range(movie_showing.number_of_seats):
#             Ticket.objects.create(movie=movie_showing, seat_number=i+1, price=movie_showing.price)
    
# #PUT REQUESTS
# class PurchaseTicketView(APIView):
#     def put(self, request, pk):
#         ticket = get_object_or_404(Ticket, pk=pk)
#         if ticket.is_available:
#             ticket.sold_on = timezone.now()
#             ticket.customer = request.user
#             ticket.is_available = False
#             ticket.save()
#             serializer = TicketSerializer(ticket)
#             return Response(serializer.data)
#         else:
#             return Response({"message": "Seat is not available"}, status=status.HTTP_400_BAD_REQUEST)

# class RefundTicketView(APIView):
#     def put(self, request, pk):
#         ticket = get_object_or_404(Ticket, pk=pk)
#         if ticket.customer == request.user:
#             ticket.is_refunded = True
#             ticket.is_available = True
#             ticket.save()
#             serializer = TicketSerializer(ticket)
#             return Response(serializer.data)
#         else:
#             return Response({"message": "Ticket not available for refund"}, status=status.HTTP_400_BAD_REQUEST)

class MovieViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Movie.objects.all()  
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)
    
class TicketViewSet(viewsets.ViewSet):
    def list(self, request, title):
        movie = Movie.objects.get(title=title)
        tickets = Ticket.objects.filter(movie=movie, is_available=True)
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)
