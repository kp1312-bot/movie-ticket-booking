from django import forms
from .models import Movie,Show,Seat,Booking,BookingSeat

class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title','description','genre','language','duration','release_date','poster','status']

class ShowModelForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['movie','show_date','show_time','screen']

class SeatModelForm(forms.ModelForm):
    class Meta:
        model = Seat
        fields = ['show','seat_number','is_booked']

class BookingModelForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user','show','total_amount','status']

class BookingSeatModelForm(forms.ModelForm):
    class Meta:
        model = BookingSeat
        fields = ['booking','seat']                             