from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieAPI.as_view(), name='movie_api'),
    path('shows/', views.ShowAPI.as_view(), name='show_api'),
    path('seats/<int:show_id>/', views.SeatAPI.as_view(), name='seat_api'),
    path('bookings/',views.BookingAPI.as_view(),name = 'booking'),
    path('payment/',views.PaymentAPI.as_view(), name = 'payment'),
    path('bookings/<int:booking_id>/cancel/',views.CancelBookingAPI.as_view(), name = 'cancel_booking')
]