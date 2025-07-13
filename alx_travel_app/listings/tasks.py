from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_email(to_email, listing_title):
    subject = 'Booking Confirmation'
    message = f'Thank you for booking {listing_title}!'
    from_email = 'no-reply@alxtravel.com'

    send_mail(subject, message, from_email, [to_email])

