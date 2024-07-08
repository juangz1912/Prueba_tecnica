from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Amenity, Reservation
from .forms import ReservationForm
from django.contrib import messages


@login_required
def home(request):
    amenities = Amenity.objects.all()
    return render(request, 'home.html', {'amenities': amenities})

@login_required
def create_reservation(request, amenity_id):
    amenity = get_object_or_404(Amenity, id=amenity_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, amenity=amenity)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.amenity = amenity
            reservation.save()
            return redirect('base:home')
    else:
        form = ReservationForm(amenity=amenity)
    return render(request, 'create_reservation.html', {'form': form, 'amenity': amenity})


@login_required
def my_reservations(request):
    if request.method == 'POST':
        reservation_id = request.POST.get('reservation_id')
        reservation = get_object_or_404(Reservation, id=reservation_id)
        if reservation.user == request.user:
            reservation.delete()
            messages.success(request, '¡Reserva cancelada correctamente!')
            return redirect('base:my_reservations')
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'my_reservation.html', {'reservations': reservations})


def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('base:home')
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

