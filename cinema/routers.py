from cinema.viewsets import MovieViewSet, TicketViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movies', MovieViewSet, basename='movie')
router.register('tickets', TicketViewSet, basename='ticket')