from cinema.models import Movie, Ticket
from cinema.serializers import MovieSerializer, TicketSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

#list, create, retrieve, update, partial_update, destroy
class MovieViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Movie.objects.all()  
        serializer = MovieSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Movie.objects.all()
        movie = get_object_or_404(queryset, pk=pk)
        serializer = MovieSerializer(movie, context={"request": request})
        return Response(serializer.data)
    
    def create(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():   
            movie_showing = serializer.save()
            self.create_tickets_for_movie(movie_showing)
        return Response(serializer.data)
    
class TicketViewSet(viewsets.ViewSet):
    def list(self, request, title):
        movie = Movie.objects.get(title=title)
        tickets = Ticket.objects.filter(movie=movie, is_available=True)
        serializer = TicketSerializer(tickets, many=True, context={"request": request})
        return Response(serializer.data)
    
    def create(self, request):
        movie = request.data.get("movie_id")
        number_of_tickets = request.data.get("number_of_tickets")
        for _ in range(number_of_tickets):
            ticket = Ticket.objects.filter(movie=movie, is_available=True).first()
            ticket.is_available = False
            ticket.save()
        return Response({"message": "Tickets purchased successfully"})


# class MovieViewSet(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

# class TicketViewSet(viewsets.ModelViewSet):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer