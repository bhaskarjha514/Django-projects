from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from . models import Notice,Profile
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
        message = instance.msg
        noticebranch =instance.branch
        profiles = Profile.objects.all()
        e=1
        while noticebranch != None:
            for i in profiles:
                if i.branch == noticebranch:
                    emailid= emails[e]
                    send_mail('From Aravali College',
                    message,
                    settings.EMAIL_HOST_USER,
                    [emailid],
                    fail_silently = False)
                e+=1
            break
        while noticebranch == None:
            for email in emails:
                send_mail(instance.subject,
                message,
                settings.EMAIL_HOST_USER,
               [email],
              fail_silently = False) 
            break
                