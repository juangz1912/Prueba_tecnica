from django.db import models
from django.contrib.auth.models import User

class Amenity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        unique_together = ('amenity', 'start_time')

    def __str__(self):
        return f'{self.amenity} reserved by {self.user} from {self.start_time} to {self.end_time}'

    @staticmethod
    def is_time_available(amenity, start_time, end_time):
        reservations = Reservation.objects.filter(
            amenity=amenity,
            start_time__lt=end_time,
            end_time__gt=start_time
        )
        return not reservations.exists()
