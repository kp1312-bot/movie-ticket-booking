from django.core.management.base import BaseCommand

from api.utils import reset_expired_show_seats


class Command(BaseCommand):

    help = "Reset seats for expired movie shows"

    def handle(self, *args, **kwargs):

        result = reset_expired_show_seats()

        self.stdout.write(
            self.style.SUCCESS(
                f"Expired shows checked successfully.\n"
                f"Shows reset: {result['shows_reset']}\n"
                f"Seats reset: {result['seats_reset']}\n"
                f"Bookings expired: {result['bookings_expired']}"
            )
        )