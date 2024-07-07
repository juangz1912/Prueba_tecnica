from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['shift']

    def __init__(self, *args, **kwargs):
        self.amenity = kwargs.pop('amenity', None)
        super(ReservationForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        shift = cleaned_data.get('shift')

        if shift and self.amenity:
            if not Reservation.is_shift_available(self.amenity, shift):
                raise forms.ValidationError('El turno seleccionado ya está ocupado.')
        return cleaned_data
