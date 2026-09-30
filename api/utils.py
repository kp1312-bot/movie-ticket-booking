from django.utils import timezone
from django.db import transaction

from base.models import Show, Seat, Booking


def reset_expired_show_seats():

    now = timezone.localtime()

    current_date = now.date()
    current_time = now.time()

    expired_shows = Show.objects.filter(
        show_date__lt=current_date
    )

    expired_today_shows = Show.objects.filter(
        show_date=current_date,
        show_time__lt=current_time
    )

    shows = expired_shows | expired_today_shows

    total_shows = 0
    total_seats = 0
    total_bookings = 0

    for show in shows.distinct():

        with transaction.atomic():

            seats = Seat.objects.filter(
                show=show,
                is_booked=True
            )

            seat_count = seats.count()

            seats.update(
                is_booked=False
            )

            bookings = Booking.objects.filter(
                show=show,
                status="Confirmed"
            )

            booking_count = bookings.count()

            bookings.update(
                status="Expired"
            )

            if seat_count > 0:

                total_shows += 1
                total_seats += seat_count

            total_bookings += booking_count

    return {
        "shows_reset": total_shows,
        "seats_reset": total_seats,
        "bookings_expired": total_bookings
    }