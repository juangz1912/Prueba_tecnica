from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Amenity, Reservation
from .forms import ReservationForm
from django.utils import timezone

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
    reservations = Reservation.objects.filter(user=request.user, end_time__gt=timezone.now())
    return render(request, 'my_reservation.html', {'reservations': reservations})

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
