from django.db import models
from django.contrib.auth.models import User

class Amenity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    SHIFT_CHOICES = [
        ('07:00-08:00', '07:00-08:00'),
        ('08:00-09:00', '08:00-09:00'),
        ('09:00-10:00', '09:00-10:00'),
        ('10:00-11:00', '10:00-11:00'),
        ('11:00-12:00', '11:00-12:00'),
        ('13:00-14:00', '13:00-14:00'),
        ('14:00-15:00', '14:00-15:00'),
        ('15:00-16:00', '15:00-16:00'),
        ('16:00-17:00', '16:00-17:00'),
        ('17:00-18:00', '17:00-18:00'),
        ('18:00-19:00', '18:00-19:00'),
        ('19:00-20:00', '19:00-20:00'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES)

    class Meta:
        unique_together = ('amenity', 'shift')

    def __str__(self):
        return f'{self.amenity} reserved by {self.user} for {self.shift}'

    @staticmethod
    def is_shift_available(amenity, shift):
        reservations = Reservation.objects.filter(amenity=amenity, shift=shift)
        return not reservations.exists()

