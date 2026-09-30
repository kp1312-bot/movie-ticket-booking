from rest_framework import serializers

from base.models import Movie, Show, Seat, Booking, BookingSeat, Payment


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = "__all__"


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"


class BookingSeatSerializer(serializers.ModelSerializer):
    seat_number = serializers.CharField(
        source="seat.seat_number",
        read_only=True
    )

    class Meta:
        model = BookingSeat
        fields = ["id", "seat", "seat_number"]


class BookingSerializer(serializers.ModelSerializer):
    seats = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = [
            "id",
            "user",
            "show",
            "total_amount",
            "status",
            "booking_date",
            "seats"
        ]

    def get_seats(self, obj):
        booking_seats = BookingSeat.objects.filter(booking=obj)
        return BookingSeatSerializer(
            booking_seats,
            many=True
        ).data


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'id',
            'amount',
            'payment_method',
            'payment_status',
            'transaction_id',
            'created_at'
        ]