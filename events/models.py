from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Event(models.Model):
    title = models.CharField(
        max_length=100
    )
    description = models.TextField()
    date = models.DateField()

    location = models.CharField(
        max_length=100
    )
    participants = models.ManyToManyField(
        User,
        blank=True,
        related_name='events'
    )
    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='organized_events',
        null=True,  # Позволява NULL за старите записи
        blank=True,  # Не изисква поле в админ формата
    )

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )
    booking_date = models.DateTimeField(
        auto_now_add=True
    )
    status = models.CharField(
        max_length=50,
        choices=[
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('cancelled', 'Cancelled'),
        ])

    def __str__(self):
        return f'{self.user.username} - {self.event.title}'


class TestModel(models.Model):
    title = models.CharField(
        max_length=100
    )
    image = models.ImageField(
        upload_to='images/'
    )

    def __str__(self):
        return self.title
