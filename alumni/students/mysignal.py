from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from . models import Notice
from students.models import Profile
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwarg ):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Notice)
def sendmail(sender, instance, created, **kwarg ):
    if created:
        emails = User.objects.values_list('email', flat=True)
        message = instance.subject
        for email in emails:
            send_mail('contact form',
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently = False)
        
        # Profile.objects.create(user=instance)
        
