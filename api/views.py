from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from base.models import Movie, Show, Seat, Booking, BookingSeat,Payment
from rest_framework.permissions import IsAuthenticated
from .utils import reset_expired_show_seats
# from .serializers import PaymentSerializer import uuid

from .serializers import (
    MovieSerializer,
    ShowSerializer,
    SeatSerializer,
    BookingSerializer,
    PaymentSerializer 
)
import uuid


class MovieAPI(APIView):

    def get(self, request):

        movies = Movie.objects.filter(status=True)

        serializer = MovieSerializer(
            movies,
            many=True
        )

        return Response(serializer.data)


class ShowAPI(APIView):

    def get(self, request):
        movie_id = request.query_params.get("movie_id")
        if movie_id:shows = Show.objects.filter(movie_id=movie_id)
        else:
            shows = Show.objects.all()
        serializer = ShowSerializer(shows,many=True)
        return Response(serializer.data)    


class SeatAPI(APIView):

    def get(self, request, show_id):

        # Reset seats for shows that have already ended
        reset_expired_show_seats()

        seats = Seat.objects.filter(
            show_id=show_id
        )

        serializer = SeatSerializer(
            seats,
            many=True
        )

        return Response(serializer.data)


class BookingAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        bookings = Booking.objects.filter(
            user=request.user
        ).order_by("-id")

        data = []

        for booking in bookings:

            seats = BookingSeat.objects.filter(
                booking=booking
            )

            seat_names = [
                booking_seat.seat.seat_number
                for booking_seat in seats
            ]

            data.append({
                "booking_id": booking.id,
                "movie": booking.show.movie.title,
                "show_date": booking.show.show_date,
                "show_time": booking.show.show_time,
                "screen": booking.show.screen,
                "seats": seat_names,
                "total_amount": booking.total_amount,
                "status": booking.status
            })

        return Response(data)


    def post(self, request):

        show_id = request.data.get("show")
        seat_ids = request.data.get("seats")

        if not show_id:
            return Response(
                {"error": "Show ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not seat_ids:
            return Response(
                {"error": "Please select seats"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            show = Show.objects.get(id=show_id)

        except Show.DoesNotExist:
            return Response(
                {"error": "Show not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        seats = Seat.objects.filter(
            id__in=seat_ids,
            show=show
        )

        if seats.count() != len(seat_ids):
            return Response(
                {"error": "Some seats are invalid"},
                status=status.HTTP_400_BAD_REQUEST
            )

        booked_seats = seats.filter(is_booked=True)

        if booked_seats.exists():
            return Response(
                {"error": "One or more selected seats are already booked"},
                status=status.HTTP_400_BAD_REQUEST
            )

        ticket_price = 150

        total_amount = seats.count() * ticket_price

        booking = Booking.objects.create(
            user=request.user,
            show=show,
            total_amount=total_amount,
            status="Confirmed"
        )

        for seat in seats:

            BookingSeat.objects.create(
                booking=booking,
                seat=seat
            )

            seat.is_booked = True
            seat.save()

        return Response({
            "message": "Booking successful",
            "booking_id": booking.id,
            "movie_id":show.movie.id,
            "movie_title": show.movie.title,
            "show_id": show.id,
            "show_date": show.show_date,
            "show_time": show.show_time,
            "screen":show.screen,
            "seats": [
                seat.seat_number
                for seat in seats
            ],
            "ticket_price": ticket_price,
            "total_amount": total_amount,
            "status": booking.status
        }, status=status.HTTP_201_CREATED)



class PaymentAPI(APIView):

    def post(self, request):

        print("========== PAYMENT REQUEST ==========")
        print("USER:", request.user)
        print("AUTHENTICATED:", request.user.is_authenticated)
        print("DATA:", request.data)

        if not request.user.is_authenticated:

            return Response(
                {
                    "error": "Please login before making payment."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        amount = request.data.get("amount")
        payment_method = request.data.get("payment_method")

        print("AMOUNT:", amount)
        print("PAYMENT METHOD:", payment_method)

        if not amount:

            return Response(
                {
                    "error": "Amount is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if payment_method not in ["UPI", "CARD"]:

            return Response(
                {
                    "error": "Invalid payment method"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:

            transaction_id = (
                "TXN" +
                uuid.uuid4().hex[:10].upper()
            )

            print("TRANSACTION ID:", transaction_id)

            payment = Payment.objects.create(

                user=request.user,

                amount=amount,

                payment_method=payment_method,

                payment_status="SUCCESS",

                transaction_id=transaction_id

            )

            print("PAYMENT CREATED:", payment)

            serializer = PaymentSerializer(payment)

            return Response(
                {
                    "message": "Payment successful",
                    "payment": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        except Exception as e:

            print("========== PAYMENT ERROR ==========")
            print(type(e).__name__)
            print(str(e))

            return Response(
                {
                    "error": "Payment failed",
                    "details": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )

class CancelBookingAPI(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, booking_id):

        print("CANCEL BOOKING ID:", booking_id)
        print("CANCEL USER:", request.user)
        print("AUTH:", request.user.is_authenticated)

        try:
            booking = Booking.objects.get(
                id=booking_id,
                user=request.user
            )
        except Booking.DoesNotExist:
            return Response(
                {"error": "Booking not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if booking.status == "Cancelled":
            return Response(
                {"error": "Booking is already cancelled"},
                status=status.HTTP_400_BAD_REQUEST
            )

        booking_seats = BookingSeat.objects.filter(
            booking=booking
        )

        for booking_seat in booking_seats:
            seat = booking_seat.seat
            seat.is_booked = False
            seat.save()

        booking.status = "Cancelled"
        booking.save()

        return Response(
            {
                "message": "Booking cancelled successfully",
                "booking_id": booking.id,
                "status": booking.status
            },
            status=status.HTTP_200_OK
        )