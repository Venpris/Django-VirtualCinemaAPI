from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    duration = models.DurationField()
    genre = models.CharField(max_length=50)
    show_time = models.DateTimeField()
    seats = models.IntegerField()
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

class Ticket(models.Model):
    seat_number = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    price = models.FloatField(default=0.0)
    sold_on = models.DateTimeField(auto_now_add=True)
    is_refunded = models.BooleanField(default=False)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie.title} - {self.seat_number}"