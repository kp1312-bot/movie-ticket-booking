from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField()
    genre = models.CharField()
    language = models.CharField()
    duration = models.IntegerField()
    release_date = models.DateField()
    poster = models.ImageField(upload_to = 'photo')
    status = models.BooleanField(default = True)

    def __str__(self):
        return self.title

class Show(models.Model):
        movie = models.ForeignKey(Movie, on_delete = models.CASCADE,related_name = 'shows')
        show_date = models.DateField()
        show_time = models.TimeField()
        screen = models.CharField()

        def __str__(self):
            return f"{self.movie.title} - {self.show_date} - {self.show_time}"

class Seat(models.Model):
        show = models.ForeignKey(Show, on_delete = models.CASCADE,related_name = 'seats')
        seat_number = models.CharField()
        is_booked = models.BooleanField(default = False)

        def __str__(self):
            return f"{self.show.movie.title} - {self.seat_number}"

class Booking(models.Model):
        user = models.ForeignKey(User, on_delete = models.CASCADE,related_name = 'bookings')
        show = models.ForeignKey(Show, on_delete = models.CASCADE,related_name = 'bookings')
        booking_date = models.DateField(auto_now_add = True)
        total_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
        status = models.CharField(max_length = 20, default = "Confirmed")

        def __str__(self):
            return f"{self.user.username} - {self.show.movie.title}"

class BookingSeat(models.Model):
        booking = models.ForeignKey(Booking, on_delete = models.CASCADE,related_name = 'bookingseat')
        seat = models.ForeignKey(Seat, on_delete = models.CASCADE,related_name = 'bookingseat')
        class Meta:
            constraints = [models.UniqueConstraint(fields=['booking','seat'],name = 'unique_booking_seat')]
        def __str__(self):
            return f"{self.booking.id} - {self.seat.seat_number}"

class Payment(models.Model):
    PAYMENT_METHOD_CHOCIES = [
        ('UPI','UPI'),('CARD','CARD')
    ]
    PAYMENT_STATUS_CHOICES = [
        ('PENDING','Pending'),('SUCCESS','Success'),('FAILED','Failed')
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES,default='PENDING')
    transaction_id = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.transaction_id                                            
