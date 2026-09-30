from django.urls import path
from . import views

urlpatterns = [
    # Movie
    path('', views.create, name = 'create'),
    path('read', views.read, name = 'read'),
    path('update/<int:did>', views.update, name = 'update'),
    path('delete/<int:did>', views.delete, name = 'delete'),
    # Show

    path('show_create', views.show_create, name = 'show_create'),
    path('show_read', views.show_read, name = 'show_read'),
    path('show_update/<int:sid>', views.show_update, name = 'show_update'),
    path('show_delete/<int:sid>', views.show_delete, name = 'show_delete'),

    # Seat
    path('seat_create',views.seat_create, name = 'seat_create'),
    path('seat_read', views.seat_read, name = 'seat_read'),
    path('seat_update/<int:sis>', views.seat_update, name = 'seat_update'),
    path('seat_delete/<int:sis>', views.seat_delete, name = 'seat_delete'),

    #Booking
    path('booking_create', views.booking_create, name = 'booking_create'),
    path('booking_read', views.booking_read, name = 'booking_read'),
    path('booking_update/<int:bib>', views.booking_update, name = 'booking_update'),
    path('booking_delete/<int:bib>', views.booking_delete, name = 'booking_delete'),

    #BookingSeat

    path('bookseat_create', views.bookseat_create, name = 'bookseat_create'),
    path('bookseat_read', views.bookseat_read, name = 'bookseat_read'),
    path('bookseat_update/<int:bs>', views.bookseat_update, name = 'bookseat_update'),
    path('bookseat_delete/<int:bs>', views.bookseat_delete, name = 'bookseat_delete')

    
]