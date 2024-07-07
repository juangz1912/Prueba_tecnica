from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['start_time', 'end_time']

    def __init__(self, *args, **kwargs):
        self.amenity = kwargs.pop('amenity', None)
        super(ReservationForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time and self.amenity:
            if not Reservation.is_time_available(self.amenity, start_time, end_time):
                raise forms.ValidationError('El horario seleccionado ya está ocupado.')
        return cleaned_data
