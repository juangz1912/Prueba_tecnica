from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['shift']

    def __init__(self, *args, **kwargs):
        self.amenity = kwargs.pop('amenity', None)
        super(ReservationForm, self).__init__(*args, **kwargs)
        if self.amenity:
            reserved_shifts = Reservation.objects.filter(amenity=self.amenity).values_list('shift', flat=True)
            available_shifts = [(shift, shift) for shift, _ in self.fields['shift'].choices if shift not in reserved_shifts]
            self.fields['shift'].choices = available_shifts

    def clean(self):
        cleaned_data = super().clean()
        shift = cleaned_data.get('shift')

        if shift and self.amenity:
            if not Reservation.is_shift_available(self.amenity, shift):
                raise forms.ValidationError('El turno seleccionado ya está ocupado.')
        return cleaned_data
